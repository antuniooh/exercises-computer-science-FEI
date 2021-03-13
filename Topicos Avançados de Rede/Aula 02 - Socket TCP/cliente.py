from socket import *

#definir como localhost o endereço de IP do scoket do servudor
serverName = ""
#define a porta com a qual vai se comunicar com o servidor
serverPort=12000
#crio o socket
clientSocket= socket(AF_INET, SOCK_STREAM)
#tento estabelcer uma conexão TCP
clientSocket.connect((serverName,serverPort))
#dados a serem viados ao servidor
sentence = input("Sigite algo em letra minuscula")
#codificar a msg
sen = sentence.encode()
#envio a msg para o serviro
clientSocket.send(sen)
#le a resposta do servidor
modifiedSentence = clientSocket.recv(1024)
#imprimo a msg
print("Recebido: ", modifiedSentence.decode())
#fecha o socket
