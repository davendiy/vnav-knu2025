"""pub_linux.py [-h] filename
Simple ZMQ data provider.

Parameters:
    filename : name of csv which should be used as data provider
    -h : show this message
"""

import time
import threading
import zmq


class DataProvider:

    sock_name = "ipc://@data.socket"

    def __init__(self, ctx, filename):
        self.ctx = ctx
        self.socket = None
        self._running = False
        self._worker = threading.Thread(target=self.run)
        self._filename = filename
        self._fd = None

    def __enter__(self):
        self.socket = self.ctx.socket(zmq.PUB)
        self.socket.bind(self.sock_name)
        self.socket.__enter__()

        self._fd = open(self._filename)
        self._fd.__enter__()
        return self

    def __exit__(self, typ, val, traceback):
        if self.socket is not None:
            self.socket.__exit__(typ, val, traceback)
        if self._fd is not None:
            self._fd.__exit__(typ, val, traceback)

    def start(self):
        if self._running:
            raise ValueError()
        self._running = True
        self._worker.start()

    def run(self):
        if self._fd is None or self.socket is None:
            raise ValueError("Use context manager before running")
        while self._running:
            d = self._fd.readline()
            self.socket.send_pyobj({"data": d})

    def stop(self):
        self._running = False


if __name__ == "__main__":

    import sys

    if "-h" in sys.argv:
        print(__doc__)
        exit(0)

    if len(sys.argv) != 2:
        print(__doc__)
        exit(1)

    filename = sys.argv[1]

    with zmq.Context() as ctx, DataProvider(ctx, filename) as dp:
        dp.start()

        while True:
            print("pulse")
            time.sleep(1)
