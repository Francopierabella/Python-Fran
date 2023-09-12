'''
La cuadrícula de Sudoku consiste en espacios de 9x9.
Solo se pueden usar números del 1 al 9.
Cada bloque de 3x3 solo puede contener números del 1 al 9.
Cada columna vertical solo puede contener números del 1 al 9.
Cada fila horizontal solo puede contener números del 1 al 9.
Cada número del bloque de 3x3, de la columna vertical o de la fila horizontal solo se puede utilizar una vez.
El juego finaliza cuando toda la cuadrícula de Sudoku se completa correctamente con los números.
'''


def tablero():
  return  [['7','3','4','1','2','6','9','8','5'],
           ['-','8','6','-','2','-','-','-','2'],
           ['5','1','2','-','-','-','3','-','7'],
           ['3','-','-','-','-','-','-','-','4'],
           ['-','-','-','-','-','-','-','-','3'],
           ['-','-','-','-','-','-','-','-','1'],
           ['-','-','-','-','-','-','-','-','8'],
           ['-','-','-','-','-','-','-','-','9'],
           ['-','-','-','-','4','-','-','-','6']]
# Numeros posibles etc

def imprime_tablero(tablero:list):
    for i in tablero:
        print(i)
def Posible(filaCoolumna):
  return True if filaCoolumna >= 0 and filaCoolumna <= 9 else False
def bloque(tablero:list,fila,desde,hasta):
  b1 = tablero[fila][desde:hasta]
  b2 = tablero[fila + 1][desde:hasta]
  b3 = tablero[fila + 2][desde:hasta]
  return b1,b2,b3
# imprime_tablero(bloque(tablero(),0,0,3))
def estaEnbloque(tablero,numero,fila,desde,hasta):
  for i in range(3):
    if numero in bloque(tablero,fila,desde,hasta)[i]:
      return True
  return False
print(estaEnbloque(tablero(),'4',0,3,6))
def desdeyhasta(columna):
  desde = 0
  hasta = 0
  if columna < 3:
    desde = 0
    hasta =  3
    return [desde,hasta]
  elif columna >= 3  and columna < 6:
    desde = 3
    hasta = 6
    return [desde,hasta]
  elif columna >= 6 and columna < 9:
    desde = 6
    hasta = 9
    return [desde,hasta]


def tableroColumna(tablero,columna):
  tabCol = []
  for i in range(9):
    tabCol.append(tablero[i][columna])
  return tabCol
# print(tableroColumna(tablero(),4))
def tableroFila(tablero,fila):
  tabFila = []
  for i in range(9):
    tabFila.append(tablero[fila][i])
  return tabFila
# print(tableroFila(tablero(),4))
def PosicionValida(tablero,fila,columna,numero):
  if Posible(fila) and Posible(columna):
    if tablero[fila][columna] == '-':
      if numero not in tableroFila(tablero,fila) and numero not in tableroColumna(tablero,columna) \
        and numero not in bloque(tablero,fila,desdeyhasta(columna)[0],desdeyhasta(columna)[1]):
            return True
  return False
# print(PosicionValida(tablero(),0,4,'7'))

def EstaEnFilaOColumna(tablero,fila,columna,numero):
    cantidad = 0
    for i in tableroFila(tablero,fila):
        if i == numero:
            cantidad +=1
    for j in tableroColumna(tablero,columna):
        if j == numero:
            cantidad +=1
    return cantidad >= 1

# print(EstaEnFilaOColumna(tablero(),'8',1,3))



def jugada(tablero:list):
    fila = int(input("Fila (1-9): "))
    columna = int(input("Columna (1-9): "))
    numero = str(input("Que numero (1-9) quieres colocar en la posicion " + str((fila,columna))+ ':'))
    if PosicionValida(tablero,fila,columna,numero):
        tablero[fila][columna] = numero
    else:
        print("Posicion invalida")
        fila = int(input("Fila: "))
        columna = int(input("Columna: "))
        numero = str(input("Que numero quieres colocar en la posicion ",(fila,columna),": "))
    return imprime_tablero(tablero)

# print(jugada(tablero()))

# print(EstaEnFilaOColumna(tablero(),6,0,'9') or estaEnbloque(tablero(),'9',6,0,3))
def ganador(tablero):
    valor = True
    for i in tablero:
        for j in i:
            if j != '-':
                valor = True
            valor = False
    return valor
# print(ganador(tablero()))
def sudoku():
    tableroActualizado = tablero()
    terminaJuego = False
    print("BIENVENIDOS AL SUDOKU!")
    print("ESTE ES EL TABLERO A RELLENAR")
    print(imprime_tablero(tableroActualizado))
    print("A JUGAR!")
    while not terminaJuego:
        jugada(tableroActualizado)
        if ganador(tableroActualizado):
            terminaJuego = True
            print ("GANASTE!")
        
sudoku()







































