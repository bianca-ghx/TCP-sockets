# Client - server communication for files transfer using TCP sockets in C/C++ and Python

## Introduction
This project demonstrates the implementation of a client-server communication system for file transfer using TCP sockets. The project includes both C/C++ and Python versions of the client and server programs. The goal is to facilitate file transfer between a client and server over a network using TCP sockets.

## Installation
To install and run this project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/bianca-ghx/TCP-sockets.git
    ```
2. Navigate to the project directory:
    ```sh
    cd TCP-sockets
    ```
3. Ensure you have a C/C++ compiler and Python installed on your system.

## Usage
To use the client-server file transfer system, follow these instructions:

### Using C/C++:
1. Compile the server program:
    ```sh
    gcc server.c -o server
    ```
2. Compile the client program:
    ```sh
    gcc client.c -o client
    ```
3. Run the server:
    ```sh
    ./server
    ```
4. Run the client in a separate terminal:
    ```sh
    ./client
    ```

### Using Python:
1. Run the server:
    ```sh
    python server.py
    ```
2. Run the client in a separate terminal:
    ```sh
    python client.py
    ```

## Workflow
1. The server listens for connections.
2. The client connects to the server and sends the name of a file it wants to download.
3. The server locates the file in its directory, opens it, and sends the content to the client.
4. The client writes the received file content to its current directory.

## Acknowledgements
This project was for the Communication Networks course at POLITEHNICA Bucharest National University of Science and Technology developed to demonstrate the use of TCP sockets for client-server communication in C/C++ and Python.
