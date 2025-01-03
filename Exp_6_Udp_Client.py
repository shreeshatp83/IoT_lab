import socket
msgFromClient = "Hello UDP Server"
bufferSize = 1024
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1",20001)
UDPClientSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)