import socket
from math import sqrt
serverHost = 'localhost'
serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))

print("Servidor pronto! ")

while True:
	op, clientAddress = serverSocket.recvfrom(2048)
	stre=op.decode('utf-8')
	vt=stre.split()
#	soma1=int(vt[1])+int(vt[2])
#	print (soma1)
#	soma=0
	if	vt[0]=='soma':
		soma=0
		soma=int(vt[1])+int(vt[2])
		somae=str(soma).encode('utf-8')
		serverSocket.sendto(somae, clientAddress)
	elif vt[0]=='raiz':
		raiz=sqrt(int(vt[1]))
		raize=str(raiz).encode('utf-8')
		serverSocket.sendto(raize, clientAddress)
