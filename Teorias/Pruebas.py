# l = [1,2,3,4]
# tupla = (1,l)
# # l.append(5)
# l[0] = 6
# print(tupla) # Si se modifica la tupla

# t = (1,l)
# t[1].append("5") # Esto si, pues estoy cambiando la lista y no la tupla
# print(t)
# # t[1] = [1,2,3] # Esto no se puede

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# # l[1000] = 1 # index out of range
# print(l)
# print(l[2:5:10])
# l[::]

# def buscar (lista,elemento,i = 0):
#     if i == len(lista):
#         return False
#     if lista[i] == elemento:
#         return True
#     return buscar(lista,elemento, i + 1)
# print(buscar([1,2,3,4,5,7],2))


# t = (1,"hola",True,(2,1),[1,2,3])
# t[4][2] = 1
# print(t)
# # for i in t:
# #     tupla = ()
# #     tupla +=(i,i)
# #     print(tupla)
# # """ 
# def sumaTuplas(tupla1,tupla2):
#     tuplavacia = ()
#     suma = tupla1 + tupla2
#     tuplavacia += suma
#     print(tuplavacia)
# sumaTuplas((1,2),(3,2))
# tv = (2,1,2,3,2,2)
# tcc = (2,[1,2,3],"hola",True)
# tv += tcc
# print(tv)
# contador = tv.count(2)
# a  = tv.index(1)
# b = tv.__add__((1,2))
# c = tv.__contains__(2)
# print(contador,a,b,c)
# t1 = (1,2)
# t2 = (1,2)
# t3 = t1 + t2
# print(t3)
# # Se puede sumar tupla a otra tupla. tupla + tupla = (tupla,tupla)
# # no se le puede sumar un elemento
# # """

# pal = "string"
# # pal[2] = 'S' np se puede.
# print (pal[0])


# #Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante)
# # y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.

# def contra ():
#     ingreso = str(input("contraseña: "))
#     ingreso1 = str(input("contraseña: "))
#     intentos = 3
#     while ingreso != ingreso1 and intentos > 1:
#         intentos -= 1
#         print("tienes",intentos,"para ingresar la contraseña")
#         ingreso1 = str(input("contraseña: "))
#     if ingreso == ingreso1:
#         print("COntraseña correcta")
#     else:
#         print("Contrañesa incorrecta espera n minutos")

# contra()



fran = [1,2,"hola",True]
fran.remove(2)
print(fran)