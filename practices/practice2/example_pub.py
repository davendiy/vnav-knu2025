
import zmq
import time

PORT = 5556


ctx = zmq.Context()

socket = ctx.socket(zmq.PUB)
socket.bind(f"tcp://*:{PORT}")

i = 0

while True:
    print(f"[-->] Sending {i}...")
    socket.send_pyobj({"param": "counter", "val": i})
    i += 1
    time.sleep(1)
