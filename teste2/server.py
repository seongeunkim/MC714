import zmq
context = zmq.Context(

p1 = "tcp://"+ HOST +":"+ PORT1 # how and where to connect
p2 = "tcp://"+ HOST +":"+ PORT2 # how and where to connect
s  = context.socket(zmq.REP)
# create reply socket

s.bind(p1)
s.bind(p2)

while True:
	message = s.recv()
	if not "STOP" in message:
		s.send(message + "*")
	else:
		break

