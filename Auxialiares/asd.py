# def SiguientesposicionesValidas(tablero:list,fila,columna,piezas,orientacion): 
#     listaDePosibles = []
#     if fila >= 0 and fila <= 7 and columna >= 0 and columna <= 6:
#         if piezas == 2:
#             if orientacion == 'Horizontal':
#                 if fila >=1 and fila <= 6 and columna >= 1 and columna <= 5:
#                     if tablero[fila][columna + 1] == '-':
#                         listaDePosibles.append((fila,columna + 1))
#                     if tablero[fila][columna - 1] == '-':
#                         listaDePosibles.append((fila,columna - 1))
#                 elif fila == 0 or fila == 7:
#                     if columna == 0:
#                         if tablero[fila][columna + 1] == '-':
#                             listaDePosibles.append((fila,columna + 1))
#                     elif columna == 6:
#                         if tablero [fila][columna - 1] == '-':
#                             listaDePosibles.append((fila,columna - 1))
#                     else:
#                         if tablero[fila][columna + 1] == '-':
#                             listaDePosibles.append((fila,columna + 1))
#                         if tablero[fila][columna - 1] == '-':
#                             listaDePosibles.append((fila,columna - 1))
#                 elif columna == 0:
#                     if tablero[fila][columna + 1] == '-':
#                         listaDePosibles.append((fila,columna + 1))
#                 elif columna == 6:
#                     if tablero[fila][columna - 1]== '-':
#                         listaDePosibles.append((fila,columna - 1))
#     return listaDePosibles

# print(SiguientesposicionesValidas(TableroJugador1(),1,2,2,'horizontal'))
                    
                    
l = [((1,2),(1,3)),((5,3),(5,4))]
laux = []
for i in range(len(l)):
    for j in l[i]:
        laux.append(j)
print(laux)

print((1,2) in l[0])

polla = [(4, 3), (5, 3), (6, 3), (2, 3), (1, 3), (0, 3)]
print((4,3) in polla)

asfa = [(5,2),(7,2)]
print((7,2) in asfa)