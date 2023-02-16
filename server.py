"""
Server side: it simultaneously handle multiple clients
and broadcast when a client new client joins or a client
sends a message.
"""
from socket import *
import _thread as thread
import time
import sys


#this is too keep all the newly joined connections!
all_client_connections = []

def now():
	"""
	returns the time of day
	"""
	return time.ctime(time.time())

def handleClient(connection, addr):
	"""
	a client handler function 
	"""

	#this is where we broadcast everyone that a new client has joined

	### Write your code here ###
	# append this this to the list for broadcast
	all_client_connections.append(connection)
	# create a message to inform all other clients
	# that a new client has just joined.


	### Your code ends here ###


	while True:
		try:
			message = connection.recv(1024).decode('cp865')
			print (now() + " " +  str(addr) + "#  ", message)
			if (message == "exit" or not message):
				break
			### Write your code here ###
			#broadcast this message to the others
			broadcast(connection, f'{addr} joined the chat!'.encode('cp865'))
			### Your code ends here ###
		except:
			connection.close()
			all_client_connections.remove(connection)

def broadcast(connection, message):
	print("Broadcasting")
	### Write your code here ###
	for connection in all_client_connections:
		connection.send(message)
	### Your code ends here ###

def main():
	"""
	creates a server socket, listens for new connections,
	and spawns a new thread whenever a new connection join
	"""
	serverPort = 12000
	serverSocket = socket(AF_INET,SOCK_STREAM)
	try:
		# Use the bind function wisely!
		### Write your code here ###
		serverSocket.bind(('127.0.0.1', serverPort))
		### Your code ends here ###

	except:
		print("Bind failed. Error : ")
		sys.exit()
	serverSocket.listen(10)
	print('The server is ready to receive')
	while True:
		### Write your code here ###
		connectionSocket, addr = serverSocket.accept()  # accept a connection
		print('Server connected by ', addr)
		print('at ', now())
		thread.start_new_thread(handleClient, (connectionSocket, addr))
	### You code ends here ###
	serverSocket.close()

if __name__ == '__main__':
	main()
