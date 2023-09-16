def tablero():
    return [['TN','CN','AN','KN','RN','AN','CN','TN'],
            ['PN','PN','PN','PN','PN','PN','PN','PN'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['PB','PB','PB','PB','PB','PB','PB','PB'],
            ['TB','CB','AB','RB','KB','AB','CB','TB']]

def imprime_tablero(tablero):
    for i in tablero:
        print(i)

def Turno(turno):
    if turno % 2 == 0:
        return 'negro'
    else:
        return 'blanco'
def piezas(pieza,color):
    if pieza == 'peon':
        if color == 'negro':
            return 'PN'
        return 'PB'
    elif pieza == 'alfil':
        if color == 'negro':
            return 'AN'
        return 'AB'
    elif pieza == 'torre':
        if color == 'negro':
            return 'TN'
        return 'TB'
    elif pieza == 'caballo':
        if color == 'negro':
            return 'CN'
        return 'CB'
    elif pieza == 'reina':
        if color == 'negro':
            return 'RN'
        return 'RB'
    elif pieza == 'rey':
        if color == 'negro':
            return 'KN'
        return 'KB'

def peonNInicial(tablero,fila,columna):
    if fila == 1:    
        if tablero[fila][columna] == 'PN':
            return True
        else:
            return False
    return False
def peonBInicial(tablero,fila,columna):
    if fila == 6:
        if tablero[fila][columna] == 'PB':
            return True
        else:
            return False
    return False
def movimientoPeonInicial(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if peonNInicial(tablero,fila,columna):
        if columna == 0:
            if tablero[fila + 1][columna] == '--':
                listaDeMovimientosPosibles.append((fila + 1,columna))
            if tablero[fila + 2][columna] == '--':
                listaDeMovimientosPosibles.append((fila + 2,columna))
            if tablero[fila + 1][columna + 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna + 1))
        elif columna == 7:
            if tablero[fila + 1][columna] == '--':
                listaDeMovimientosPosibles.append((fila + 1,columna))
            if tablero[fila + 2][columna] == '--':
                listaDeMovimientosPosibles.append((fila + 2,columna))
            if tablero[fila + 1][columna - 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna - 1))
        elif columna >= 1 and columna <= 6:
            if tablero[fila + 1][columna] == '--':
                listaDeMovimientosPosibles.append((fila + 1,columna))
            if tablero[fila + 2][columna] == '--':
                listaDeMovimientosPosibles.append((fila + 2,columna))
            if tablero[fila + 1][columna + 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna + 1))
            if tablero[fila + 1][columna - 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna - 1))
    elif peonBInicial(tablero,fila,columna):
        if columna == 0:
            if tablero[fila - 1][columna] == '--':
                listaDeMovimientosPosibles.append((fila - 1,columna))
            if tablero[fila - 2][columna] == '--':
                listaDeMovimientosPosibles.append((fila - 2,columna))
            if tablero[fila - 1][columna + 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna + 1))
        elif columna == 7:
            if tablero[fila - 1][columna] == '--':
                listaDeMovimientosPosibles.append((fila - 1,columna))
            if tablero[fila - 2][columna] == '--':
                listaDeMovimientosPosibles.append((fila - 2,columna))
            if tablero[fila - 1][columna - 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna - 1))
        elif columna >= 1 and columna <= 6:
            if tablero[fila - 1][columna] == '--':
                listaDeMovimientosPosibles.append((fila - 1,columna))
            if tablero[fila - 2][columna] == '--':
                listaDeMovimientosPosibles.append((fila - 2,columna))
            if tablero[fila - 1][columna + 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna + 1))
            if tablero[fila - 1][columna - 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna - 1))
    elif tablero[fila][columna][1] == 'N':
        if fila >= 2 and fila <= 6 and columna >= 1 and columna <= 6:
            if tablero[fila + 1][columna] == '--':
                listaDeMovimientosPosibles.append((fila + 1,columna))
            if tablero[fila + 1][columna - 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna - 1))
            if tablero[fila + 1][columna + 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna + 1))
        if fila >= 2 and fila <= 6 and columna == 0:
            if tablero[fila + 1][columna + 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna + 1))
        if fila >= 2 and fila <= 6 and columna == 7:
            if tablero[fila + 1][columna - 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna - 1))
    elif tablero[fila][columna][1] == 'B':
        if fila <= 5 and fila >= 1 and columna >= 1 and columna <= 6:
            if tablero[fila - 1][columna] == '--':
                listaDeMovimientosPosibles.append((fila - 1,columna))
            if tablero[fila - 1][columna - 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna - 1))
            if tablero[fila - 1][columna + 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna + 1))
        if fila <= 5 and fila >= 1 and columna == 0:
            if tablero[fila - 1][columna + 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna + 1))
        if fila <= 5 and fila >= 1 and columna == 7:
            if tablero[fila - 1][columna - 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna - 1))    
       
    return listaDeMovimientosPosibles


# print(movimientoPeonInicial(tablero(),5,3))

def PosicionAPieza(tablero,fila,columna):
    return tablero[fila][columna]


def movientodiagonalArribaDerecha(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    i = 1
    if tablero[fila][columna][1] == 'N':
        while fila - i >= 0 and columna + i <= 7:
            if tablero[fila - i][columna + i] == '--':
                listaDeMovimientosPosibles.append((fila - i,columna + i))
                i += 1
            elif tablero[fila - i][columna + i][1] == 'B':
                listaDeMovimientosPosibles.append((fila - i,columna + i))
                break
            elif tablero[fila - i][columna + i][1] == 'N':
                break
    if tablero[fila][columna][1] == 'B':
        while fila - i >= 0 and columna + i <= 7:
            if tablero[fila - i][columna + i] == '--':
                listaDeMovimientosPosibles.append((fila - i,columna + i))
                i += 1
            elif tablero[fila - i][columna + i][1] == 'N':
                listaDeMovimientosPosibles.append((fila - i,columna + i))
                break
            elif tablero[fila - i][columna + i][1] == 'B':
                break
                    
    return listaDeMovimientosPosibles    
# print(movientodiagonalArribaDerecha(tablero(),7,2))

def movimientodiagonalArribaIzquierda(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    i = 1
    if tablero[fila][columna][1] == 'N':
        while fila - i >= 0 and columna - i >= 0 :
            if tablero[fila - i][columna - i] == '--':
                listaDeMovimientosPosibles.append((fila - i,columna - i))
                i += 1
            elif tablero[fila - i][columna - i][1] == 'B':
                listaDeMovimientosPosibles.append((fila - i,columna - i))
                break
            elif tablero[fila - i][columna - i][1] == 'N':
                break
    if tablero[fila][columna][1] == 'B':
        while fila - i >= 0 and columna - i >= 0:
            if tablero[fila - i][columna - i] == '--':
                listaDeMovimientosPosibles.append((fila - i,columna - i))
                i += 1
            elif tablero[fila - i][columna - i][1] == 'N':
                listaDeMovimientosPosibles.append((fila - i,columna - i))
                break
            elif tablero[fila - i][columna - i][1] == 'B':
                break
    return listaDeMovimientosPosibles
# print(movimientodiagonalArribaIzquierda(tablero(),5,7))

def movimientodiagonalAbajoDerecha(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    i = 1
    if tablero[fila][columna][1] == 'N':
        while fila + i <= 7 and columna + i <= 7:
            if tablero[fila + i][columna + i] == '--':
                listaDeMovimientosPosibles.append((fila + i,columna + i))
                i += 1
            elif tablero[fila + i][columna + i][1] == 'B':
                listaDeMovimientosPosibles.append((fila + i,columna + i))
                break
            elif tablero[fila + i][columna + i][1] == 'N':
                break
    if tablero[fila][columna][1] == 'B':
        while fila + i <= 7 and columna + i <= 7:
            if tablero[fila + i][columna + i] == '--':
                listaDeMovimientosPosibles.append((fila + i,columna + i))
                i += 1
            elif tablero[fila + i][columna + i][1] == 'N':
                listaDeMovimientosPosibles.append((fila + i,columna + i))
                break
            elif tablero[fila + i][columna + i][1] == 'B':
                break
    return listaDeMovimientosPosibles
# print(movimientodiagonalAbajoDerecha(tablero(),2,0))

def movientodiagonalAbajoIzquierda(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    i = 1
    if tablero[fila][columna][1] == 'N':
        while fila + i <= 7 and columna - i >= 0:
            if tablero[fila + i][columna - i] == '--':
                listaDeMovimientosPosibles.append((fila + i,columna - i))
                i += 1
            elif tablero[fila + i][columna - i][1] == 'B':
                listaDeMovimientosPosibles.append((fila + i,columna - i))
                break
            elif tablero[fila + i][columna - i][1] == 'N':
                break
    if tablero[fila][columna][1] == 'B':
        while fila + i <= 7 and columna - i >= 0:
            if tablero[fila + i][columna - i] == '--':
                listaDeMovimientosPosibles.append((fila + i,columna - i))
                i += 1
            elif tablero[fila + i][columna - i][1] == 'N':
                listaDeMovimientosPosibles.append((fila + i,columna + i))
                break
            elif tablero[fila + i][columna - i][1] == 'B':
                break
    return listaDeMovimientosPosibles
# print(movientodiagonalAbajoIzquierda(tablero(),2,7))
def movimientoLateralDerecha(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    i = 1
    if tablero[fila][columna][1] == 'N':
        while columna + i <= 7:
            if tablero[fila][columna + i] == '--':
                listaDeMovimientosPosibles.append((fila,columna + i))
                i += 1
            elif tablero[fila][columna + i][1] == 'B':
                listaDeMovimientosPosibles.append((fila,columna + i))
                break
            elif tablero[fila][columna + i][1] == 'N':
                break
    if tablero[fila][columna][1] == 'B':
        while columna + i <= 7:
            if tablero[fila][columna + i] == '--':
                listaDeMovimientosPosibles.append((fila,columna + i))
                i += 1
            elif tablero[fila][columna + i][1] == 'N':
                listaDeMovimientosPosibles.append((fila,columna + i))
                break
            elif tablero[fila][columna + i][1] == 'B':
                break
    return listaDeMovimientosPosibles
# print(movimientoLateralDerecha(tablero(),4,0))
def movimientoLateralIzquierda(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    i = 1
    if tablero[fila][columna][1] == 'N':
        while columna - i >= 0:
            if tablero[fila][columna - i] == '--':
                listaDeMovimientosPosibles.append((fila,columna - i))
                i += 1
            elif tablero[fila][columna - i][1] == 'B':
                listaDeMovimientosPosibles.append((fila,columna - i))
                break
            elif tablero[fila][columna - i][1] == 'N':
                break
    if tablero[fila][columna][1] == 'B':
        while columna - i >= 0:
            if tablero[fila][columna - i] == '--':
                listaDeMovimientosPosibles.append((fila,columna - i))
                i += 1
            elif tablero[fila][columna - i][1] == 'N':
                listaDeMovimientosPosibles.append((fila,columna - i))
                break
            elif tablero[fila][columna - i][1] == 'B':
                break
            
    return listaDeMovimientosPosibles
# print(movimientoLateralIzquierda(tablero(),4,7))
def movimientoHaciaArriba(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    i = 1
    if tablero[fila][columna][1] == 'N':
        while fila - i >= 0:
            if tablero[fila - i][columna] == '--':
                listaDeMovimientosPosibles.append((fila - i,columna))
                i += 1
            elif tablero[fila - i][columna][1] == 'B':
                listaDeMovimientosPosibles.append((fila - i,columna))
                break
            elif tablero[fila - i][columna][1] == 'N':
                break
    if tablero[fila][columna][1] == 'B':
        while fila - i >= 0:
            if tablero[fila - i][columna] == '--':
                listaDeMovimientosPosibles.append((fila - i,columna))
                i += 1
            elif tablero[fila - i][columna][1] == 'N':
                listaDeMovimientosPosibles.append((fila - i,columna))
                break
            elif tablero[fila - i][columna][1] == 'B':
                break
    return listaDeMovimientosPosibles
# print(movimientoHaciaArriba(tablero(),6,3))
def movimientoHaciaAbajo(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    i = 1
    if tablero[fila][columna][1] == 'N':
        while fila + i <= 7:
            if tablero[fila + i][columna] == '--':
                listaDeMovimientosPosibles.append((fila + i,columna))
                i += 1
            elif tablero[fila + i][columna][1] == 'B':
                listaDeMovimientosPosibles.append((fila + i,columna))
                break
            elif tablero[fila + i][columna][1] == 'N':
                break
    if tablero[fila][columna][1] == 'B':
        while fila + i <= 7:
            if tablero[fila + i][columna] == '--':
                listaDeMovimientosPosibles.append((fila + i,columna))
                i += 1
            elif tablero[fila + i][columna][1] == 'N':
                listaDeMovimientosPosibles.append((fila + i,columna))
                break
            elif tablero[fila + i][columna][1] == 'B':
                break
    return listaDeMovimientosPosibles
# print(movimientoHaciaAbajo(tablero(),2,3))
     
def movimientoCaballo1(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if fila >= 2 and fila <= 5 and columna >= 1 and columna <= 6:
        if tablero[fila + 2][columna + 1] == '--':
            listaDeMovimientosPosibles.append((fila + 2,columna + 1))
        if tablero[fila + 2][columna - 1] == '--':
            listaDeMovimientosPosibles.append((fila + 2,columna - 1))
        if tablero[fila - 2][columna + 1] == '--':
            listaDeMovimientosPosibles.append((fila - 2,columna + 1))
        if tablero[fila - 2][columna - 1] == '--':
            listaDeMovimientosPosibles.append((fila - 2,columna - 1))
    if fila == 0 or fila == 1 and columna >= 1 and columna <= 6:
        if tablero[fila + 2][columna + 1] == '--':
            listaDeMovimientosPosibles.append((fila + 2,columna + 1))
        if tablero[fila + 2][columna - 1] == '--':
            listaDeMovimientosPosibles.append((fila + 2,columna - 1))
    if fila == 6 or fila == 7 and columna >= 1 and columna <= 6:
        if tablero[fila - 2][columna + 1] == '--':
            listaDeMovimientosPosibles.append((fila - 2,columna + 1))
        if tablero[fila - 2][columna - 1] == '--':
            listaDeMovimientosPosibles.append((fila - 2,columna - 1))
    if columna == 0 and (fila == 1 or fila == 0):
        if tablero[fila + 2][columna + 1] == '--':
            listaDeMovimientosPosibles.append((fila + 2,columna + 1))
    if columna == 0 and (fila == 6 or fila == 7):
        if tablero[fila - 2][columna + 1] == '--':
            listaDeMovimientosPosibles.append((fila - 2,columna + 1))
    if columna == 0 and (fila >= 2 and fila <= 5):
        if tablero[fila - 2][columna + 1] == '--':
            listaDeMovimientosPosibles.append((fila - 2,columna + 1))
        if tablero[fila + 2][columna + 1] == '--':
            listaDeMovimientosPosibles.append((fila + 2,columna + 1))
    if columna == 7 and (fila == 0 or fila == 1):
        if tablero[fila + 2][columna - 1] == '--':
            listaDeMovimientosPosibles.append((fila + 2,columna - 1))
    if columna == 7 and (fila ==  6 or fila == 7):
        if tablero[fila - 2][columna - 1] == '--':
            listaDeMovimientosPosibles.append((fila - 2,columna - 1))
    if columna == 7 and (fila >= 2 and fila <= 5):
        if tablero[fila + 2][columna - 1] == '--':
            listaDeMovimientosPosibles.append((fila + 2,columna - 1))
        if tablero[fila - 2][columna - 1] == '--':
            listaDeMovimientosPosibles.append((fila - 2,columna - 1))
    return listaDeMovimientosPosibles

def movimientoCaballo2(tablero,f,c):
    listaDeMovimientosposibles = []
    if c >= 2 and c <= 5 and f >=1 and f <= 6:
        if tablero[f + 1][c + 2] == '--':
            listaDeMovimientosposibles.append((f + 1,c + 2))
        if tablero[f + 1][c - 2] == '--':
            listaDeMovimientosposibles.append((f + 1,c - 2))
        if tablero[f - 1][c + 2] == '--':
            listaDeMovimientosposibles.append((f - 1,c + 2))
        if tablero[f - 1][c - 2] == '--':
            listaDeMovimientosposibles.append((f - 1,c - 2))
    if f == 7 and (c >= 2 and c <= 5):
        if tablero[f - 1][c + 2] == '--':
            listaDeMovimientosposibles.append((f - 1,c + 2))
        if tablero[f - 1][c - 2] == '--':
            listaDeMovimientosposibles.append((f - 1,c - 2))
    if f == 0 and (c >= 2 and c <= 5):
        if tablero[f + 1][c + 2] == '--':
            listaDeMovimientosposibles.append((f + 1,c + 2))
        if tablero[f + 1][c - 2] == '--':
            listaDeMovimientosposibles.append((f + 1,c - 2))
    if f == 0 and (c == 0 or c == 1):
        if tablero[f + 1][c + 2] == '--':
            listaDeMovimientosposibles.append((f + 1,c + 2))
    if f == 7 and (c == 0 or  c == 1): 
        if tablero[f - 1][c + 2] == '--':
            listaDeMovimientosposibles.append((f - 1,c + 2))
    if f >= 1 and f <= 6 and (c == 0 or c == 1):
        if tablero[f + 1][c + 2] == '--':
            listaDeMovimientosposibles.append((f + 1,c + 2))
        if tablero[f - 1][c + 2] == '--':
            listaDeMovimientosposibles.append((f - 1,c + 2))
    if f == 0 and (c == 6 or c == 7):
        if tablero[f + 1][c - 2] == '--':
            listaDeMovimientosposibles.append((f + 1,c - 2))
    if f == 7 and (c == 6 or c == 7):
        if tablero[f - 1][c - 2] == '--':
            listaDeMovimientosposibles.append((f - 1,c - 2))
    return listaDeMovimientosposibles


def comeCaballoLArribaDerecha(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if tablero[fila][columna][1] == 'N':
        if fila >= 2 and columna <= 6:
            if tablero[fila - 2][columna + 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila - 2,columna + 1))
    elif tablero[fila][columna][1] == 'B':
        if fila >= 2 and columna <= 6:
            if tablero[fila - 2][columna + 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 2,columna + 1)) 
    return listaDeMovimientosPosibles


def comeCaballoAbajoDerecha(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if tablero[fila][columna][1] == 'N':
        if fila <= 5 and columna <= 6:
            if tablero[fila + 2][columna + 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 2,columna + 1))
    elif tablero[fila][columna][1] == 'B':
        if fila <= 5 and columna <= 6:
            if tablero[fila + 2][columna + 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila + 2,columna + 1)) 
    return listaDeMovimientosPosibles


def comeCaballoArribaIzquierda(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if tablero[fila][columna][1] == 'N':
        if fila >= 2 and columna >= 1:
            if tablero[fila - 2][columna - 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila - 2,columna - 1))
    elif tablero[fila][columna][1] == 'B':
        if fila >= 2 and columna >= 1:
            if tablero[fila - 2][columna - 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 2,columna - 1))
    return listaDeMovimientosPosibles


def comeCaballoAbajoIzquierda(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if tablero[fila][columna][1] == 'N':
        if fila <= 5 and columna >= 1:
            if tablero[fila + 2][columna - 1][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 2,columna - 1))
    elif tablero[fila][columna][1] == 'B':
        if fila <= 5 and columna >= 1:
            if tablero[fila + 2][columna - 1][1] == 'N':
                listaDeMovimientosPosibles.append((fila + 2,columna - 1))
    return listaDeMovimientosPosibles


def comeCaballoDerechaArriba(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if tablero[fila][columna][1] == 'N':
        if fila >= 1 and columna <= 5:
            if tablero[fila - 1][columna + 2][1] == 'B':
                listaDeMovimientosPosibles.append((fila - 1,columna + 2))
    elif tablero[fila][columna][1] == 'B':
        if fila >= 1 and columna <= 5:
            if tablero[fila - 1][columna + 2][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna + 2))
    return listaDeMovimientosPosibles


def comeCaballoDerechaAbajo(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if tablero[fila][columna][1] == 'N':
        if fila <= 6 and columna <= 5:
            if tablero[fila - 1][columna + 2][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna + 2))
    elif tablero[fila][columna][1] == 'B':
        if fila <= 6 and columna <= 5:
            if tablero[fila - 1][columna + 2][1] == 'N':
                listaDeMovimientosPosibles.append((fila + 1,columna + 2))  
    return listaDeMovimientosPosibles


def comeCaballoIzquierdaArriba(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if tablero[fila][columna] == 'N':
        if fila <= 6 and columna >= 2:
            if tablero[fila - 1][columna - 2][1] == 'B':
                listaDeMovimientosPosibles.append((fila - 1,columna - 2))
    elif tablero[fila][columna][1] == 'B':
        if fila <= 6 and columna >= 2:
            if tablero[fila - 1][columna - 2][1] == 'N':
                listaDeMovimientosPosibles.append((fila - 1,columna - 2)) 
    return listaDeMovimientosPosibles


def comeCaballoIzquierdaAbajo(tablero,fila,columna):
    listaDeMovimientosPosibles = []
    if tablero[fila][columna][1] == 'N':
        if fila <= 6 and columna >= 2:
            if tablero[fila + 1][columna - 2][1] == 'B':
                listaDeMovimientosPosibles.append((fila + 1,columna - 2))
    elif tablero[fila][columna][1] == 'B':
        if fila <= 6 and columna >= 2:
            if tablero[fila + 1][columna - 2][1] == 'N':
                listaDeMovimientosPosibles.append((fila + 1,columna - 2))
    return listaDeMovimientosPosibles


def movimientoCaballo(tablero,fila,columna):
    return movimientoCaballo1(tablero,fila,columna) + movimientoCaballo2(tablero,fila,columna) + \
            comeCaballoAbajoDerecha(tablero,fila,columna) + comeCaballoAbajoIzquierda(tablero,fila,columna) + \
             comeCaballoArribaIzquierda(tablero,fila,columna) + comeCaballoLArribaDerecha(tablero,fila,columna) + \
              comeCaballoDerechaAbajo(tablero,fila,columna) + comeCaballoDerechaArriba(tablero,fila,columna) + \
                  comeCaballoIzquierdaAbajo(tablero,fila,columna) + comeCaballoIzquierdaArriba(tablero,fila,columna)

# print(movimientoCaballo(tablero(),4,4))

def movimientoTorre (tablero,fila,columna):
    return movimientoHaciaAbajo(tablero,fila,columna) + \
            movimientoHaciaArriba(tablero,fila,columna) + \
             movimientoLateralDerecha(tablero,fila,columna) + \
              movimientoLateralIzquierda(tablero,fila,columna)
# print(movimientoTorre(tablero(),3,0))   

def movimientoAlfil(tablero,fila,columna):
    return movientodiagonalAbajoIzquierda(tablero,fila,columna) + \
            movientodiagonalArribaDerecha(tablero,fila,columna) + \
             movimientodiagonalAbajoDerecha(tablero,fila,columna) + \
              movimientodiagonalArribaIzquierda(tablero,fila,columna)   

# print(movimientoAlfil(tablero(),7,2))

def movimientoReina(tablero,fila,columna):
    return movimientoAlfil(tablero,fila,columna) + movimientoTorre(tablero,fila,columna)
# print(movimientoReina(tablero(),3,0))

def movimientoRey(tablero,fila,columna):
    listaDemovimientosPosibles = []
    if fila >= 1 and fila <= 6 and columna >= 1 and columna <= 6:
        if tablero[fila][columna][1] == 'N':
            if tablero[fila + 1][columna][1] != 'N':
                listaDemovimientosPosibles.append((fila + 1,columna))
            if tablero[fila - 1][columna][1] != 'N':
                listaDemovimientosPosibles.append((fila - 1,columna))
            if tablero[fila][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila,columna - 1))
            if tablero[fila][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila,columna + 1))
            if tablero[fila - 1][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila - 1,columna + 1))
            if tablero[fila - 1][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila - 1,columna - 1))
            if tablero[fila + 1][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila + 1,columna - 1))
            if tablero[fila + 1][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila + 1,columna + 1))
        elif tablero[fila][columna][1] == 'B':
            if tablero[fila + 1][columna][1] != 'B':
                listaDemovimientosPosibles.append((fila + 1,columna))
            if tablero[fila - 1][columna][1] != 'B':
                listaDemovimientosPosibles.append((fila - 1,columna))
            if tablero[fila][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila,columna - 1))
            if tablero[fila][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila,columna + 1))
            if tablero[fila - 1][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila - 1,columna + 1))
            if tablero[fila - 1][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila - 1,columna - 1))
            if tablero[fila + 1][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila + 1,columna - 1))
            if tablero[fila + 1][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila + 1,columna + 1))
    elif fila >= 1 and fila <= 6 and columna == 0:
        if tablero[fila][columna][1] == 'N':
            if tablero[fila][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila,columna + 1))
            if tablero[fila - 1][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila - 1,columna + 1))
            if tablero[fila + 1][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila + 1,columna + 1))
        elif tablero[fila][columna][1] == 'B':
            if tablero[fila][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila,columna + 1))
            if tablero[fila - 1][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila - 1,columna + 1))
            if tablero[fila + 1][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila + 1,columna + 1))
    elif fila >= 1 and fila <= 6 and columna == 7:
        if tablero[fila][columna][1] == 'N':
            if tablero[fila][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila,columna - 1))
            if tablero[fila + 1][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila + 1,columna - 1))
            if tablero[fila - 1][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila - 1,columna - 1))
        elif tablero[fila][columna][1] == 'B':
            if tablero[fila][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila,columna - 1))
            if tablero[fila + 1][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila + 1,columna - 1))
            if tablero[fila - 1][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila - 1,columna - 1))
    elif fila == 0 and columna >= 1 and columna <= 6:
        if tablero[fila][columna][1] == 'N':
            if tablero[fila][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila,columna - 1))
            if tablero[fila][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila,columna + 1))
            if tablero[fila + 1][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila - 1,columna - 1))
            if tablero[fila + 1][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila + 1,columna + 1))
        elif tablero[fila][columna][1] == 'B':
            if tablero[fila][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila,columna - 1))
            if tablero[fila][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila,columna + 1))
            if tablero[fila + 1][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila - 1,columna - 1))
            if tablero[fila + 1][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila + 1,columna + 1))
    elif fila == 7 and columna >= 1 and columna <= 6:
        if tablero[fila][columna][1] == 'N':
            if tablero[fila][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila,columna - 1))
            if tablero[fila][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila,columna + 1))  
            if tablero[fila - 1][columna - 1][1] != 'N':
                listaDemovimientosPosibles.append((fila - 1,columna - 1))
            if tablero[fila - 1][columna + 1][1] != 'N':
                listaDemovimientosPosibles.append((fila - 1,columna + 1))
        elif tablero[fila][columna][1] == 'B':
            if tablero[fila][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila,columna - 1))
            if tablero[fila][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila,columna + 1))  
            if tablero[fila - 1][columna - 1][1] != 'B':
                listaDemovimientosPosibles.append((fila - 1,columna - 1))
            if tablero[fila - 1][columna + 1][1] != 'B':
                listaDemovimientosPosibles.append((fila - 1,columna + 1))
    return listaDemovimientosPosibles
# print(movimientoRey(tablero(),4,4))
            

def jugadaPeon(tablero):
    fila0 = int(input("En que fila esta ese Peon : "))
    columna0 = int(input("En que columna esta ese Peon: "))
    color = tablero[fila0][columna0][1]
    if color == "N":
        print("Movimientos posibles: ",movimientoPeonInicial(tablero,fila0,columna0))
        fila = int(input("Siguiente fila:  "))
        columna = int(input("Siguiente columna :"))
        if (fila,columna) not in movimientoPeonInicial(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "PN"
    elif color == 'B':
        print("Movimientos posibles: ",movimientoPeonInicial(tablero,fila0,columna0))
        fila = int(input("A que fila la queres mover: "))
        columna = int(input("columna :"))
        if (fila,columna) not in movimientoPeonInicial(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "PB"
        
    return imprime_tablero(tablero)
# print(jugadaPeon(tablero()))
    
def jugadaAlfil(tablero):
    fila0 = int(input("En que fila esta esa pieza : "))
    columna0 = int(input("En que columna esta esa pieza: "))
    color = tablero[fila0][columna0][1]
    if color == "N":
        print("Movimientos posibles: ",movimientoAlfil(tablero,fila0,columna0))
        fila = int(input("Siguiente fila:  "))
        columna = int(input("Siguiente columna :"))
        if (fila,columna) not in movimientoAlfil(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "AN"
    elif color == 'B':
        print("Movimientos posibles: ",movimientoAlfil(tablero,fila0,columna0))
        fila = int(input("A que fila la queres mover: "))
        columna = int(input("columna :"))
        if (fila,columna) not in movimientoAlfil(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "AB"
        
    return imprime_tablero(tablero)

# print(jugadaAlfil(tablero()))               

def jugadaCaballo(tablero):
    fila0 = int(input("En que fila esta esa pieza : "))
    columna0 = int(input("En que columna esta esa pieza: "))
    color = tablero[fila0][columna0][1]
    if color == "N":
        print("Movimientos posibles: ",movimientoCaballo(tablero,fila0,columna0))
        fila = int(input("Siguiente fila:  "))
        columna = int(input("Siguiente columna :"))
        if (fila,columna) not in movimientoCaballo(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "CN"
    elif color == 'B':
        print("Movimientos posibles: ",movimientoCaballo(tablero,fila0,columna0))
        fila = int(input("A que fila la queres mover: "))
        columna = int(input("columna :"))
        if (fila,columna) not in movimientoCaballo(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "CB"
        
    return imprime_tablero(tablero)        
        
# print(jugadaCaballo(tablero()))      
 
def jugadaTorre(tablero):
    fila0 = int(input("En que fila esta esa pieza : "))
    columna0 = int(input("En que columna esta esa pieza: "))
    color = tablero[fila0][columna0][1]
    if color == "N":
        print("Movimientos posibles: ",movimientoTorre(tablero,fila0,columna0))
        fila = int(input("Siguiente fila:  "))
        columna = int(input("Siguiente columna :"))
        if (fila,columna) not in movimientoTorre(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "TN"
    elif color == 'B':
        print("Movimientos posibles: ",movimientoTorre(tablero,fila0,columna0))
        fila = int(input("A que fila la queres mover: "))
        columna = int(input("columna :"))
        if (fila,columna) not in movimientoTorre(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "TB"
        
    return imprime_tablero(tablero)        
        
# print(jugadaTorre(tablero()))  

def jugadaReina(tablero):
    fila0 = int(input("En que fila esta esa pieza : "))
    columna0 = int(input("En que columna esta esa pieza: "))
    color = tablero[fila0][columna0][1]
    if color == "N":
        print("Movimientos posibles: ",movimientoReina(tablero,fila0,columna0))
        fila = int(input("Siguiente fila:  "))
        columna = int(input("Siguiente columna :"))
        if (fila,columna) not in movimientoReina(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "RN"
    elif color == 'B':
        print("Movimientos posibles: ",movimientoReina(tablero,fila0,columna0))
        fila = int(input("A que fila la queres mover: "))
        columna = int(input("columna :"))
        if (fila,columna) not in movimientoReina(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "RB"
        
    return imprime_tablero(tablero)        
        
# print(jugadaReina(tablero()))      
             
def jugadaRey(tablero):
    fila0 = int(input("En que fila esta esa pieza : "))
    columna0 = int(input("En que columna esta esa pieza: "))
    color = tablero[fila0][columna0][1]
    if color == "N":
        print("Movimientos posibles: ",movimientoRey(tablero,fila0,columna0))
        fila = int(input("Siguiente fila:  "))
        columna = int(input("Siguiente columna :"))
        if (fila,columna) not in movimientoRey(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "KN"
    elif color == 'B':
        print("Movimientos posibles: ",movimientoRey(tablero,fila0,columna0))
        fila = int(input("A que fila la queres mover: "))
        columna = int(input("columna :"))
        if (fila,columna) not in movimientoRey(tablero,fila0,columna0):
            return "jugada invalida"
        else:
            tablero[fila0][columna0] ='--'
            tablero[fila][columna] = "KB"
        
    return imprime_tablero(tablero)



def posicionReyN(tablero):
    pos = ()
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == 'KN':
                pos += (i,j) 
    return pos            
# print(posicionReyN(tablero()))

def posicionReyB(tablero):
    pos = ()
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j] == 'KB':
                pos += (i,j) 
    return pos            
# print(posicionReyB(tablero()))

def Jaque(tablero,pieza,turno,fila,columna):
    if Turno(turno) == 'negro':
        if pieza == 'peon':
            if posicionReyB(tablero) in movimientoPeonInicial(tablero,fila,columna):
                return True
            return False
        elif pieza == 'alfil':
            if posicionReyB(tablero) in movimientoAlfil(tablero,fila,columna):
                return True
            return False
        elif pieza == 'caballo':
            if posicionReyB(tablero) in movimientoCaballo(tablero,fila,columna):
                return True
            return False
        elif pieza == 'reina':
            if posicionReyB(tablero) in movimientoReina(tablero,fila,columna):
                return True
            return False
        elif pieza == 'torre':
            if posicionReyB(tablero) in movimientoTorre(tablero,fila,columna):
                return True
            return False
        elif pieza == 'rey':
            if posicionReyB(tablero) in movimientoRey(tablero,fila,columna):
                return True
            return False
    elif Turno(turno) == 'blanco':
        if pieza == 'peon':
            if posicionReyN(tablero) in movimientoPeonInicial(tablero,fila,columna):
                return True
            return False
        elif pieza == 'alfil':
            if posicionReyN(tablero) in movimientoAlfil(tablero,fila,columna):
                return True
            return False
        elif pieza == 'caballo':
            if posicionReyN(tablero) in movimientoCaballo(tablero,fila,columna):
                return True
            return False
        elif pieza == 'reina':
            if posicionReyN(tablero) in movimientoReina(tablero,fila,columna):
                return True
            return False
        elif pieza == 'torre':
            if posicionReyN(tablero) in movimientoTorre(tablero,fila,columna):
                return True
            return False
        elif pieza == 'rey':
            if posicionReyN(tablero) in movimientoRey(tablero,fila,columna):
                return True
            return False

# print(Jaque(tablero(),'alfil',0,4,1)) -> True}

def PiezaAjugada(pieza:str,tablero):
    if pieza == 'peon':
        return jugadaPeon(tablero)
    elif pieza == 'alfil':
        return jugadaAlfil(tablero)
    elif pieza == 'caballo':
        return jugadaCaballo(tablero)
    elif pieza == 'reina':
        return jugadaReina(tablero)
    elif pieza == 'rey':
        return jugadaRey(tablero)
    elif pieza == 'torre':
        return jugadaTorre(tablero)

def HayunGanador(tablero):
    ganador = True
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            if tablero[i][j][0] == 'K':
                ganador = False
                return ganador
    return ganador
def juego():
    print('Bienvenidos al Ajedrez de Fran!')
    print('Este es el tablero en el que vamos a jugar')
    tableroActualizado = tablero()
    print(imprime_tablero(tableroActualizado))
    turno = 0
    TerminaJuego = False
    while not TerminaJuego:
        TurnoDeJugador = Turno(turno)
        print('Turno de color',TurnoDeJugador)
        pieza = str(input('Que pieza quieres mover (peon,alfil,caballo,reina,rey,torre): '))
        posX =int(input('en que fila esta esa pieza ?'))
        posY = int(input('en que columna esta esa pieza ?'))
        if piezas(pieza,TurnoDeJugador)[1] == tablero[posX][posY][1]:
            PiezaAjugada(pieza,tableroActualizado)
            if Jaque(tableroActualizado,pieza,turno,posX,posY):
                print('Jaque!')
            if HayunGanador(tableroActualizado):
                TerminaJuego = False
                return 'ganó el jugador' + Turno(turno)
            turno += 1
        else:
            print('jugada invalida')
            turno += 1        
print(juego())        
        
    