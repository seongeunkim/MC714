import zmq
import random
from multiprocessing import Pool
from multiprocessing import Process
import threading
from threading import Thread
import time

starting_port = 5000
HOST = "127.0.0.1"
num_processes = 8
libera_o_portao = 0



class NoDeFofoca():

	def __init__(self, port_number):

		self.port_number = port_number
		self.exit = 0
		
		print (self.port_number)

		# only the first process has the message
		if self.port_number != starting_port:
			self.info = ""
		else:
			self.info = "what am i doing"

		client_thread = threading.Thread(target=self.client)
		client_thread.start()
		self.server()
		client_thread.join()

	def server(self):
		
		context = zmq.Context()
		print "Running server on port: %d" % self.port_number
		p = "tcp://%s:%s" % (HOST, self.port_number)
		s = context.socket(zmq.REP)
		#zmq_setsocketopt(s, ZMQ_RCVTIMEO, 600)
		#s.RCVTIMEO = 1000
		s.bind(p)

		while self.exit == 0:
			try:
				#print ("before recv of server %d" % self.port_number)
				#message = s.recv(flags=zmq.NOBLOCK)
				message = s.recv()
				print ("after recv of server %d" % self.port_number)
				print ("%d RECEIVED a message!!!! Message = %s" % (self.port_number, message))
				if message != self.info:
					print ("%d RECEIVED a NEW message!" % (self.port_number))
					#print ("%d" % self.info)
					s.send("thank you")
					self.info = message
					#print "message: %s" % self.info
				else:
					print ("SERVER %d SENDING STOP MESSAGE" % self.port_number)
					s.send("stop")
					print ("$$$$$$$$$$$$$$$$$$")
					time.sleep(2)
			except zmq.Again as e:
				pass
		print ("%d saiu do while server porra " % self.port_number)


	def client(self):

		print ("Start of client ! id = %d" % self.port_number)
		context = zmq.Context()
		s1 = context.socket(zmq.REQ)
		#s1.RCVTIMEO = 10000

		time.sleep(1)
		while self.exit == 0:
			if self.info != "":
				# randomly picks a port
				port = list(range(starting_port, starting_port + num_processes))
				port.remove(self.port_number)
				port = random.choice(port)
				#port = 4444

				print "meu id %d e a porta %d" % (self.port_number, port)

				php = "tcp://%s:%s" % (HOST, port)
				

				s1.connect(php)
				print ("%d SENDING a message to %d!!!! Message = %s" % (self.port_number, port, self.info))
				s1.send(self.info)
				print "before recv of client"
				try:
					#message = s1.recv(flags=zmq.NOBLOCK)
					message = s1.recv()
					print ("Client of id %d received a message %s" % (self.port_number, message))
					if not "thank you" in message:
						print("it knew it\n")
						print("I am %d and I stopped" % self.port_number)
						self.exit = 1
						break
					else:
						print("it didnt know it\n")

				except zmq.Again as e:
					pass

				#print("I know nothing and I am %d" % self.port_number)

		print ("%d saiu do while client porra " % self.port_number)
		
	
	#def client():


def apply_async_with_callback():
	exit = 0
	processes= []
	#pool = Pool()
	for i in range(num_processes):
		p = Process(target = NoDeFofoca, args = (i + starting_port, ))
		processes.append(p)
		processes[i].start()

		#try:
		#pool.apply_async(NoDeFofoca, args = (i + starting_port, ))
		#except:
			#print "error in creating process"
		#print("I wanna die and my number is %d" % i)
		#time.sleep(1)
	#global libera_o_portao
	#libera_o_portao = 1
	for i in range(num_processes):
		
		processes[i].join()
	#p.close()
	print "what"
	#p.join()
	print "the end"

if __name__ == '__main__':
	apply_async_with_callback()
