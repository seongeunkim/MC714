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

def node(port_number, message):
	self.port_number = port_number

	print (self.port_number)

	# only the first process has the message
	if self.port_number != starting_port:
		self.info = ""
	else:
		self.info = "what am i doing"

	# server socket
	server_context = zmq.Context()
	print "Running server on port: %d" % self.port_number
	server_p = "tcp://%s:%s" % (HOST, self.port_number)		# how and where to connect
	server_socket = context.socket(zmq.REP)					# create reply socket
	server_socket.bind(server_p)							# bind socket to address

	# client socket
	client_context = zmq.Context()
	client_socket = context.socket(zmq.REQ)

	while True:
		






