import socket

HOST, PORT = '127.0.0.1', 7777

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message_client = b'hello world'

addr = (HOST, PORT)

s.sendto(message_client, addr)

message_server = s.recv(1024).decode()
print(message_server)
s.close()