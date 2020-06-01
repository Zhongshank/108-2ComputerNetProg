import socket

HOST, PORT = '127.0.0.1', 7777
# HOST,PORT ='140.112.42.100', 7777
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

message_client = b'hello world'
addr = (HOST, PORT)

# new
s.connect(addr)
s.sendall(message_client)
# s.sendto(message_client, addr)

#message_server = s.recv(1024).decode()
message_server = s.recv(1024)
print(message_server)
s.close()


# s.connect((HOST, PORT))
#    s.sendall(b'Hello, world')
#    data = s.recv(1024)

# Response = input(s.recv(1000).decode('utf-8')).encode('utf-8') 
# s.send(response)