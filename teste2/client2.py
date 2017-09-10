import zmq
context = zmq.Context()

HOST = "127.0.0.1"
PORT = "5555"

php = "tcp://"+ HOST +":"+ PORT
s = context.socket(zmq.REQ)

s.connect(php)
s.send("Hello World")
message = s.recv()
s.send("STOP")
print message
