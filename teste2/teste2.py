import zmq
import random
from multiprocessing import Array, Manager, Value
from multiprocessing import Process
import threading
from threading import Thread
import time
from ctypes import Structure, c_int

starting_port = 5000
HOST = "127.0.0.1"
num_processes = 10
libera_o_portao = 0
k = 8

# creates a struct with the values
class Values(Structure):

	_fields_ = [('port_number', c_int), ('hasinfo', c_int), ('attempts', c_int), ('successes', c_int)]


class NoDeFofoca():

	def __init__(self, port_number, value_array, gossip_starting_time):

		self.port_number = port_number

		self.exit = 0


		self.hasinfo = 0
		self.attempts = 0
		self.successes = 0


		# only the last process has the message
		if self.port_number != (starting_port + num_processes - 1):
			gossip_starting_time.value = time.time()
			self.info = ""
		else:
			#gossip_starting_time.value = time.time()
			self.info = "what am i doing"
			self.hasinfo = 1

		client_thread = threading.Thread(target=self.client)
		client_thread.start()
		self.server()
		client_thread.join()

		index = self.port_number - starting_port
		value_array[index].port_number = self.port_number
		value_array[index].hasinfo = self.hasinfo
		value_array[index].attempts = self.attempts
		value_array[index].successes = self.successes



	def server(self):
		
		context = zmq.Context()
		#print "Running server on port: %d" % self.port_number
		p = "tcp://%s:%s" % (HOST, self.port_number)
		s = context.socket(zmq.REP)
		#zmq_setsocketopt(s, ZMQ_RCVTIMEO, 600)
		s.RCVTIMEO = 10000
		s.bind(p)

		while (time.time()-gossip_starting_time.value < 40):

		#while (time.time()-gossip_starting_time.value < 12):
			try:
				#print ("before recv of server %d" % self.port_number)
				#message = s.recv(flags=zmq.NOBLOCK)
				message = s.recv()
				#print ("after recv of server %d" % self.port_number)
				#print ("%d RECEIVED a message!!!! Message = %s" % (self.port_number, message))
				if message != self.info:
					print ("%d RECEIVED a NEW message!" % (self.port_number))
					self.hasinfo = 1
					s.send("thank you")
					self.info = message
				else:
					#print ("SERVER %d SENDING STOP MESSAGE" % self.port_number)
					s.send("stop")
					#print ("$$$$$$$$$$$$$$$$$$")
					#time.sleep(1)
			except zmq.Again as e:
				pass
		#print ("%d saiu do while server porra " % self.port_number)


	def client(self):

		#print ("Start of client ! id = %d" % self.port_number)
		context = zmq.Context()
		context.setsockopt(zmq.LINGER, 100)
		
		client_timer = time.time()
		s1 = context.socket(zmq.REQ)
		while (self.exit == 0 and time.time()-gossip_starting_time.value < 40):
		#while (time.time()-gossip_starting_time.value < 12):
			if self.info != "":
				s1 = context.socket(zmq.REQ)
				#s1.RCVTIMEO = 10000
				#s1.SNDTIMEO = 10000

				# randomly picks a port
				port = list(range(starting_port, starting_port + num_processes))
				port.remove(self.port_number)
				port = random.choice(port)

				self.attempts += 1
				#print "meu id %d e a porta %d" % (self.port_number, port)

				php = "tcp://%s:%s" % (HOST, port)
				t = time.time()-client_timer
				s1.connect(php)
				#print ("%d SENDING a message to %s!!!!" % (self.port_number, php))
				try:
					s1.send(self.info, zmq.NOBLOCK)
					#message = s1.recv(flags=zmq.NOBLOCK)
					message = s1.recv()
					#print ("Client of id %d received a message %s" % (self.port_number, message))
					if not "thank you" in message:
						# stops with a probability of 1 of k
						prob = random.randrange(1,k+1)
						if(prob == 1):
							print("%f: I am %d and I stopped" % (time.time()-gossip_starting_time.value, self.port_number))
							self.exit = 1
							break
						else:
							#print("I am %d and im not dying bitch" % self.port_number)
							pass
						
					else:
						self.successes += 1
						#print("it didnt know it\n")
				except:
					#print("time %f: %d MESSAGE TO %d FAILED!!!!!!" % (t, self.port_number, port))
					pass

				time.sleep(2)

				#print("I know nothing and I am %d" % self.port_number)

		#print ("%d saiu do while client porra " % self.port_number)
		#print (":::::::%d:::::::\n  tem info: %d\n  attempts: %d\n  successes: %d" % (self.port_number, self.hasinfo, self.attempts, self.successes))
		s1.close()
		context.term()
		#exit()


# get lowest number of attempts
def get_lowest(value_array):

	min_value = value_array[0].attempts

	for a in value_array:
		if min_value > a.attempts:
			min_value = a.attempts

	return min_value

# get highest number of attempts
def get_highest(value_array):

	max_value = value_array[0].attempts

	for a in value_array:
		if max_value < a.attempts:
			max_value = a.attempts

	return max_value

# get the mean number of attempts
def get_mean(value_array):

	sum = 0

	for a in value_array:
		sum += a.attempts

	return float(sum)/num_processes

def calculate_success(value_array):

	succ_sum = 0
	attpts_sum = 0

	for a in value_array:
		succ_sum += a.successes
		attpts_sum += a.attempts

	return float(succ_sum)/attpts_sum

def total_nodes_with_info(value_array):

	total = 0

	for a in value_array:
		total += a.hasinfo

	return total



if __name__ == '__main__':
	exit = 0
	processes= []
	#pool = Pool()
	value_array = Array(Values, num_processes, lock = True)

	manager = Manager()
	gossip_starting_time = manager.Value('d', time.time()+100)

	#initial_time = time.time()

	for i in range(num_processes):
		p = Process(target = NoDeFofoca, args = (i + starting_port, value_array, gossip_starting_time))
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

	final_time = time.time()

	# number of attempts
	print ("lowest number of attempts: %d" % get_lowest(value_array))
	print ("highest number of attempts: %d" % get_highest(value_array))
	print ("mean: %.3f" % get_mean(value_array))

	# success rate
	print ("success rate: %.2f" % calculate_success(value_array))

	# total number of nodes with info
	print ("%d of %d have the info" % (total_nodes_with_info(value_array), num_processes))

	print ("total time: %ds" % (final_time-gossip_starting_time.value))


	print "what"
	#p.join()
	print "the end"
