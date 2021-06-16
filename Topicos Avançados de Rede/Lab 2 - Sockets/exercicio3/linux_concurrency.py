import os
import sys

def linuxConcurrentTCPConnection(tcp, task):
    connectionSocket, clientAddress = tcp.accept()

    processID = os.fork()

    # os.fork() creates another process based on the current one and resumes from the point it was created. The original process is called parent process and receives a value higher than 0. The new process is called child process and receives a value of 0.
    if processID == 0: # if we're in the child process
        tcp.close()
        task(
            connectionSocket,  #connectionSocket
            clientAddress,  #clientAddress
            'users.db',
        )
        connectionSocket.close()
        sys.exit(0)
        
    else: #if we're in the parent process
        connectionSocket.close()
    