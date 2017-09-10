import zmq
context = zmq.Context()

HOST = "127.0.0.1" 
PORT = "5000"
info = ""

php = "tcp://"+ HOST +":"+ PORT
s = context.socket(zmq.REQ)

s.connect(php)
s.send("help")
message = s.recv()
if not "thank you" in message:
	print("it knew it\n")
else:
	print("it didnt know it\n")
#print message
