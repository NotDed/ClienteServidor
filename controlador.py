import zmq
import json
import os

from time import sleep

from Parchis.ficha import Ficha
from Parchis.tablero import Tablero

colores = ('R', 'G', 'B', 'Y')
players = []

class Controlador():
    
    def __init__(self):
        self.context = zmq.Context()
        self.cliente = self.context.socket(zmq.REQ)
        self.servidor = self.context.socket(zmq.REP)
        self.servidor.bind("tcp://*:5555")
        
        
    def waitForPlayers(self, capacity = 4):
        for _ in range(capacity):
            rPacket = json.loads(self.servidor.recv())
            players.append(rPacket)
            self.servidor.send_string("conectado")
            
    def clearIps(self):
        players.clear()
        
    def waitForDice(self, player):
        ip = player['ip']
        puerto = player['puerto']
        nombre = player['nombre']
        
        direction = "tcp://{}:{}".format(ip, puerto)
        
        self.cliente.connect(direction)
        
        self.cliente.send_string(json.dumps(["dice","Es tu turno {}".format(nombre)]))
        diceResult = self.cliente.recv()
        
        self.cliente.disconnect(direction)
        print(json.loads(diceResult))
        
        return json.loads(diceResult)
    
    
    def endGame(self):
        for player in players:
            ip = player['ip']
            puerto = player['puerto']
            
            direction = "tcp://{}:{}".format(ip, puerto)
            self.cliente.connect(direction)
            self.cliente.send_string(json.dumps(["end"]))
            self.cliente.recv()
        
            self.cliente.disconnect(direction)
        
    def broadCast(self, frame):
        packet = json.dumps(frame)
        for player in players:
            ip = player['ip']
            puerto = player['puerto']
            
            direction = "tcp://{}:{}".format(ip, puerto)
            self.cliente.connect(direction)
            self.cliente.send_string(packet)
            self.cliente.recv()
        
            self.cliente.disconnect(direction)
            
        

control = Controlador()
table = Tablero()

control.waitForPlayers()
# control.endGame()

pieceCount = 1

for player, color in zip(players, colores):
    player['fichas'] = []
    for token in range(pieceCount):
        f = Ficha('{}{}'.format(color, token+1))
        f.setStart()
        f.setSequence()
        table.fichas.append(f)
        player['fichas'].append(f)
        
os.system('cls')
table.update()

control.broadCast(['table',table.casillas])

while not table.ended:
    for player in players:
        print('turno de ' + str(f.color))
        dado = control.waitForDice(player)[0]
        sleep(2)
        player['fichas'][0].move(dado)
        os.system('cls')
        table.update()
        control.broadCast(['table',table.casillas])
        if table.ended:
            control.endGame()
            break