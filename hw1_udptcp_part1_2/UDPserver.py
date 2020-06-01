import socket

HOST, PORT = '127.0.0.1', 7777

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

message_client, address = s.recvfrom(1024)
print(message_client + " from " + str(address))


s.sendto(b'Nice to meet you', address)
s.close()