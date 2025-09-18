
import time
import zmq


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    print("[<--] waiting for client")
    message = socket.recv_pyobj()
    print("[*] Got:", message)

    time.sleep(1)
    print("[-->] sending answer")
    socket.send_pyobj({"val": "answer"})
