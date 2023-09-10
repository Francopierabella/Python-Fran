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
            ['-','-','-','1','-','-','-'],
            ['-','-','-','1','-','-','-'],
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
                    
def SiguientesposicionesValida(tablero:list,fila,columna,orientacion,piezas):
    listaDeposibles = []
    if fila >= 0 and fila <= 7 and columna >= 0 and columna <= 6: 
        if piezas == 2:
            if orientacion == 'H':
                if columna >= 1 and columna <= 5:
                    for i in range(-1,2):
                        if tablero[fila][columna + i] == '-':
                            listaDeposibles.append(((fila,columna + i),))
                elif columna == 0:
                    if tablero[fila][columna + 1] == '-':
                        listaDeposibles.append(((fila,columna + 1),))
                elif columna == 6:
                    if tablero[fila][columna - 1] == '-':
                        listaDeposibles.append(((fila,columna - 1),)) 
            elif orientacion == 'V':
                if fila >= 1 and fila <= 6:
                    for  j in range(-1,2):
                        if tablero[fila + j][columna] == '-':
                            listaDeposibles.append(((fila + j,columna),))
                elif fila == 0:
                    if tablero [fila + 1][columna] == '-':
                        listaDeposibles.append(((fila + 1,columna),))
                elif fila == 7:
                    if tablero[fila - 1][columna] == '-':
                        listaDeposibles.append(((fila - 1,columna),))
        elif piezas == 3:
            if orientacion == 'H':
                if columna == 2 or columna == 3 or columna == 4:
                    if tablero[fila][columna - 1] and tablero [fila][columna - 2] == '-':
                        listaDeposibles.append(((fila,columna - 1),(fila,columna - 2)))
                    if tablero[fila][columna + 1] and tablero [fila][columna + 2] == '-':
                        listaDeposibles.append(((fila,columna + 1),(fila,columna + 2)))
                elif columna == 0 or columna == 1:
                    if tablero[fila][columna + 1] and tablero [fila][columna + 2] == '-':
                        listaDeposibles.append(((fila,columna + 1),(fila,columna + 2)))
                elif columna == 5 or columna == 6:
                    if tablero[fila][columna - 1] and tablero [fila][columna - 2] == '-':
                        listaDeposibles.append(((fila,columna - 1),(fila,columna - 2)))
            elif orientacion == 'V':
                if fila >= 2 and fila <= 5:
                    if tablero[fila + 1][columna] == '-' and tablero[fila + 2] [columna] == '-':
                        listaDeposibles.append(((fila + 1,columna),(fila + 2,columna)))
                    if tablero[fila - 1][columna] == '-' and tablero[fila - 2] [columna] == '-':
                        listaDeposibles.append(((fila - 1,columna),(fila - 2,columna)))
                elif fila == 0 or fila == 1:
                    if tablero[fila + 1][columna] == '-' and tablero[fila + 2] [columna] == '-':
                        listaDeposibles.append(((fila + 1,columna),(fila + 2,columna)))
                elif fila == 6 or fila == 7:
                    if tablero[fila - 1][columna] == '-' and tablero[fila - 2] [columna] == '-':
                        listaDeposibles.append(((fila - 1,columna),(fila - 2,columna)))
        elif piezas == 4:
            if orientacion == 'H':
                if columna == 3:
                    if tablero[fila][columna + 1] == '-' and tablero[fila][columna + 2] == '-' and tablero[fila][columna + 3] == '-':
                        listaDeposibles.append(((fila,columna + 1),(fila,columna + 2),(fila,columna + 3)))
                    if tablero[fila][columna - 1] == '-' and tablero[fila][columna - 2] == '-' and tablero[fila][columna - 3] == '-':
                        listaDeposibles.append(((fila,columna - 1),(fila,columna - 2),(fila,columna - 3)))
                if columna == 0 or columna == 1 or columna == 2:
                    if tablero[fila][columna + 1] == '-' and tablero[fila][columna + 2] == '-' and tablero[fila][columna + 3] == '-':
                        listaDeposibles.append(((fila,columna + 1),(fila,columna + 2),(fila,columna + 3)))
                if columna == 4 or columna == 5 or columna == 6:
                    if tablero[fila][columna - 1] == '-' and tablero[fila][columna - 2] == '-' and tablero[fila][columna - 3] == '-':
                        listaDeposibles.append(((fila,columna - 1),(fila,columna - 2),(fila,columna - 3)))
            elif orientacion == 'V':
                if fila == 3 or fila == 4:
                    if tablero[fila + 1][columna] == '-' and tablero[fila + 2][columna] == '-' and tablero[fila +3][columna] == '-':
                        listaDeposibles.append(((fila + 1,columna),(fila + 2,columna),(fila + 3,columna)))
                    if tablero[fila - 1][columna] == '-' and tablero[fila - 2][columna] == '-' and tablero[fila - 3][columna] == '-':
                        listaDeposibles.append(((fila - 1,columna),(fila - 2,columna),(fila - 3,columna)))
                if fila == 0 or fila == 1 or fila == 2:
                    if tablero[fila + 1][columna] == '-' and tablero[fila + 2][columna] == '-' and tablero[fila + 3][columna] == '-':
                        listaDeposibles.append(((fila + 1,columna),(fila + 2,columna),(fila + 3,columna)))
                if fila == 5 or fila == 6 or fila == 7:
                    if tablero[fila - 1][columna] == '-' and tablero[fila - 2][columna] == '-' and tablero[fila - 3][columna] == '-':
                        listaDeposibles.append(((fila - 1,columna),(fila - 2,columna),(fila - 3,columna)))               
             
    return listaDeposibles    
                         
def tuplasSiguientes(listadeposibles:list):
    JugadasPosibles = []
    for i in range (len(listadeposibles)):
        for j in listadeposibles[i]:
            JugadasPosibles.append(j)
    return JugadasPosibles
def posicionInicialValida(tablero,fila,columna,orientacion,piezas):
    if tablero[fila][columna] == '-' and (SiguientesposicionesValida(tablero,fila,columna,orientacion,piezas)) != []:
        return True
    return False

            
def valida(posicion:tuple,listadeposiciones):
    if posicion in tuplasSiguientes(listadeposiciones):
        return True
    return False            
def colocarBarco(turno,tableroActualizadoJugador1,tableroActualizadoJugador2):
    cantidadDebarcos = 1
    if Turno(turno) == 'Jugador 1':
        print("Hora de colocar tus barcos Jugador 1!")
        print("Situalos estrategicamente asi tendras mas chances de ganar!")
        for j in range(cantidadDebarcos):
            piezas = int(input("De cuantas piezas sera su barco(2,3): "))
            orientacion = str(input("Ingrese la orientacion de su barco. 'V' (vertical) o 'H' (horizontal): "))
            filainicial = int(input("Ingrese la fila en la que irá la primer pieza: "))
            columnaincial = int(input("Ingrese la columna en la que irá la primer pieza: "))
            if posicionInicialValida(tableroActualizadoJugador1,filainicial,columnaincial,orientacion,piezas):
                tableroActualizadoJugador1 [filainicial][columnaincial] = '1'
                for i in range(piezas - 1):
                    print("Posiciones posibles:",tuplasSiguientes(SiguientesposicionesValida(tableroActualizadoJugador1,filainicial,columnaincial,orientacion,piezas)))
                    print(imprime_tablero(tableroActualizadoJugador1))
                    filaSiguiente = int(input("Ingrese la fila en la que seguira el barco: "))
                    columnaSiguiente = int(input("Ingrese la columna en la que seguira el barco: "))
                    if valida((filaSiguiente,columnaSiguiente),SiguientesposicionesValida(tableroActualizadoJugador1,filainicial,columnaincial,orientacion,piezas)):
                        tableroActualizadoJugador1[filaSiguiente][columnaSiguiente] = '1' 
                        print(imprime_tablero(tableroActualizadoJugador1))   
                    else:
                        print("Error, Perdiste el turno")   
        return tableroActualizadoJugador1                         
    elif Turno(turno) == 'Jugador 2':
        print("Hora de colocar tus barcos Jugador 2!")
        print("Situalos estrategicamente asi tendras mas chances de ganar!")
        for j in range(cantidadDebarcos):
            piezas = int(input("De cuantas piezas sera su barco(2,3): "))
            orientacion = str(input("Ingrese la orientacion de su barco. 'V' (vertical) o 'H' (horizontal): "))
            filainicial = int(input("Ingrese la fila en la que irá la primer pieza: "))
            columnaincial = int(input("Ingrese la columna en la que irá la primer pieza: "))
            if posicionInicialValida(tableroActualizadoJugador2,filainicial,columnaincial,orientacion,piezas):
                tableroActualizadoJugador2 [filainicial][columnaincial] = '1'
                for i in range(piezas - 1):
                    print("Posiciones posibles:",tuplasSiguientes(SiguientesposicionesValida(tableroActualizadoJugador2,filainicial,columnaincial,orientacion,piezas)))
                    print(imprime_tablero(tableroActualizadoJugador2))
                    filaSiguiente = int(input("Ingrese la fila en la que seguira el barco: "))
                    columnaSiguiente = int(input("Ingrese la columna en la que seguira el barco: "))
                    if valida((filaSiguiente,columnaSiguiente),SiguientesposicionesValida(tableroActualizadoJugador2,filainicial,columnaincial,orientacion,piezas)):
                        tableroActualizadoJugador2[filaSiguiente][columnaSiguiente] = '1' 
                        print(imprime_tablero(tableroActualizadoJugador2))   
                    else:
                        print("Error, Perdiste el turno")  
        return tableroActualizadoJugador2

def piezaAlrededor(tablero,fila,columna):
    if tablero[fila + 1][columna] == '1' or tablero[fila - 1][columna] == '1'\
        or tablero[fila][columna + 1] == '1' or tablero[fila][columna - 1] == '1':
            return True
    return False
    
print(piezaAlrededor(TableroJugador2(),3,3))
def HundirBarcosDelJugador1(tablero,fila,columna):
    if tablero[fila][columna] != '-':
        tablero[fila][columna] = '-'
        if piezaAlrededor(tablero,fila,columna):
            print("Has hundido una pieza!")
        else:
            print("Le has hundido un barco felicidades!")
    else:
        print("Agua")            
def HundirBarcosDelJugador2(tablero,fila,columna):
    if tablero[fila][columna] != '-':
        tablero[fila][columna] = '-'
        if piezaAlrededor(tablero,fila,columna):
            print("Has hundido una pieza!")
        else:
            print("Le has hundido un barco felicidades!")
    else:
        print("Agua")                
# HundirBarcosDelJugador1(colocarBarco(0,TableroJugador1(),TableroJugador2()),3,3)

def ganador(tablero):
    for i in tablero:
        for j in i:
            if j != '-':
                return False
    return True        
def juego():
    turno = 0
    tableroActualizadoJ1 = TableroJugador1()
    tableroActualizadoJ2 = TableroJugador2()
    terminaJuego = False
    colocarBarco(turno,tableroActualizadoJ1,tableroActualizadoJ2)
    turno += 1
    colocarBarco(turno,tableroActualizadoJ1,tableroActualizadoJ2)
    print(imprime_tablero(tableroActualizadoJ1))
    print(imprime_tablero(tableroActualizadoJ2))
    print("Una vez colocados los barcos... A JUGAR!!")
    while not terminaJuego:
        if Turno(turno) == 'Jugador 1':
            print("Jugador 1! Es tu turno de jugar!")
            fila = int(input("En que fila piensas que Jugador 2 coloco sus barcos? : "))
            columna = int(input("En que columna piensas que Jugador 2 coloco sus barcos? : "))
            HundirBarcosDelJugador2(tableroActualizadoJ2,fila,columna)
            if ganador(tableroActualizadoJ2):
                terminaJuego  = True
                print("Felicidades! Ha ganado jugador 1")
            turno += 1
        elif Turno(turno) == 'Jugador 2':
            print("Jugador 2! Es tu turno de jugar!")
            fila = int(input("En que fila piensas que Jugador 1 coloco sus barcos? : "))
            columna = int(input("En que columna piensas que Jugador 1 coloco sus barcos? : "))
            HundirBarcosDelJugador1(tableroActualizadoJ1,fila,columna)
            if ganador(tableroActualizadoJ2):
                terminaJuego  = True
                print("Felicidades! Ha ganado jugador 2")
            turno += 1
    print("Gracias por jugar!")            
        
juego()        
    
    
    



 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    