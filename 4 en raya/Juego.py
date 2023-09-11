'''
Funcionamiento del juego:
Dos jugadores, o sea, ficha R (rojas) vs ficha N (negras).
El programa le pedira al usuario ingresar en que columna quiere jugar la ficha.
El programa chequeara si la posicion dada es valida, es decir que:
1) no haya otra ficha en esa posicion
2) que pertenezca al tablero
3) que sea una mas de la posicion de abajo, es decir, no se puede poner una ficha en la posicion 3 si no hay una ficha en la 2.
    En palabras mas simples, la ficha va a la posicion mas baja de esa columna.
...
Jugador 1 == 'R'
Jugador 2 == 'N'
Como hago para saber a quien le toca
Funcion Turno que devuelve 'R' si turno es par y 'N' si es impar
Funcion chequear diagonal. Una vez puesta la ficha en la posicion dada, el programa debe chequear las diagonales inferiores.
    Esto se hace verificando la columna dada - 1 y + 1 en la fila de abajo y asi 3 veces.
    Retorna True si hay 4 del mismo color en diagonal y False de lo contrario.
 
'''

def tablero():
    return [['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-']]
# print(len(tablero())) == 8
def imprime_tablero(tablero:list):
    for i in tablero:
        print(i)

# Las fichas son 'R' -> Rojas y 'N' -> Negras
def Turno(turno:int):
    if turno % 2 == 0:
        return 'R'
    else:
        return 'N'       
    
def jugadaValida(tablero,fila,columna):
    if fila >= 0 and fila <= 7 and columna >= 0 and columna <= 6:
        if tablero[fila][columna] == '-':
            if fila != 7:
                if tablero[fila + 1][columna] != '-':
                    return True
                else:
                    return False
            return True
    return False


def jugada(tablero,turno,fila,columna):
    if jugadaValida(tablero,fila,columna):
        if Turno(turno) == 'N':
            tablero[fila][columna] = 'N'
            return tablero
        else:
            if Turno(turno) == 'R':
                tablero[fila][columna] = 'R'
                return tablero
    else:
        print("jugada no valida")
        return tablero


def chequearDiagonal(tablero,fila,columna):
    if tablero[fila][columna] == 'N':
        if fila >= 0 and fila <= 2 and columna <= 2 and columna >= 0: # este if chequea
            if tablero[fila + 1][columna + 1] == 'N':
                if tablero[fila + 2][columna + 2] == 'N':
                    if tablero[fila + 3][columna + 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            else: 
                return False
        elif fila >= 0 and fila <= 2 and columna >= 4 and columna <=6:
            if tablero[fila - 1][columna - 1] == 'N':
                if tablero[fila - 2][columna - 2] == 'N':
                    if tablero[fila - 3][columna - 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            else: 
                return False
        
        elif fila >= 5 and fila <= 7 and columna <= 2 and columna >= 0:
            if tablero[fila - 1][columna + 1] == 'N':
                if tablero[fila - 2][columna + 2] == 'N':
                    if tablero[fila - 3][columna + 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            else: 
                return False
        elif fila >= 5 and fila <= 7 and columna >= 4 and columna <= 6:
            if tablero[fila - 1][columna - 1] == 'N':
                if tablero[fila - 2][columna - 2] == 'N':
                    if tablero[fila - 3][columna - 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            else: 
                return False
            
        elif fila == 3 or fila == 4 and columna >= 0 and columna <= 2:
            if tablero[fila - 1][columna + 1] == 'N':
                if tablero[fila - 2][columna + 2] == 'N':
                    if tablero[fila - 3][columna + 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila + 1][columna + 1] == 'N':
                if tablero[fila + 2][columna + 2] == 'N':
                    if tablero[fila + 3][columna + 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif fila == 3 or fila == 4 and columna >= 4 and columna <= 6:
            if tablero[fila - 1][columna - 1] == 'N':
                if tablero[fila - 2][columna - 2] == 'N':
                    if tablero[fila - 3][columna - 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila + 1][columna - 1] == 'N':
                if tablero[fila + 2][columna - 2] == 'N':
                    if tablero[fila + 3][columna - 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False    
        elif fila >= 0 and fila <= 2 and columna == 3:
            if tablero[fila + 1][columna - 1] == 'N':
                if tablero[fila + 2][columna - 2] == 'N':
                    if tablero[fila + 3][columna - 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila - 1][columna + 1] == 'N':
                if tablero[fila - 2][columna + 2] == 'N':
                    if tablero[fila - 3][columna + 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif fila >= 5 and fila <= 7 and columna == 3:
            if tablero[fila - 1][columna + 1] == 'N':
                if tablero[fila - 2][columna + 2] == 'N':
                    if tablero[fila - 3][columna + 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila - 1][columna - 1] == 'N':
                if tablero[fila - 2][columna - 2] == 'N':
                    if tablero[fila - 3][columna - 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif fila == 3 or fila == 4 and columna == 3:
            if tablero[fila - 1][columna + 1] == 'N':
                if tablero[fila - 2][columna + 2] == 'N':
                    if tablero[fila - 3][columna + 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila - 1][columna - 1] == 'N':
                if tablero[fila - 2][columna - 2] == 'N':
                    if tablero[fila - 3][columna - 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila + 1][columna + 1] == 'N':
                if tablero[fila + 2][columna + 2] == 'N':
                    if tablero[fila + 3][columna + 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila + 1][columna - 1] == 'N':
                if tablero[fila + 2][columna - 2] == 'N':
                    if tablero[fila + 3][columna - 3] == 'N':
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
    if tablero[fila][columna] == 'R':
        if fila >= 0 and fila <= 2 and columna <= 2 and columna >= 0: # este if chequea
            if tablero[fila + 1][columna + 1] == 'R':
                if tablero[fila + 2][columna + 2] == 'R':
                    if tablero[fila + 3][columna + 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            else: 
                return False
        elif fila >= 0 and fila <= 2 and columna >= 4 and columna <=6:
            if tablero[fila - 1][columna - 1] == 'R':
                if tablero[fila - 2][columna - 2] == 'R':
                    if tablero[fila - 3][columna - 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            else: 
                return False
        
        elif fila >= 5 and fila <= 7 and columna <= 2 and columna >= 0:
            if tablero[fila - 1][columna + 1] == 'R':
                if tablero[fila - 2][columna + 2] == 'R':
                    if tablero[fila - 3][columna + 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            else: 
                return False
        elif fila >= 5 and fila <= 7 and columna >= 4 and columna <= 6:
            if tablero[fila - 1][columna - 1] == 'R':
                if tablero[fila - 2][columna - 2] == 'R':
                    if tablero[fila - 3][columna - 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            else: 
                return False
            
        elif fila == 3 or fila == 4 and columna >= 0 and columna <= 2:
            if tablero[fila - 1][columna + 1] == 'R':
                if tablero[fila - 2][columna + 2] == 'R':
                    if tablero[fila - 3][columna + 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila + 1][columna + 1] == 'R':
                if tablero[fila + 2][columna + 2] == 'R':
                    if tablero[fila + 3][columna + 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif fila == 3 or fila == 4 and columna >= 4 and columna <= 6:
            if tablero[fila - 1][columna - 1] == 'R':
                if tablero[fila - 2][columna - 2] == 'R':
                    if tablero[fila - 3][columna - 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila + 1][columna - 1] == 'R':
                if tablero[fila + 2][columna - 2] == 'R':
                    if tablero[fila + 3][columna - 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False    
        elif fila >= 0 and fila <= 2 and columna == 3:
            if tablero[fila + 1][columna - 1] == 'R':
                if tablero[fila + 2][columna - 2] == 'R':
                    if tablero[fila + 3][columna - 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila - 1][columna + 1] == 'R':
                if tablero[fila - 2][columna + 2] == 'R':
                    if tablero[fila - 3][columna + 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif fila >= 5 and fila <= 7 and columna == 3:
            if tablero[fila - 1][columna + 1] == 'R':
                if tablero[fila - 2][columna + 2] == 'R':
                    if tablero[fila - 3][columna + 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila - 1][columna - 1] == 'R':
                if tablero[fila - 2][columna - 2] == 'R':
                    if tablero[fila - 3][columna - 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif fila == 3 or fila == 4 and columna == 3:
            if tablero[fila - 1][columna + 1] == 'R':
                if tablero[fila - 2][columna + 2] == 'R':
                    if tablero[fila - 3][columna + 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila - 1][columna - 1] == 'R':
                if tablero[fila - 2][columna - 2] == 'R':
                    if tablero[fila - 3][columna - 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila + 1][columna + 1] == 'R':
                if tablero[fila + 2][columna + 2] == 'R':
                    if tablero[fila + 3][columna + 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
            elif tablero[fila + 1][columna - 1] == 'R':
                if tablero[fila + 2][columna - 2] == 'R':
                    if tablero[fila + 3][columna - 3] == 'R':
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
        

def chequearFila(tablero,fila,columna):
    if tablero[fila][columna] == 'N':
        if columna >= 0 and columna <= 3:
            if tablero[fila][columna + 1] == 'N':
                if tablero[fila][columna + 2] == 'N':
                    if tablero[fila][columna + 3] == 'N':
                        return True
            else:
                return False
        if columna >=4 and columna <= 6: 
            if tablero[fila][columna - 1] == 'N':
                if tablero[fila][columna - 2]== 'N':
                    if tablero[fila][columna - 3]== 'N':
                        return True
        else:
            return False
    if tablero[fila][columna] == 'R':
        if columna >= 0 and columna <= 3:
            if tablero[fila][columna + 1] == 'R':
                if tablero[fila][columna + 2] == 'R':
                    if tablero[fila][columna + 3] == 'R':
                        return True
            else:
                return False
        if columna >=4 and columna <= 6: 
            if tablero[fila][columna - 1] == 'R':
                if tablero[fila][columna - 2]== 'R':
                    if tablero[fila][columna - 3]== 'R':
                        return True
        else:
            return False
    

def chequearColumna(tablero,fila,columna):
    if tablero[fila][columna] == 'N':
        if fila >= 0 and fila <= 3:
            if tablero[fila + 1][columna] == 'N':
                if tablero[fila + 2][columna] == 'N':
                    if tablero[fila + 3][columna] == 'N':
                        return True
            else:
                return False
        if fila >= 4 and fila <= 7:
            if tablero[fila - 1][columna] == 'N':
                if tablero[fila - 2][columna] == 'N':
                    if tablero[fila - 3][columna] == 'N':
                        return True
            else: 
                return False
    if tablero[fila][columna] == 'R':
        if fila >= 0 and fila <= 3:
            if tablero[fila + 1][columna] == 'R':
                if tablero[fila + 2][columna] == 'R':
                    if tablero[fila + 3][columna] == 'R':
                        return True
            else:
                return False
        if fila >= 4 and fila <= 7:
            if tablero[fila - 1][columna] == 'R':
                if tablero[fila - 2][columna] == 'R':
                    if tablero[fila - 3][columna] == 'R':
                        return True
            else: 
                return False        
                       
def chequearGanador(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero [i][j] != '-':
                if chequearDiagonal(tablero,i,j) or chequearColumna(tablero,i,j) or chequearFila(tablero,i,j):
                    return True
    return False

def tableroLleno(tablero):
    fichasN = 0
    fichasR = 0
    for filas in tablero:
        for elemento in filas:
            if elemento == 'N':
                fichasN +=1
            elif elemento == 'R':
                fichasR += 1
    return fichasR + fichasN == 56

# def juego ():
#     turno = 0
#     tableroActual = tablero()
#     fila = int(input("Fila: "))
#     columna = int(input("Columna: "))
#     Terminajuego = False
#     while not Terminajuego or not tableroLleno(tableroActual): 
#         if tableroLleno(tableroActual):
#             Terminajuego = True          
#         elif jugadaValida(tableroActual,fila,columna):
#             tableroActual = jugada(tableroActual,turno,fila,columna)
#             imprime_tablero(tableroActual)
#             turno += 1
#             if chequearGanador(tableroActual):
#                 if tableroActual[fila][columna] == 'N':
#                     Terminajuego = True
#                     return "Gano Negro"
#                 elif tableroActual[fila][columna] == 'R':
#                     Terminajuego = True
#                     return "Gano Rojo"      
#             fila = int(input("Fila: "))
#             columna = int(input("Columna: "))     
#         else:
#             print("jugada invalida, perdiste el turno")
#             turno += 1
#             fila = int(input("Fila: "))
#             columna = int(input("Columna: ")) 
#     print("El juego ha terminado")
            
# print(juego())

                
                        
            
                       
        
        

            
            
            
        
    
    




    