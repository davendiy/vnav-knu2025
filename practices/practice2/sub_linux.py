import time
import zmq
import threading


class DataPrinter:

    sock_name = "ipc://@data.socket"

    def __init__(self, ctx):
        self.ctx = ctx
        self.socket = None
        self._running = False
        self._worker = threading.Thread(target=self.run)

    def __enter__(self):
        self.socket = self.ctx.socket(zmq.PUB)
        self.socket.setsockopt(zmq.SUBSCRIBE, b'')
        self.socket.connect(self.sock_name)
        self.socket.__enter__()
        return self

    def __exit__(self, typ, val, traceback):
        if self.socket is not None:
            self.socket.__exit__(typ, val, traceback)

    def start(self):
        if self._running:
            raise ValueError()
        self._running = True
        self._worker.start()

    def run(self):
        if self.socket is None:
            raise ValueError("Use context manager before running")
        while self._running:
            data = self.socket.recv_pyobj()
            print(data)

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

    with zmq.Context() as ctx, DataPrinter(ctx) as dp:
        dp.start()

        while True:
            print("pulse")
            time.sleep(1)
