from socket import *

serverName = "localhost"

serverPort = 12000

clienteSocket = socket(AF_INET, SOCK_STREAM)  # Socket TCP

clienteSocket.connect((serverName, serverPort))

while True:
    message = clienteSocket.recv(1024)

    if message.decode():
        print("Message received: ")
        print(f'>>>>>>>>>>>>>>>> {message.decode()}')

        if message.decode() == 'Goodbye!':
            break

        answer = input()
        clienteSocket.send(answer.encode())
        print("Message sent")

    


clienteSocket.close()
