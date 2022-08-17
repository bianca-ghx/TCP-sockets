import socket                                 # Import socket module
import os
from _thread import *

ServerSideSocket = socket.socket()             # Create a socket object
port = 60000                                   # Reserve a port for your service.
host = socket.gethostname()                    # Get local machine name
ThreadCount = 0

try:
    ServerSideSocket.bind((host, port))        # Bind to the port
except socket.error as e:
    print(str(e))

ServerSideSocket.listen(5)                     # Now wait for client connection.
print('Server listening....')

def multi_threaded_client(connection):
    filename = connection.recv(1024)
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        connection.send(l)
        l = f.read(1024)
    f.close()

    print('Done sending')
    print('Thank you for connecting')
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()