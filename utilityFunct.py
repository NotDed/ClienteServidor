from socket import gethostbyname, gethostname
from random import randint

def getMyIp():
    return gethostbyname(gethostname())

def rollTheDice(diceSize = 5):
    return randint(1,diceSize)