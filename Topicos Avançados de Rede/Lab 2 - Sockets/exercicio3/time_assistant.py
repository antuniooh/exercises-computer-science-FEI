from datetime import datetime
from user_shelf import *


def getTimeAssistantBanner():
    return '''
########################################################
#                                                      #
#              J.A.W. operating successfuly            #
#                                                      #
########################################################
'''


def getProperTimeResponse(request):
    now = datetime.now()
    hour = now.hour
    
    print(f"Current hour: {hour}")

    morning = hour in range(6,11)
    afternoon = hour in range(12,18)
    night = hour in range(19,23) or hour in range(1,5)

    answer = "Actually, it's "
    
    if morning and request.lower() != 'good morning':
        answer += "good morning"
    elif afternoon and request.lower() != 'good afternoon':
        answer += "good afternoon"
    elif night and request.lower() != 'good night':
        answer += "good night"
    else:
        answer = request

    return answer


def runTimeAssistant(connectionSocket, clientAddress, shelfName):
    print(50*'-')
    print(f"Client {clientAddress[0]} conected in port {clientAddress[1]}")

    if not checkUser(str(clientAddress[0]), shelfName):
        message = "How can I call you?".encode()
        connectionSocket.send(message)
        print(f"Message sent to ({clientAddress[0]}, {clientAddress[1]})")

        userName = connectionSocket.recv(1024).decode()
        print(f"Message received from ({clientAddress[0]}, {clientAddress[1]})")
        
        createNewUser(str(clientAddress[0]), userName, shelfName)
    
    userName = getUserName(clientAddress[0], shelfName)
    message = f"Welcome, {userName}!".encode()
    connectionSocket.send(message)
    print(f"Message sent to ({clientAddress[0]}, {clientAddress[1]})")

    breakLoop = False

    while True:
        request = connectionSocket.recv(1024).decode()
        print(f"Message received from ({clientAddress[0]}, {clientAddress[1]})")
        answer = ''

        if (request.upper() == "COMMANDS"):
            answer = "\n>TIME\n>Good Morning\n>Good Afternoon\n>Good Night\n>EXIT"
            answer = answer.encode()

        elif request.upper() == "TIME":
            hour = datetime.now().strftime('%H:%M:%S')
            answer = f'It´s {hour}'.encode()

        elif request.lower() in ["good morning", "good afternoon", "good night"]:
            answer = getProperTimeResponse(request)
            answer = answer.encode()

        elif request.upper() == "EXIT":
            answer = 'Goodbye!'.encode()
            breakLoop = True

        else:
            print("Invalid command")
            answer = "I can't understand this command yet :(".encode()

        connectionSocket.send(answer)
        print(f"Message sent to ({clientAddress[0]}, {clientAddress[1]})")

        if breakLoop:
            print(f'Closing connection with user ({clientAddress[0]}, {clientAddress[1]})')
            print(50*'-')
            break

    return




