
import zmq

PORT = 5556


ctx = zmq.Context()
socket = ctx.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b'')
socket.connect(f"tcp://localhost:{PORT}")

while True:
    print("[<--] Waiting for server..")
    val = socket.recv_pyobj()
    print("[*] Got:", val)
