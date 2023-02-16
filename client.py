#Client side connects to the server and sends a message to everyone

import socket
import select
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# write server ip and port, and connect
### write your code here ###
client_socket.connect(('127.0.0.1', 12000))
### your code ends here ###

while True:

    """ we are going to use a select-based approach here because it will help
    us deal with two inputs (user's input (stdin) and server's messages from socket)
    """
    inputs = [sys.stdin, client_socket]

    """ read the select documentations - You pass select three lists: the
    first contains all sockets that you might want to try reading; the
    second all the sockets you might want to try writing to, and the last
    (normally left empty) those that you want to check for errors. """

    read_sockets,write_socket, error_socket = select.select(inputs,[],[])

    # we check if the message is either coming from your terminal or
    # from a server
    for socks in read_sockets:
        if socks == client_socket:

            # receive message from client and display it on the server side
            # also handle exceptions here if there is no message from the
            # client, you should exit.

            ### write your code here ###
            try:
                print("Velkommen til chat!")
                message = client_socket.recv(1024).decode()
                if not message:
                    print("Mistet forbindelse")
                    break
                print("Mottatt fra server: ", message)
            except socket.error as e:
                print("Error receiving data from server")
                break
            ### your code ends here ###

        else:
            #takes inputs from the user
            message = sys.stdin.readline()

            #send a message to the server

            ### write your code here ###
            client_socket.send(message.encode())
            ### your code ends here ###


client_socket.close()
