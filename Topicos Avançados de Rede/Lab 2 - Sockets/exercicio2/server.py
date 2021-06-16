from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) # Socket TCP
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)

firstNumber = 0
secondNumber = 0

def createResult(firstNumber, request, secondNumber):
    message = ""
    if request == "1":
        message = ("Ok, you want to make the operation %d + %d \nSo, that's the result %d\n" %( firstNumber, secondNumber, (firstNumber + secondNumber)))
    elif request == "2":
        message = ("Ok, you want to make the operation %d - %d \nSo, that's the result %d\n" %( firstNumber, secondNumber, (firstNumber - secondNumber)))
    elif request == "3":
        message = ("Ok, you want to make the operation %d / %d \n So, that's the result %d\n" %( firstNumber, secondNumber, (firstNumber / secondNumber)))
    elif request == "4":
        message = ("Ok, you want to make the operation with %d * %d \nSo, that's the result %d\n" %( firstNumber, secondNumber, (firstNumber * secondNumber)))
    else:
        message = ("Ok, you want to make the operation with %d <i have no idea what operation is that> %d \nSo, that's the result %d\n" %(firstNumber, secondNumber, 0 ))
    return message.encode()

while True:
    connectionSocket, addr = serverSocket.accept()
    print(50*'-')
    print("Cliente {} conectado ao servidor".format(addr))

    connectionSocket.send( ("Hey man, How are you? \nI'm here to solve math questions. \nPlease insert two numbers!\n").encode() )

    while True:
        request = connectionSocket.recv(1024).decode()
        print("RECEIVE MSG >>>> " + request)

        if not request: 
            break
        else:
            if len(request) >= 3:
                numbers = request.split(' ')
                try:
                    firstNumber = (float(numbers[0]))
                    secondNumber = (float(numbers[1]))
                except:
                    print("invalid operation...")
                    connectionSocket.send(("Ok, you want to make some operation with invalid numbers...\nVery funny man" ).encode())
                    break
                else:
                    message = ("Ok, you want to make some operation with %d and %d \n Now, insert the operation\n" %( firstNumber, secondNumber))
                    connectionSocket.send(message.encode())
                
            elif len(request) == 1:
                connectionSocket.send(createResult(firstNumber, request, secondNumber))
                break
    print("close connection...")
    connectionSocket.close()



