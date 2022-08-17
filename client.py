import socket                                   # Import socket module

ClientMultiSocket = socket.socket()             # Create a socket object
host = socket.gethostname()                     # Get local machine name
port = 60000                                    # Reserve a port for your service.

print('Waiting for connection response')
try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
    quit()

filename = input("Enter the name of the file you want to download: ")
ClientMultiSocket.send(bytes(filename, 'utf-8'))

new_filename = input("How do you want to save the received file as? ")
with open(f'{new_filename}', 'wb') as f:
    data = ClientMultiSocket.recv(1024)
    # write data to a file
    f.write(data)

f.close()
print('Successfully got the file')
ClientMultiSocket.close()
print('Connection closed')