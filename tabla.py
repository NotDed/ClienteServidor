from jugador import Jugador
from time import sleep
import sys
import os

puerto = sys.argv[1]

nombre = sys.argv[2]

j1 = Jugador(puerto, nombre)
j1.sendPlayer('localhost', '5555')


os.system('cls')
j1.getBroadcast()

end = False
while not end:
    end = j1.waitMyTurn()
    # j1.getBroadcast()