import zmq
import json
from time import sleep

colores = ['R', 'G', 'B', 'Y']
players = []

class Controlador():
    
    def __init__(self):
        self.context = zmq.Context()
        self.cliente = self.context.socket(zmq.REQ)
        self.servidor = self.context.socket(zmq.REP)
        self.servidor.bind("tcp://*:5555")
        
        
    def waitForPlayers(self):
        for _ in range(2):
            rPacket = json.loads(self.servidor.recv())
            players.append(rPacket)
            self.servidor.send_string("conectado")
            
    def clearIps(self):
        players.clear()
        
    def waitForDice(self, player):
        sleep(2)
        ip = player['ip']
        puerto = player['puerto']
        nombre = player['nombre']
        print(player)
        
        direction = "tcp://{}:{}".format(ip, puerto)
        
        self.cliente.connect(direction)
        
        self.cliente.send_string("Es tu turno {}".format(nombre))
        diceResult = self.cliente.recv()
        
        self.cliente.disconnect(direction)
        print(json.loads(diceResult))
        
    def broadCast():
        pass
        

control = Controlador()
control.waitForPlayers()
for player in players:
    
for player in players:
    print(player)
    control.waitForDice(player)
    sleep(2)