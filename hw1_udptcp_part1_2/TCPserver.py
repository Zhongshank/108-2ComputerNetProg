import socket

HOST, PORT = '127.0.0.1', 7777

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))

#new
s.listen(0)
conn, addr = s.accept()

#message_client, address = s.recvfrom(1024)
data = conn.recv(1024)
print(data + " from " + str(addr))

# s.sendall(b'Nice to meet all')
conn.sendto(b'Nice to meet you', addr)
s.close()