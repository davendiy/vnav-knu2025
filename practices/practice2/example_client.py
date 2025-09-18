
import zmq


context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for req in range(10):
    print(f"[-->] sending {req}...")
    socket.send_pyobj({"num": req, "message": "Hello world!"})

    message = socket.recv_pyobj()
    print("[*] got:", message)
