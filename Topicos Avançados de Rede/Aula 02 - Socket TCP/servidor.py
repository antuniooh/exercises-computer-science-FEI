from socket import *

#define a porta da aplicacao
serverPort=12000
#crio o socket para escutar pedidos dos 
serverSocket= socket(AF_INET, SOCK_STREAM)
#atrelo o socket TCP
serverSocket.bind(("", serverPort))
#para escutar pedidos
serverSocket.listen(1)
print("Serbidor pronto para receber")
#loop para escutar por conexoes
while True:
    #aceita uma conexao e cria um novo soket para atendela
    connectionSocket, addr = serverSocket.accept()
    #leio o que chega do cliente em connection Socket
    sentence = connectionSocket.recv(1024)
    #convert oem maisucula
    capitalizeSentence = sentence.upper()
    #envio de volta
    connectionSocket.send(capitalizeSentence)
    #fecha o socket
    connectionSocket.close()
