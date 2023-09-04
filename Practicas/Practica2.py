# Bucles for y while
# Ejercicio 1:"Escriba un ciclo definido para imprimir por pantalla todos los números entre 10 y 20."
# def imprime1020():
#     for i in range (10,21):
#         print (i)
# imprime1020()
# Ejercicio 2: imprime fichas domino
# 0-0.1-0,1-1,2-0-2-1,2-2...
# def domino ():
#     for i in range(0,7):
#         for j in range(0,7):
#             print(i,"-",j)
# domino()
# # Ejercicio 3: Lo  mismo pero de 0 hasta n

# def Nfichas (n):
#     for i in range(0,n + 1):
#         for j in range (0, n + 1):
#             print(i,":",j)
# Nfichas(6)

# Ejercicio 4: Escriba una función que tome una cantidad m de valores
# que serán ingresados por el usuario y, a medida que se ingresa cada número,
# muestre el factorial del mismo. El valor de m es ingresado inicialmente por el usuario

# def factorial (n):
#     if (n == 0) or (n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# def calculaFactorial ():
#     m = int(input("Ingrese una cantidad de valores: "))
#     for i in range(m):
#         numero = int(input("ingrese un numero: "))
#         resultado = factorial(numero)
#         print("El factorial de",numero, "es",resultado)

# calculaFactorial()

#Ejercio 5 y 6:

# Ejercicio 6: numeros triangulares: 1-1,2-3,3-6...
def sumahastan(n):
    suma = 0
    for i in range(n):
        suma += i
    return suma
def numerosTriangulares(n):
    for i in range(1,n+1):
        aux = sumahastan(i)
        nro2 = i + aux
        print(i,"-",nro2)    
numerosTriangulares(5)


#Bucles while

# Ejercicio 1:Escriba una función que le pida al usuario que ingrese un número positivo.
#Si el usuario ingresa cualquier cosa que no sea lo pedido se le debe informar de su error mediante
#un mensaje y volver a pedirle el número,repitiendo este proceso hasta que ingrese lo pedido.

# def ingreseNumeroPositvo():
#     valor = False
#     while not valor:
#         ingreso = int(input("Ingrese un numero Positivo: "))
#         if ingreso > 0:
#             valor = True
#         else:
#             print("ingrese un numero positivo por favor")
#             ingreso = int(input("Ingrese un numero Positivo: ")) 

# ingreseNumeroPositvo()
# Funciona medio raro

# Ejercicio8. Usuario ingresa notas y le vas preguntando si desea
# poner mas notas. Al finalizar impprime el promedio de las notas

# def promedioNotas ():
#     sumaDeNotas = 0
#     cantidadDeNotas = 0
#     valor = True
#     while valor:
#         nota = int(input("ingrese una nota o -1 para finalizar: "))
#         if nota != -1:
#             cantidadDeNotas += 1
#             sumaDeNotas += nota
#             promedio = sumaDeNotas / cantidadDeNotas
#         else:
#             valor = False
#     print(promedio)
# promedioNotas()

# Ejercicio 9:



#Ejercicio 10: recibe como parametro 2 numeros y devuelve cuantos multiplos
# del primero son menores que el 2do
# def multiplos(x: int, y:int):
#     cantidad = 0
#     for i in range(1,y):
#         if i % x == 0:
#             cantidad += 1
#     print (cantidad)
# multiplos(1,10)

# #implementarla utilizando un ciclo while, que multiplique
# # el primer número hasta que sea mayor que el segundo.

# def f2(a:int,b:int):


#Ejercicio 11: ingresar correctamente una contrsaeña

# def contraseña():
#     password = "franpier10"
#     ingreso = str(input("Contraseña: "))
#     t = True
#     while t:
#         if ingreso == password:
#             print("contraseña correcta")
#             t = False
#         else:
#             ingreso = str(input("Contraseña: "))
# contraseña()

# def contraseña_con_intentos ():
#     password = "franpier10"
#     intentos = int(input("intentos: "))
#     ingreso = str(input("Contraseña: "))
#     f = True
#     intentosaux = 1
#     while f:
#         if intentosaux < intentos:
#             if not ingreso == password:
#                 intentosaux +=1
#                 ingreso = str(input("Contraseña: "))
#             else:
#                 print("Contraseña correcta. Hiciste",intentosaux,"intentos")
#                 f = False
#         else:
#             print("te quedaste sin intentos, vuelve mas tarde")
#             f = False
# contraseña_con_intentos()

# def contraseña_con_intentos_TRUE_FALSE(): #?





#Ejercicio 12:

# def es_primo(n: int):
#     contador = 0
#     for i in range (1,n+1):
#         if n % i == 0:
#             contador += 1
#     if contador == 2:
#         return True
#     else:
#         return False
# print(es_primo(13))
# # imprimir todos lso numeros primos que hay menores o iguales que ese numero

# def imprimePrimos(x:int):
#     for i in range(1,x+1):
#         if es_primo(i):
#             print (i)
# imprimePrimos(20)


# Ejercicio 13: es potencia de dos?


# def es_potencia_de_dos (x:int):
#     if x <= 0:
#         return False
#     while x > 1:
#         if x % 2 != 0:
#             return False
#         x /= 2
#     return True

# def suma_de_potencias_de_dos (a:int,b:int):
#     suma = 0
#     for i in range(a,b+1):
#         if es_potencia_de_dos(i):
#             suma += i
#     print(suma)
# suma_de_potencias_de_dos(2,16)

from random import *

# def lanzamiento_dado():
#     dado = randint(1,6)
#     intentos = 0
#     while dado != 6:
#         print("Sacaste",dado)
#         intentos += 1
#         dado = randint(1,6)
#     print ("Sacaste",dado,"en",intentos,"intentos")
# lanzamiento_dado()

# def lanzo_n_veces_dos_dados():
#     n = int(input("Ingrese la cantidad de veces que se lanzaran los dados: "))
#     coincidencias = 0
#     for i in range (n+1):
#         dado1 = randint(1,6)
#         dado2 = randint(1,6)
#         if dado1 == dado2:
#             coincidencias +=1
#     print ("Los dados coincidieron",coincidencias,"veces")
# lanzo_n_veces_dos_dados()

# def juego_de_dados ():
#     veces = int(input("Ingrese la cantidad de veces que se lanzaran los dados: "))
#     pesos = 0
#     dolares = 0
#     for i in range(veces + 1):
#         dado = randint(1,6)
#         if dado == 6:
#             pesos += 4
#         elif dado == 3:
#             dolares += 1
#         elif dado == 2 or dado == 4 or dado == 5:
#             pesos -= 2
#     print("El resultado final del juego fue:",pesos,"pesos y" ,dolares ,"dolares")

# juego_de_dados()




















