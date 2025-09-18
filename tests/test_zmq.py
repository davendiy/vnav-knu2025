"""test_zmq.py [-h] role

-h : print this message
role : sub/pub -- either work as csv reader or as consumer.
"""

import time

import zmq

from common.conc_base import SubBase, PubBase


class TestReader(PubBase):

    sock_name = "tcp://*:5555"
    unique = True

    def __init__(self, ctx, filename):
        super().__init__(ctx)
        self.filename = filename
        self._fd = None

    def _prepare_enter(self):
        self._fd = open(self.filename)
        self._fd.__enter__()

    def _prepare_exit(self, typ, val, traceback):
        if self._fd is not None:
            self._fd.__exit__(typ, val, traceback)

    def run(self):
        if self._fd is None:
            raise ValueError("You should use `with` before running.")
        while self._running:
            line = self._fd.readline()
            self._socket.send_pyobj(line)
            time.sleep(0.01)


class TestPrinter(SubBase):

    sock_name = "tcp://localhost:5555"
    unique = False

    def _prepare_enter(self):
        pass

    def _prepare_exit(self, typ, val, traceback):
        pass

    def run(self):
        while self._running:
            line = self._socket.recv_pyobj()
            print(line)


if __name__ == "__main__":
    import sys

    if "-h" in sys.argv:
        print(__doc__)
        exit(0)

    if len(sys.argv) != 2:
        print(__doc__)
        exit(1)

    role = sys.argv[1]

    if role == "pub":

        with (
            zmq.Context() as ctx,
            TestReader(ctx, "../assets/test.csv") as reader,
        ):
            reader.start()
            i = 0
            while True:
                print(f"click reader #{i}")
                time.sleep(1)
                i += 1
    else:

        with zmq.Context() as ctx, TestPrinter(ctx) as printer:
            printer.start()
            i = 0
            while True:
                print(f"click printer #{i}")
                time.sleep(1)
                i += 1
