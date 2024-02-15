import socket

def start_client(host = '127.0.0.1', port = 12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = '127.0.0.1'  # localhost
    #port = 12345  # the same port as the server

    client_socket.connect((host, port))

    message = "Hello, server! How are you?"
    client_socket.send(message.encode('utf-8'))

    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received response from server: {data}")

    client_socket.close()

start_client()
