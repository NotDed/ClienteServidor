from socket import gethostbyname, gethostname
from colorama import Fore, Style
from random import randint

def getMyIp():
    return gethostbyname(gethostname())

def rollTheDice(diceSize = 4):
    return randint(1,diceSize)

def prettyPrint(casillas):
        for casilla in casillas:
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
                    print('⌗ ', end ='')
            print()