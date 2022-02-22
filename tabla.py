from jugador import Jugador
from time import sleep
import sys

puerto = sys.argv[1]

nombre = sys.argv[2]

j1 = Jugador(puerto, nombre)
j1.sendPlayer('localhost', '5555')
j1.waitMyTurn()
j1.waitMyTurn()