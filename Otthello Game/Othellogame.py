#-----------------------------------------------TRABAJO PRACTICO 1 PROGRAMACION-----------------------------------------------
#Integrantes del grupo: Tomas Benjamin Ferreyra y Franco Pierabella

#Como aclaracion, pensamos el codigo de manera que, en el archivo, cada linea contenga un espacio antes del \n.
#Ademas 
# 'Alejandro,B '
# 'B '
# 'A2 '

def tablero():
    return [ #no variables globales
 #    A   B   C   D   E   F   G   H 
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','X','-','-',],
    ['-','-','-','O','X','X','-','-',],
    ['-','-','-','X','O','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',],
    ['-','-','-','-','-','-','-','-',]
    ]

def sinUltimos3(listadeLineas: 'list') -> 'list':
    '''
    Esta funcion tomara una lista y a cada elemento le quitara los ultimos 3 caracteres
    '''
    ListaSinLosUltimoseCaracteres = []
    for palabra in listadeLineas:
        ListaSinLosUltimoseCaracteres += [palabra[0:len(palabra)-2]]
    return ListaSinLosUltimoseCaracteres[0:len(listadeLineas)]

def LineasInLista(archivo_origen :str) -> 'list':
    '''
    
    Esta funcion va a recibir el archivo y creara una lista, siendo cada elemento de la misma una linea del archivo (sin ' \n')
    '''
    archivo = open(archivo_origen,'r')
    lineas = []
    for linea in archivo.readlines():
        lineas += [linea]
    archivo.close()
    return sinUltimos3(lineas)


def LetraNumero(s: str) -> int:
    '''
    la funcion se encarga de pasar de la posicion x, expresada en letras, a la misma posicion
    pero expresada en numeros, lo que permite poder accedera a la posicion de tablero deseada
    '''
    letra = ord(s)
    if letra < 97:
        letra = letra - 64  
    else:
        letra = letra - 96 
    return letra


def opuesto(ficha:str) -> str:
    '''
    esta funcion va a recibir una ficha y va retornar en la ficha opuesta.
    '''
    return 'O' if ficha == 'X' else 'X'

def letraColor(ficha):
    '''
    Funcion que recibe 'B' o 'N' y devuelve 'O' y 'X' respectivamente.
    '''
    if ficha == 'B':
        return 'O'
    elif ficha == 'N':
        return 'X'
    else:
        return '-'
    # return 'O' if ficha == 'B' else 'X'

def strTupla(posicion:str,) -> 'tuple':
    '''
    Esta funcion toma la posicion a cambiar, la ficha que le corresponde y el tablero actual
    El return va a ser el nuevo estado (el tablero actualizado)
    '''
    posnX = int(LetraNumero(posicion[0])) - 1
    posnY = int(posicion[1]) - 1
    return (posnY,posnX)

def extremo(posnY,posnX):
    return posnY < 8 and posnY > -1 and posnX < 8 and posnX > -1

def imprimir_tablero(tablero:'list') -> str:
    '''
    funcion para imprimir tablero
    '''
    for i in tablero:
        print(i)

def turno(Tinicial:str,cantTurnos:int) -> str:
    '''
    Funcion que va a tomar el turno inicial, la cantidad de turnos que ya se jugaron
    y va a devolver el color que le corresponde al turno actual.
    '''
    par_impar = cantTurnos % 2
    fichas1 = ['O','X']
    fichas2 = ['X','O']
    if Tinicial == 'B':
        #turnos impares a los lancos y pares a los negros.
        return fichas1[par_impar]
    else: #Tinicial == 'N'
        #turnos pares a los blancos e impares a los negros.
        return fichas2[par_impar]

def filtro(listatup):
    '''
    Funcion que toma una lista de tuplas y retorna en una nueva lista sin las tuplas que contentan un -1 en el interior.
    '''
    nuevalista = []
    for i in listatup:
        if i[0] != -1 and i[1] != -1:
            nuevalista += [i]
    return nuevalista

def verificaLados(posnY: int, posnX: int, tablero: list, ficha):
    '''
    funcion que va a verificar si a los lados de la ficha que se quiere jugar tienen 
    fichas de diferente color.
    '''
    lista = [(posnY,posnX)]
    for i in range(-1,2):
        for j in range(-1,2):
            if posnY + i < 8 and posnX + j < 8:
                if tablero[posnY + i][posnX + j] == ficha:
                    lista = lista
                elif tablero[posnY + i][posnX + j] != ficha:
                    if tablero[posnY + i][posnX + j] != '-':
                        lista += [(posnY + i,posnX + j)]    
            elif posnY + i >= 8 and posnX + j < 8:
                if tablero[posnY][posnX + j] == ficha:
                    lista = lista
                elif tablero[posnY][posnX + j] != ficha:
                    if tablero[posnY][posnX + j] != '-':
                        lista += [(posnY,posnX + j)]   
            elif posnY + i < 8 and posnX + j >= 8:
                if tablero[posnY + i][posnX] == ficha:
                    lista = lista
                elif tablero[posnY + i][posnX] != ficha:
                    if tablero[posnY + i][posnX] != '-':
                        lista += [(posnY + i,posnX)] 
            else:
                if tablero[posnY][posnX] == ficha:
                    lista = lista
                elif tablero[posnY][posnX] != ficha:
                    if tablero[posnY][posnX] != '-':
                        lista += [(posnY,posnX)] 
    return filtro(lista)

def paso(cord1,cord2):
    '''
    Funcion que recibe una coordenada origen y otra coordenada destino, la funcion nos devolvera
    lo que hay que sumarle a la coordenada origen para llegar a la destino.
    '''
    return (cord2[0]-cord1[0],cord2[1]-cord1[1])

def verifica_cond3(listadePosibles: 'list', tablero:'list',ficha):
    '''
    Funcion que recibe una lista filtrada por la funcion validaLados, el tablero actual y la ficha que le corresponde al turno
    va a ir iterando la lista y a cada elemento de la misma le va a aplicar la funcion paso, para con esta informacion
    poder 'seguir' la traza actual hasta llegar a una ficha con el mismo color que la origen.
    '''
    listadePosiblesN = listadePosibles[1:] #lista des posibles a dar vuelta sin la coordenada origen
    Origen = listadePosibles[0] # coordenada origen 
    listaAdarVuelta = [Origen] # esta lista va a guardar todas las posiciones a dar vuelta
    for i in (range(len(listadePosiblesN))):
        pasoAux = paso(Origen,listadePosiblesN[i])# 0,1 . 1,-1 . etc
        posAux = (Origen[0] + pasoAux[0], Origen[1] + pasoAux[1])
        listaAux = []
        mismaFicha = []
        while extremo(posAux[0],posAux[1]) and tablero[posAux[0]][posAux[1]] != '-' and len(mismaFicha) < 1:
            listaAux += [posAux]#---  
            if tablero[posAux[0]][posAux[1]] == opuesto(ficha):
                listaAux += [posAux]      
            elif tablero[posAux[0]][posAux[1]] == ficha:
                mismaFicha += [1]
                listaAux += [posAux]   
            posAux = (posAux[0] + pasoAux[0] , posAux[1] + pasoAux[1])
        listaAuxU = listaAux[-1]
        if ficha == tablero[listaAuxU[0]][listaAuxU[1]]:
            listaAdarVuelta = listaAdarVuelta + listaAux
    return listaAdarVuelta

def darVuelta(aDarVuelta:'list',tablero,ficha):
    '''
    Funcion que recibe una lista con coordenadas del tablero que tiene que asignarle el valor ficha
    '''
    for i in range(len(aDarVuelta)):
        tablero[aDarVuelta[i][0]][aDarVuelta[i][1]] = ficha
    return tablero

def jugadaActual1(listadeJugadas,turnoActual):
    '''
    Funcion que toma la lista de jugadas, el turno actual y determina la jugada actual
    '''
    return listadeJugadas[turnoActual]
# imprimir_tablero(darVuelta([(0,0),(1,1),(7,7),(0,7)], tablero(), 'X'))

def cantElementos(lista:'list'):
    '''
    Funcion que verifica que la una lista tenga mas de un elemento.
    '''
    cantidadElementos = len(lista)
    return cantidadElementos > 2

def verifica(jugadaActual,turnoInicial,turnoActual,tableroActual):
    return verifica_cond3( (verificaLados ( strTupla(jugadaActual)[0],strTupla(jugadaActual)[1],tableroActual,turno(turnoInicial,turnoActual))),tableroActual,turno(turnoInicial,turnoActual) )

#darVuelta(verifica_cond3(verificaLados(strTupla('A1')[0],strTupla('A1')[1],tablero(),turno(tinicial,tactual))), tablero(),turno(tinicial,tactual))

def valida(jugadaActual: str) -> bool:
    if jugadaActual != '':
        pos = strTupla(jugadaActual)
        posnY = pos[0] 
        posnX = pos[1]
        return posnX <= 8 and posnX > -1 and posnY <= 8 and posnY > -1
    else:
        return False
def tableroLleno(tableroActual: 'list') -> bool:
    '''
    funcion que toma un tablero y verifica si todos los elementos de las 7 filas tienen elementos no vacios (not elemento == '-')
    '''
    FichasX = 0
    FichasO = 0
    for Filas in tableroActual:
        for elemento in Filas:
            if elemento == 'X':
                FichasX += 1
            elif elemento == 'O':
                FichasO += 1
    return FichasO + FichasX == 64

def contadorDeFichas(tableroActual: 'list') -> str:    
    '''
    funcion que toma un tablero y cuenta la cantidad de fichas de cada color y retorna en cual de los colores tiene mas fichas, en
    caso de empate retornara a un '-'
    '''
    FichasO = 0
    FichasX = 0
    for Filas in tableroActual:
        for elemento in Filas:
            if elemento == 'X':
                FichasX += 1
            elif elemento == 'O':
                FichasO += 1
    if FichasO > FichasX:
        return 'O'
    elif FichasO < FichasX:
        return 'X'
    else:
        return '-'
# def main(archivo_origen: str) -> str:
#     '''
#     Funcion principal del juego.
#     La funcion main va a recibir un directorio el cual es un archivo con una partida hecha del juego othello
#         la funcion con los datos que reciba dentro del archivo simulara una partida devolviendonos el tablero y,
#         si es que lo hay, el ganador del juego
#     '''
#     Archivo = open(archivo_origen, 'r')
#     tableroActual:'list' = tablero() #variable que va a ir actualizando el tablero a medida que avanza el juego.
#     ListadeLineas = LineasInLista(archivo_origen) #variable que contiene en una lista todas las lineas del archivo en forma de listas.
#     jugador1:str = ListadeLineas[0][:len(ListadeLineas[0])-2] #Nombre del jugador 1, sin  ,'color
#     colorJugador1:str = letraColor(ListadeLineas[0][len(ListadeLineas[0])-1:]) #Color que le corresponde al jugador 1, pasado o a X o a O
#     jugador2:str = ListadeLineas[1][:len(ListadeLineas[1])-2] #Nombre del jugador 2, sin  ,'color
#     colorJugador2:str = letraColor(ListadeLineas[1][len(ListadeLineas[1])-1:]) #Color que le corresponde al jugador 1, pasado o a X o a O
#     turnoInicial:str = ListadeLineas[2] #Color que inicia el juego.
#     lista_de_jugadas:'list' = ListadeLineas[3:] #Lista que contiene todas las jugadas que estan escritas en el archivo.
#     turnoActual:int = 0 #Variable que va a ir actualizando el turno actual del juego
#     jugadaActual:str = jugadaActual1(lista_de_jugadas, turnoActual) #Esta variable recibe la lista de jugadas y el turno actual y devuelve la jugada actual
#     terminaJuego:bool = False 
#     jugadaIncorrecta = False
#     lista_de_jugadas2 = lista_de_jugadas # variable que me sirve para ir borrando elementos del archivo
#     Archivo.close()
#     while terminaJuego == False and len(lista_de_jugadas2) >= 1:#cambie esto-------------------------------------------
#         print(jugadaActual)
#         if not turnoActual < len(lista_de_jugadas) :
#             terminaJuego = True
#         elif tableroLleno(tableroActual):
#             terminaJuego = True
        
#         elif valida(jugadaActual) and cantElementos(verifica(jugadaActual,turnoInicial,turnoActual,tableroActual)):
#             lista_de_jugadas2 = lista_de_jugadas2[1:]
#             tableroActual = darVuelta(verifica(jugadaActual,turnoInicial,turnoActual,tableroActual), tableroActual, turno(turnoInicial, turnoActual) )
#             jugadaActual = jugadaActual1(lista_de_jugadas,turnoActual + 1)
#             turnoActual += 1         
#         elif not cantElementos(verifica(jugadaActual,turnoInicial,turnoActual,tableroActual)):
#             terminaJuego = True
#             jugadaIncorrecta = True
#     if terminaJuego == True or len(lista_de_jugadas2) >= 1:#cambie esto-------------------------------------------
#         if tableroLleno(tableroActual) == True:
#             if contadorDeFichas(tableroActual) == colorJugador1:
#                 imprimir_tablero(tableroActual)
#                 print(jugador1 + ' ha ganado el juego')
#             elif contadorDeFichas(tableroActual) == colorJugador2:
#                 imprimir_tablero(tableroActual)
#                 print(jugador2 + ' ha ganado el juego')
#             else: 
#                 imprimir_tablero(tableroActual)
#                 print(jugador1 + jugador2 + ' han empatado el juego')
#         else:
#             if jugadaIncorrecta == True:
#                 if turno(turnoInicial,turnoActual) == colorJugador1:
#                     imprimir_tablero(tableroActual)
#                     print(jugador1 + ' ha hecho una jugada incorrecta')
#                 else:
#                     imprimir_tablero(tableroActual)
#                     print(jugador2 + ' ha hecho una jugada incorrecta')
#             else:
#                 if contadorDeFichas(tableroActual) == colorJugador1:
#                     imprimir_tablero(tableroActual)
#                     print(jugador1 + ' ha ganado el juego')
#                 elif contadorDeFichas(tableroActual) == colorJugador2:
#                     imprimir_tablero(tableroActual)
#                     print(jugador2 + ' ha ganado el juego')
#                 else: 
#                     imprimir_tablero(tableroActual)
#                     print(jugador1 + ' y ' +  jugador2 + ' han empatado el juego')
    
#     Archivo.close()

# main('archivo.txt')

#los casos de prueba no me funcionaron en mi pc, pero en la de mi compañero si, perdonen las molestias.

