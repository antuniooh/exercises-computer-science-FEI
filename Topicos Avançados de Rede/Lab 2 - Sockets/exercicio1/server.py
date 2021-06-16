from socket import *
import shelve
from datetime import datetime

def checkUser(ip):
    s = shelve.open('users.db')
    userStored = False

    if ip in s:
        userStored = True
    else:
        userStored = False

    s.close()
    return userStored    

def newUser(ip, name):
    s = shelve.open('users.db')
    s[ip] = name
    s.close()

def getUserName(ip):
    s = shelve.open('users.db')
    name = s[ip]
    s.close()
    return name

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM) # Socket TCP

serverSocket.bind(("localhost", serverPort))

serverSocket.listen(1)

print('''
########################################################
#                                                      #
#              J.A.W. operating successfuly            #
#                                                      #
########################################################
''')

while True:
    connectionSocket, addr = serverSocket.accept()

    print(50*'-')
    print(f"Client {addr[0]} conected in door {addr[1]}")

     
    if not checkUser(str(addr[0])):
        message = "How can I call you?".encode()
        connectionSocket.send(message)
        print("Message sent")

        answer = connectionSocket.recv(1024).decode()
        print("Message received")
        
        newUser(str(addr[0]), answer)

    userName = getUserName(addr[0])
    message = f"Welcome, {userName}!".encode()
    connectionSocket.send(message)
    print("Message sent")

    while True:    
        request = connectionSocket.recv(1024).decode()
        print("Message received")


        if request.upper() == "COMMANDS":
            answer = "\n>TIME\n>Good Morning\n>Good Afternoon\n>Good Night\n>EXIT"
            answer = answer.encode()
            connectionSocket.send(answer)
            print("Message sent")

        elif request.upper() == "TIME":
            hour = datetime.now().strftime('%H:%M:%S')
            answer = f'It´s {hour}'.encode()
            connectionSocket.send(answer)
            print("Message sent")

        elif request.lower() in ["good morning", "good afternoon", "good night"]:
            now = datetime.now()
            now = now.hour
            print(f"Current hour {now}")
            morning = now in range(6,11)
            afternoon = now in range(12,18)
            night = now in range(19,23) or now in range(1,5)

            answer = "Actually, it's "
            
            if morning and request.lower() != 'good morning':
                answer += "good morning"
            elif afternoon and request.lower() != 'good afternoon':
                answer += "good afternoon"
            elif night and request.lower() != 'good night':
                answer += "good night"
            else:
                answer = request
            
            answer = answer.encode()
            connectionSocket.send(answer)
            print("Message sent")


        elif request.upper() == "EXIT":
            answer = 'Goodbye!'.encode()
            connectionSocket.send(answer)
            print("Message sent")
            print('Closing connection with this user')
            print(50*'-')
            break

        else:
            print("Invalid command")
            answer = "I can't understand this command yet :(".encode()
            connectionSocket.send(answer)
            print("Message sent")

    connectionSocket.close()




