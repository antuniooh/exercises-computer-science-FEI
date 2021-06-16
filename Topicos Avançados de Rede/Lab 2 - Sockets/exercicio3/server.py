import platform
from socket import *
from user_shelf import *
from time_assistant import *
from linux_concurrency import linuxConcurrentTCPConnection
from windows_concurrency import windowsConcurrentTCPConnection

OK = 0
ERR = 404

def platformSpecificConcurrency(tcp, concurrency):
    LOOP = True
    while LOOP:
        concurrency(tcp, runTimeAssistant)    
    
    return OK


def runServer():
    HOST = 'localhost'
    PORT = 12002
    address = (HOST, PORT)

    with socket(AF_INET, SOCK_STREAM) as tcp:
        tcp.bind(address)
        tcp.listen(1)
        
        currentPlatform = platform.system()

        print(f"[Current platform: {currentPlatform}]")
        print(f"[The server is ready to receive connections...]")

        print(getTimeAssistantBanner())

        if currentPlatform == 'Windows':
            platformSpecificConcurrency(tcp, windowsConcurrentTCPConnection)
        elif currentPlatform == 'Linux':
            platformSpecificConcurrency(tcp, linuxConcurrentTCPConnection)

    print("--End of program--")

if __name__ == '__main__':
    runServer()