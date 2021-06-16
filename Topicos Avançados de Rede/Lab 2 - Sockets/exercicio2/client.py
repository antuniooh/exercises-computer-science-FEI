from socket import *
serverName = "localhost"
serverPort = 12000
clienteSocket = socket(AF_INET, SOCK_STREAM)  # Socket TCP
clienteSocket.connect((serverName, serverPort))

while True:
    message = clienteSocket.recv(1024).decode()
    print("RECEIVE MSG >>>> ")

    if message.find("Please insert two numbers!") != -1:
        print(message)
        firstValue = input("Insert the first value: ")
        secondValue = input("Insert the second value: ")
        clienteSocket.send( (str(firstValue) + " " + str(secondValue)).encode() )
    elif message.find("insert the operation") != -1:
        print(message)
        operation = str(input("Available operations \n 1 - Plus\n 2 - Minus\n 3 - Divide\n 4 - Multiplication\nInsert the number of operation > "))
        clienteSocket.send(operation.encode())
    elif message.find("the result") != -1:
        print(message)
        break
    else:
        print(message)
        break
clienteSocket.close()