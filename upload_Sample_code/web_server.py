#####################################
###Do not copy and paste directly.###
#####################################

#import socket module
from socket import *
import time
import sys #In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
HOST, PORT = '127.0.0.1',80
serverSocket.bind((HOST,PORT))

while True:
    #Establish the connection
    print('Ready to serve...')
    serverSocket.listen(10)
    try:
        #Receive http request from the clinet
        conSocket,address=serverSocket.accept()
        message=conSocket.recv(1024).decode()
        if(len(message.split())<=1): #error handling
            break
        print("request:")
        print(message)
        filename = message.split()[1]
        if(filename=="/"):
            filename="/index.html"
        f = open(filename[1:])
        #Read data from the file that the client requested
        data=f.readlines()
        #Send response
        response=""
        response+="HTTP/1.0 200 OK\n"
        response+="Content-Type: text/html\r\n\r\n"
        for i in range(0, len(data)):
            response+=data[i]
        print("send response:")
        print(response)
        conSocket.sendall(response.encode())
    except IOError:
        #Send response message for file not found
        print(filename," Not Found!")
        conSocket.sendall("HTTP/1.0 404 Not Found!\r\n".encode())
    conSocket.close()
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
