import socket
serverName = 'localhost'
serverPort = 12000
while True:
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	message = input("Entre com a sting minuscula: ")		
	if message=='quit':
		break
	byte_msg = message.encode('utf-8')
	clientSocket.sendto(byte_msg, (serverName, serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print(modifiedMessage.decode('utf-8'))
clientSocket.close()
