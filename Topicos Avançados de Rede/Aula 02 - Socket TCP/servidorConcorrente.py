import socket
import os
import sys
HOST = ''              # Endereco IP do Servidor
PORT = 8085           # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#cria o socket TCP para escutar por novas conexões
orig = (HOST, PORT)
tcp.bind(orig)#atrela esse socket ao localhost na porta definida
tcp.listen(1)#coloca o socket para escutar

print("O sevidor está pronto para receber!")

while True:
    con, cliente = tcp.accept()#con é um novo socket criado quando tcp aceita alguém para se comunicar diretamente com esse cliente e cliente é o endereço IP do cliente
    pid = os.fork()#fork cria um processo filho
    if pid == 0:#os.fork deve retornar 0 para o processo filho e um numero de pip do filho para o processo pai
        tcp.close()#fecha o socket nesse processo filho
        print("Conectado por {} na porta {}".format(cliente[0], cliente[1]))
        #while True:
        msg = con.recv(2048)
        
        print(cliente, msg)
        frasemaiusc = msg.upper()
        con.send(frasemaiusc)
        print("Finalizando conexao do cliente", cliente)
        con.close()
        sys.exit(0)
    else:
        con.close()