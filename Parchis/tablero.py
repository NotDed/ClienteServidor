from colorama import Fore, Style

class Tablero():
    def __init__(self, dim = 7):
        self.dim = dim
        self.ended = False
        self.casillas = [['▢ ' for i in range(self.dim)] for j in range(self.dim)]
        self.fichas = []
        
    def wipe(self):
        self.casillas = [['▢ ' for i in range(self.dim)] for j in range(self.dim)]
        
    def interaction(self):
        for ficha in self.fichas:
            if ficha.inTurn:
                for comida in self.fichas:
                    if (not comida.inTurn) and comida.getPos() == ficha.getPos() and comida.color[0] != ficha.color[0]:
                        comida.sendToJail()
                        print(str(ficha.color) + " se comió a: " + str(comida.color))
                ficha.inTurn = 0
                
    def win(self):
        for ficha in self.fichas:
            if ficha.getPos() == (3,3):
                print("el ganador es " + str(ficha.color))
                self.ended = True
                break
                
            
    def update(self):
        self.win()
        self.interaction()
        self.wipe()
        for ficha in self.fichas:
            self.casillas[ficha.x][ficha.y] = ficha.color
            
        self.prettyPrint()
            
    def prettyPrint(self):
        for casilla in self.casillas:
            for casillita in casilla:
                if(casillita[0] == 'R'):
                    print(f"{Fore.RED}♟{casillita[1]}{Style.RESET_ALL}", end ='')
                elif(casillita[0] == 'G'):
                    print(f"{Fore.GREEN}♟{casillita[1]}{Style.RESET_ALL}", end ='')
                elif(casillita[0] == 'B'):
                    print(f"{Fore.BLUE}♟{casillita[1]}{Style.RESET_ALL}", end ='')
                elif(casillita[0] == 'Y'):
                    print(f"{Fore.YELLOW}♟{casillita[1]}{Style.RESET_ALL}", end ='')
                else:
                    print('▢ ', end ='')
            print()
                