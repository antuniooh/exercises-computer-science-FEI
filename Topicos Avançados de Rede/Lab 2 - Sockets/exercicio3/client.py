from socket import *
import time


HOST = input("Digite o IP do servidor (deixe em branco caso seja localhost): ")

if HOST == "":
    HOST = "localhost"

PORT = 12002

serverAddress = (HOST, PORT)
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(serverAddress)

while True:
    request = clientSocket.recv(1024)

    if request.decode():
        print("Message received: ")
        print(f'>>>>>>>>>>>>>>>> {request.decode()}')

        if request.decode() == 'Goodbye!':
            break

        response = input()
        clientSocket.send(response.encode())
        print("Message sent")

clientSocket.close()