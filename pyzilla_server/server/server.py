import socket
import threading

class Server:
    def __init__(self, host, port):
        # tcp é socket.SOCK_STREAM 
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Servidor escutando em {host}:{port}")

    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        # Lógica para lidar com cada cliente individualmente
        file_data = client_socket.recv(1024)
        pass

# HOST = 'localhost'
# PORT = 8010
# sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket 

# sct.bind((HOST, PORT))

# sct.listen()

# conn, ender = sct.accept() # conexão e endereço da conexão aceita


