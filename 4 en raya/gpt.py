def crear_tablero():
    return [[" " for _ in range(7)] for _ in range(6)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 21)

def hacer_movimiento(tablero, columna, jugador):
    for fila in reversed(range(6)):
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador
            return True
    return False

def verificar_victoria(tablero, jugador):
    # Verificar horizontalmente
    for fila in range(6):
        for columna in range(4):
            if tablero[fila][columna] == jugador and \
               tablero[fila][columna + 1] == jugador and \
               tablero[fila][columna + 2] == jugador and \
               tablero[fila][columna + 3] == jugador:
                return True

    # Verificar verticalmente
    for fila in range(3):
        for columna in range(7):
            if tablero[fila][columna] == jugador and \
               tablero[fila + 1][columna] == jugador and \
               tablero[fila + 2][columna] == jugador and \
               tablero[fila + 3][columna] == jugador:
                return True

    # Verificar diagonalmente (de izquierda a derecha)
    for fila in range(3):
        for columna in range(4):
            if tablero[fila][columna] == jugador and \
               tablero[fila + 1][columna + 1] == jugador and \
               tablero[fila + 2][columna + 2] == jugador and \
               tablero[fila + 3][columna + 3] == jugador:
                return True

    # Verificar diagonalmente (de derecha a izquierda)
    for fila in range(3):
        for columna in range(3, 7):
            if tablero[fila][columna] == jugador and \
               tablero[fila + 1][columna - 1] == jugador and \
               tablero[fila + 2][columna - 2] == jugador and \
               tablero[fila + 3][columna - 3] == jugador:
                return True

    return False

def jugar_cuatro_en_raya():
    tablero = crear_tablero()
    jugador_actual = "X"
    jugadas_restantes = 42

    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugador_actual}")
        columna = int(input("Elija una columna (0-6): "))

        if columna < 0 or columna > 6:
            print("Columna no válida. Elija una columna entre 0 y 6.")
            continue

        if hacer_movimiento(tablero, columna, jugador_actual):
            jugadas_restantes -= 1
            if verificar_victoria(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡El jugador {jugador_actual} ha ganado!")
                break
            elif jugadas_restantes == 0:
                imprimir_tablero(tablero)
                print("¡El juego ha terminado en empate!")
                break
            jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Columna llena. Elija otra columna.")

if __name__ == "__main__":
    jugar_cuatro_en_raya()
