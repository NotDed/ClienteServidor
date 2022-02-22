import zmq
import json
import os

from utilityFunct import getMyIp, rollTheDice, prettyPrint

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
        mensaje = json.loads(self.servidor.recv())
        if mensaje[0] == 'dice':
            print(mensaje[1])
            dados = [rollTheDice(), rollTheDice()]
            dados =  json.dumps(dados)
            print(dados)
            self.servidor.send_string(dados)
            return False
        if mensaje[0] == 'table':
            os.system('cls')
            prettyPrint(mensaje[1])
            self.servidor.send_string('_')
            return False
        if mensaje[0] == 'end':
            self.servidor.send_string('_')
            return True
            
        return True
    
    def getBroadcast(self):
        rPacket = json.loads(self.servidor.recv())
        prettyPrint(rPacket[1])
        self.servidor.send_string("_")
