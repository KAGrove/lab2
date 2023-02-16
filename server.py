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
print("Broadcasting")


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

	message = f"{addr} joined the chat room"
	connection.send("Velkommen til denne chat!".encode())
	broadcast(connection, message)


	### Your code ends here ###

	try:
		while True:
			message = connection.recv(1024).decode()
			print (now() + " " +  str(addr) + "#  ", message)
			if (message == "exit"):
				print("Klienten har exitet")
				break
			### Write your code here ###
			#broadcast this message to the others
			else:
				broadcast(connection, f'{addr}: {message}')
			### Your code ends here ###
	except:
		all_client_connections.remove(connection)
		connection.close()

def broadcast(connection, message):
	### Write your code here ###
	for c in all_client_connections:
		if c != connection:
			try:
				c.send(message.encode())
			except:
				print("Error")
				c.close()
				all_client_connections.remove(c)
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
		serverSocket.bind(('', serverPort))
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
