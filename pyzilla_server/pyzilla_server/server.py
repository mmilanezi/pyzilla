import socket

HOST = 'localhost'
PORT = 8010
# tcp = socket.SOCK_STREAM
sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket 

sct.bind((HOST, PORT))

sct.listen()

conn, ender = sct.accept() # conexão e endereço da conexão aceita


