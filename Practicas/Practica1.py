# Ejercicio 1: Imprimir los primeros 25 numeros pares    
def f1(s):
    if s <= 25:
        print(s)
        f1(s+1)
f1(0)
# #---------------------------------------------------
# #Ejercicio 2: Escriba un programa que imprima los primeros 100 números naturales pares)
def f2(s = 0,m = 200):
    if s < m:
        if s % 2 == 0:
            print (s)
        else:return f2(s+1,m)
    
f2()
# #EXTRA
# #Imprime los primeros N pares
# def ImprimeNPares(n):
#     for i in range(0,n,2):
#         print (i)
# ImprimeNPares(20)
# # Ejercicio 3: Imprima los primeros n numeros pares mayores que M.
# def imprimeNparesHastaM(n,m):

#     if(n > m):
#         for i in range (0,n,2):
#             if i > m:
#                 print(i)
#     else:
#         print("N tiene que ser mayor que M")
        
# imprimeNparesHastaM(5,10)
# #Ejercicio 4y 5.Escriba un programa que calcule e imprima el 
# # resultado de la suma de los primeros 50 números naturales 
# # usando una función recursiva

def suma50numsnat(n):
    suma = 0
    if n == 0:
        return 0
    else:
        suma = n + (suma50numsnat (n - 1))
        return suma

print(suma50numsnat(50))
        
# #Ejercicio 6: imprima el resultado de la suma de los primeros numeros naturlaes
# # mayores que n y menores que m 
def sumaDenumerosNyM(n,m):
    suma = 0
    if  n == m:
        return 0
    else:
        if n < m:
            suma = n + (sumaDenumerosNyM(n+1,m))
            return suma

print(sumaDenumerosNyM(-105,105))
# # Ejercicio 7:Escriba un programa que reciba un nombre y
# # retorne el nombre pasado concatenado 2 veces.
# def concatenaNombres (nombre):
#     concatenado = nombre * 2
#     print(concatenado)
# concatenaNombres("Franco")
# #Ejercicio 8: El 7 pero n veces
# def concatenaNvecesNombre (nombre,veces):
#     concatenado = nombre * veces
#     print(concatenado)
# concatenaNvecesNombre("Franco",4)

# #Ejercio 9:
#     # a) funcion suma:
# def suma (a,b):
#     resultado = a + b
#     print(resultado)
# suma(1,2)
#     # b) resta:
# def resta (x,y):
#     resultado = x - y
#     print(resultado)
# resta(2,1)
#     # c) Producto:
# def producto (q,w):
#     resultado = q * w
#     print(resultado)
# producto(2,3)
#     # d) Division
# def division (p,r):
#     resultado = p / r
#     print(resultado)
# division(4,2)
    # e) Elegir
# def operaciones():
#     operacion = int(input("Que operacion eliges: 1.Suma 2.Resta 3.Producto 4.Division: "))
#     if operacion == 1:
#         sumando1 = int(input("Sumando1:"))
#         sumando2 = int(input("Sumando2: "))
#         resultado = sumando1 + sumando2
#         print(resultado)
#     elif operacion == 2:
#         minuendo = int(input("Minuendo:"))
#         sustraendo = int(input("Sustraendo:"))
#         resultado = minuendo - sustraendo
#         print(resultado)
#     elif operacion == 3:
#         factor1 = int(input("Factor1:"))
#         factor2 = int(input("Factor2:"))
#         resultado = factor1 * factor2
#         print(resultado)
#     elif operacion == 4:
#         dividendo = int(input("Dividendo:"))
#         divisor = int(input("Divisor:"))
#         resultado = dividendo / divisor
#         print(resultado)

# operaciones()
#     # f) agregarle una opcion salir. Preguntar si es con while.
# def operaciones2():
#     operacion = int(input("Que operacion eliges: 1.Suma 2.Resta 3.Producto 4.Division 5.Salir: "))
#     if operacion == 1:
#             sumando1 = int(input("Sumando1:"))
#             sumando2 = int(input("Sumando2: "))
#             resultado = sumando1 + sumando2
#             print(resultado)
#             operaciones2()
            
#     elif operacion == 2:
#             minuendo = int(input("Minuendo:"))
#             sustraendo = int(input("Sustraendo:"))
#             resultado = minuendo - sustraendo
#             print(resultado)
#             operaciones2()
            
#     elif operacion == 3:
#             factor1 = int(input("Factor1:"))
#             factor2 = int(input("Factor2:"))
#             resultado = factor1 * factor2
#             print(resultado)
#             operaciones2()
            
#     elif operacion == 4:
#             dividendo = int(input("Dividendo:"))
#             divisor = int(input("Divisor:"))
#             resultado = dividendo / divisor
#             print(resultado)
#             operaciones2()
    
#     elif operacion == 5:
#            print("Calculadora Cerrada")

# operaciones2()
           
            
      





