#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

# import time
# import zmq

# context = zmq.Context()
# socket = context.socket(zmq.REP)
# socket.bind("tcp://*:5555")

# dirs = []

# def getIps():
#     for _ in range(4):
#         dirs.append(socket.recv())
#         socket.send(b"conectado")

#     print(dirs)

import zmq
import json

players = []

class Controlador():
    
    def __init__(self):
        self.context = zmq.Context()
        self.cliente = self.context.socket(zmq.REQ)
        self.servidor = self.context.socket(zmq.REP)
        self.servidor.bind("tcp://*:5555")
        
        
    def getIps(self):
        for _ in range(4):
            rPacket = json.loads(self.servidor.recv())
            print(rPacket)
            players.append(rPacket['nombre'])
            self.servidor.send_string("conectado")
            
    def clearIps(self):
        players.clear()
        
    def boradCast():
        pass
        

control = Controlador()
control.getIps()
print(players)
control.clearIps()
print(players)