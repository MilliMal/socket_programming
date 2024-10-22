import socket


def run_server():
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    port = 8000

    # bind the socket to a specific address and port
    server.bind((server_ip, port))
    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    # receive data from the client
    while True:
        request = client_socket.recv(1024)
        
        request = request.decode("utf-8") # convert bytes to string

        if 'close' in request.lower():
            response = "closed"
            # client_socket.send("closed".encode("utf-8"))
            client_socket.send(response.encode("utf-8"))
            break
        request = request.split()
        if len(request) != 2:
            response = "Please enter 2 number separated by a space"
            client_socket.send(response.encode("utf-8"))


# using a try/except just in case user did not give a string

        
        try:
            response = int(request[0]) + int(request[1])

        except ValueError:
            client_socket.send("Please enter numbers".encode("utf-8"))
  

        response = str(response).encode("utf-8") # convert string to bytes
        print(f"Sent back to client: {response.decode("utf-8") }")

        # convert and send accept response to the client
        client_socket.send(response)

    # close connection socket with the client
    client_socket.close()
    print("Connection to client closed")
    # close server socket
    server.close()


run_server()
