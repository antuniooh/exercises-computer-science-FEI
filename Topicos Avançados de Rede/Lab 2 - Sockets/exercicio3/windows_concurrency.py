from multiprocessing import Process

def windowsConcurrentTCPConnection(tcp, task):
    connectionSocket, clientAddress = tcp.accept()
    process = Process(
        target=task,
        args=(
            connectionSocket,  #connectionSocket
            clientAddress,  #clientAddress
            'users.db',
        ),
    )
    process.start()
    connectionSocket.close()

    