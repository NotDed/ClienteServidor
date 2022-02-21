import socket

def getMyIp():
    return socket.gethostbyname(socket.gethostname())