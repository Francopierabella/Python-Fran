'''
El juego va aconstar de dos tableros, uno para cada jugador.
el programa le pedira a cada jugador que le indique donde quiere colocar su/sus barcos.
una vez colocados comienza el juego.
De nuevo, el programa pedira al usuario que diga una posicion del tablero del rival.
Este si fijara si coincide con el barco colocado, y de ser asi, hunidira esa poscion. En 
caso contrairio imprimira "Agua" y pasara al siguiente jugador.
El programa terminara cuando uno de los barcos sea hundido.
Las partes de los barcos del jugador 1 estan representados por 
'''


def TableroJugador1():
    return [['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-']]
def TableroJugador2 ():
    return [['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-']]
 
 
def imprime_tablero(tablero:list):
    for i in tablero:
        print (i) 

def Turno(turno:int):
    if turno % 2 == 0:
        return 'Jugador 1'
    else:
        return 'Jugador 2'


    
    



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    