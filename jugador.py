import zmq
import json

from utilityFunct import getMyIp

context = zmq.Context()
# servidor = context.socket(zmq.REP)
# servidor.bind("tcp://*:1234")

# def sendIp(nombre, puerto):
#     sPacket = (sckt.gethostbyname(sckt.gethostname()), puerto, nombre)
#     sPacket = json.dumps(sPacket)
#     clienteIp = context.socket(zmq.REQ)
#     clienteIp.connect("tcp://localhost:5555")
#     clienteIp.send_string(sPacket)

#     #  Get the reply.
#     message = clienteIp.recv()
#     print("Received reply [ %s ]" % (message))
    
    
# sendIp('jose','5555')
# sendIp('juan','1234')

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
        
        
j1 = Jugador('4444', 'juan')
j1.sendPlayer('localhost', '5555')
j2 = Jugador('1234', 'jose')    
j2.sendPlayer('localhost', '5555') 