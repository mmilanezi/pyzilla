import socket

def send_file(file_path, dest_id):
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_socket.connect(('localhost', 12345))

    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Enviar o ID do destinatário e os dados do arquivo
    sender_socket.sendall(f"{dest_id:<8}".encode() + file_data)

    sender_socket.close()
