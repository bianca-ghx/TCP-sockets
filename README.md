# Client - server communication for files transfer using TCP sockets in C/C++ and Python

The workflow of the program is as follows:
- The server will listen for connections.
- The client will connect to the server and will send the name of a file it wants to download. 
- The file will be located in the same folder with the server.
- The server will open the file and will send the content to the client.
- The client will write the file in its current directory.