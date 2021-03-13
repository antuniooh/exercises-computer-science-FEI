from socket import *

#define a porta da aplicacao
serverPort=8081
#crio o socket para escutar pedidos dos 
serverSocket= socket(AF_INET, SOCK_STREAM)
#atrelo o socket TCP
serverSocket.bind(("", serverPort))
#para escutar pedidos
serverSocket.listen(1)
print("Servidor HTTP/1.1 inicializado")
#loop para escutar por conexoes
while True:
    #aceita uma conexao e cria um novo soket para atendela
    connectionSocket, addr = serverSocket.accept()
    print("Cliente {} conectado ao servidor".format(addr))
    #leio o que chega do cliente em connection Socket
    request = connectionSocket.recv(1024).decode()
    #espera receber um comando e um parametro (formato da msg)
    #netao divide a msg recebida
    split_request = request.split()
    #interpreta
    if split_request[0] == "GET":
        #realiza a ação
        #pega os parametros
        params = split_request[1]
        print("Solicitação dotipo GET, buscando orecurso {}".format(params))
        #supondo q foi um secesso
        response = ("200 OK").encode()
        connectionSocket.send(response)
    else:
        #nao recebeuo get responde com erro
        print("Somando nao pode ser interpetado")
        response = ("Deu muit ruim").encode()
        connectionSocket.send(response)
    connectionSocket.close()