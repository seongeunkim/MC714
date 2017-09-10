import zmq


print ("comeco do codigo: ")
context = zmq.Context()

HOST = "127.0.0.1"
PORT1 = "5000"
PORT2 = "5555"
info = "something"

p1 = "tcp://"+ HOST +":"+ PORT1 # how and where to connect
p2 = "tcp://"+ HOST +":"+ PORT2 # how and where to connect
s  = context.socket(zmq.REP)
# create reply socket

s.bind(p1)
s.bind(p2)
while True:
	message = s.recv()
	if not info in message:
		s.send("thank you")
		info = message
		print (info)
	else:
		s.send("stop")
		break
