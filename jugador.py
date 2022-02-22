import zmq
import json

import time

from utilityFunct import getMyIp, rollTheDice

context = zmq.Context()

class Jugador():
    
    def __init__(self, puerto, nombre,):
        self.context = zmq.Context()
        self.cliente = self.context.socket(zmq.REQ)
        self.servidor = self.context.socket(zmq.REP)
        self.servidor.bind("tcp://*:{}".format(puerto))
        
        self.myIp = getMyIp()
        self.puerto = puerto
        self.nombre = nombre
        
    def sendPlayer(self, ip, puerto):
        sPacket = {'ip':self.myIp, 'puerto':self.puerto, 'nombre':self.nombre}
        sPacket = json.dumps(sPacket)
        
        self.cliente.connect("tcp://{}:{}".format(ip, puerto))
        self.cliente.send_string(sPacket)
        
        message = self.cliente.recv()
        print(message)
        
    def waitMyTurn(self):
        mensaje = str(self.servidor.recv())
        print(mensaje)
        dados = [rollTheDice(), rollTheDice()]
        dados =  json.dumps(dados)
        print(dados)
        self.servidor.send_string(dados)