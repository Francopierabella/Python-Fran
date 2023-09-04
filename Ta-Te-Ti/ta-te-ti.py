def inicializaTablero1():
    return [' '] * 9

def inicializaTablero2():
    return [' ' for x in range(9)]


def inicializaTablero3():
    tablero = []
    i = 0
    while i < 9:
        tablero += [' ']
        i = i + 1
    return tablero


def muestraTablero1(tablero):
    for i in [0,3,6]:
        print(tablero[i], '|', tablero[i+1], '|', tablero[i+2])

def muestraTablero2(tablero):
    i = 0
    tamanio = len(tablero)
    while i < tamanio:
        print(tablero[i], '|', tablero[i+1], '|', tablero[i+2])
        i += 3

        
def ingresaJugada(tablero, ficha):
    print('Ingrese su jugada')
    jugadaValida = False
    while  not jugadaValida:
        mensaje = ''
        fila = int(input('Ingrese una fila (de 1 a 3):'))
        if fila > 3 or fila < 1:
            mensaje = 'La fila ingresada no es válida'
        else:            
            columna = int(input('Ingrese una columna (de 1 a 3):'))
            if columna > 3 or columna < 1:
                mensaje = 'La columna ingresada no es válida'
        if mensaje == '':
            posicionElegida = (fila-1)*3+(columna-1)
            if tablero[posicionElegida] == ' ':
                tablero[posicionElegida] = ficha
                mensaje = 'Su jugada ha sido realizada'
                jugadaValida = True
            else:
                mensaje = 'La casilla elegida está ocupada'
        print(mensaje)

def validaGanador(tablero):
    hayUnGanador = False
    tamanio = len(tablero)
    i = 0
    while i < tamanio and not hayUnGanador:
        if tablero[i] == tablero[i+1] == tablero[i+2] and tablero[i] != ' ':
            hayUnGanador = True
        if tablero[i//3] == tablero[3+(i//3)] == tablero[6+(i//3)] and tablero[i//3] != ' ':
            hayUnGanador = True
        i += 3
    if not hayUnGanador and \
       (tablero[0] == tablero[4] == tablero[8] and tablero[0] != ' ') or \
       (tablero[2] == tablero[4] == tablero[6] and tablero[2] != ' '):
            hayUnGanador = True
    return hayUnGanador



def jugar():
    print('Bienvenido al juego del Ta-Te-Ti')
    tableroTaTeTi = inicializaTablero1()
    jugadaNumero = 0
    hayUnGanador = False
    ficha = ['X', 'O']
    while jugadaNumero < 9 and not hayUnGanador:
        muestraTablero1(tableroTaTeTi)        
        ingresaJugada(tableroTaTeTi, ficha[jugadaNumero % 2])
        jugadaNumero += 1
        if jugadaNumero >= 5:
            hayUnGanador = validaGanador(tableroTaTeTi)
            if hayUnGanador:
                print('Felicitaciones ha ganado jugador', (jugadaNumero-1) % 2 +1)
                muestraTablero1(tableroTaTeTi)
    if not hayUnGanador:
        print('La partida ha finalizado en empate')


jugar()
        
        
