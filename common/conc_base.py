import threading
import zmq

from abc import ABC, abstractmethod


# from Python cookbook
class DaemonBase(ABC):

    def __init__(self):
        self._running = False
        self._worker = threading.Thread(target=self.run)

    def start(self):
        if self._running:
            raise ValueError(f"Task {self} is already running!")
        self._running = True
        self._worker.start()

    @abstractmethod
    def run(self):
        """This method will be running inside another thread."""

        # we can use it since memory is shared across all the threads
        while self._running:
            pass

    def stop(self):
        # it's not particularly safe, but we can assume that nobody will use this
        # variable except functions `start` or `stop`
        self._running = False


class SubBase(DaemonBase):
    """Base class for Subscribers using ZMQ.

    Made as possible daemon. Can be also used in blocking mode.
    """

    sock_name: str = ...  # type: ignore
    unique = False

    def __init__(self, ctx, topic=b""):
        super().__init__()
        self.ctx = ctx
        self._topic = topic
        self._socket: zmq.Socket = None  # type: ignore

    def __enter__(self):
        self._socket = self.ctx.socket(zmq.SUB)
        self._socket.setsockopt(zmq.SUBSCRIBE, self._topic)

        if self.unique:
            self._socket.bind(self.sock_name)
        else:
            self._socket.connect(self.sock_name)

        self._socket.__enter__()

        self._prepare_enter()
        return self

    @abstractmethod
    def _prepare_enter(self):
        pass

    def __exit__(self, typ, val, traceback):
        self.stop()
        self._prepare_exit(typ, val, traceback)

        if self._socket is not None:
            self._socket.__exit__(typ, val, traceback)

    @abstractmethod
    def _prepare_exit(self, typ, val, traceback):
        pass


class PubBase(DaemonBase):

    sock_name: str = ...  # type: ignore
    unique = True

    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self._socket: zmq.Socket = None  # type: ignore

    def __enter__(self):
        self._socket = self.ctx.socket(zmq.PUB)

        if self.unique:
            self._socket.bind(self.sock_name)
        else:
            self._socket.connect(self.sock_name)

        self._socket.__enter__()

        self._prepare_enter()
        return self

    @abstractmethod
    def _prepare_enter(self):
        pass

    def __exit__(self, typ, val, traceback):
        self.stop()
        self._prepare_exit(typ, val, traceback)

        if self._socket is not None:
            self._socket.__exit__(typ, val, traceback)

    @abstractmethod
    def _prepare_exit(self, typ, val, traceback):
        pass
