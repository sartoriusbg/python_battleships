import socket

def start_server(host, port):
    print("starting")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #host = '127.0.0.1'  # localhost
    #port = 12345  # choose an available port

    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received data: {data}")

        response = "Hello, client! I received your message."
        client_socket.send(response.encode('utf-8'))

        client_socket.close()

start_server()
