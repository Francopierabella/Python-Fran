def inicializaTablero() -> 'list':
    tablero = []
    for i in range(3):
        tablero.append(([' '] * 3))
    return tablero


def muestraTablero(tablero: 'list') -> None:
    for fila in tablero:
        print(fila[0], '|', fila[1], '|', fila[2])


def coordValida(c: int) -> bool:
    return c > 0 and c < 4
        
def ingresaCoord(orientacion: str) -> int:
    coord = int(input('Ingrese una ' + orientacion + ' (de 1 a 3)'))
    
    while (not coordValida(coord)):
        print ('La ' + orientacion + ' ingresada no es válida')
        coord = int(input('Ingrese una ' + orientacion + ' (de 1 a 3)'))
    
    return coord-1      # restamos 1 para obtener un número de 0 a 2
    

def ingresaJugada(tablero: 'list', ficha: str) -> None:
    print('Ingrese su jugada')
    jugadaValida = False

    while  not jugadaValida:
        fila = ingresaCoord('fila')
        columna = ingresaCoord('columna')
        
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = ficha
            mensaje = 'Su jugada ha sido realizada'
            jugadaValida = True
        else:
            mensaje = 'La casilla elegida está ocupada'
        
        print(mensaje)


def checkFila(i: int, tablero: 'list') -> bool:
    return tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != ' '

def checkColumna(i: int, tablero: 'list') -> bool:
    return tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != ' '

def checkDiag(tablero: 'list') -> bool:
    return tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != ' '

def checkDiagInv(tablero: 'list') -> bool:
    return tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[2][0] != ' '


def validaGanador(tablero: 'list') -> bool:
    hayUnGanador = False
    tamanio = len(tablero)
    i = 0

    while i < tamanio and not hayUnGanador:
        hayUnGanador = checkFila(i,tablero) or checkColumna(i,tablero)
        i += 1
    
    if not hayUnGanador:
            hayUnGanador = checkDiag(tablero) or checkDiagInv(tablero)
    
    return hayUnGanador


def jugar() -> None:
    print('Bienvenido al juego del Ta-Te-Ti')
    tableroTaTeTi = inicializaTablero()
    jugadaNumero = 0
    hayUnGanador = False
    ficha = ['X', 'O']

    while jugadaNumero < 9 and not hayUnGanador:
        muestraTablero(tableroTaTeTi)        
        ingresaJugada(tableroTaTeTi, ficha[jugadaNumero % 2])
        jugadaNumero += 1
        
        if jugadaNumero >= 5:
            hayUnGanador = validaGanador(tableroTaTeTi)
            
    if hayUnGanador:
        print('Felicitaciones ha ganado jugador', (jugadaNumero-1) % 2 +1)
        muestraTablero(tableroTaTeTi)
    else:
        print('La partida ha finalizado en empate')
        
        
        
jugar()
        
