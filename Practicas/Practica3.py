# # Ejercicio 1: posiciones multiplo

# def posiciones_multiplo(lista:"list",multiplo:int):
#     nuevaLista=[]
#     longitud = len(lista)
#     for i in range(longitud):
#         if i % multiplo == 0:
#             nuevaLista.append(lista[i])
#     print (nuevaLista)
# posiciones_multiplo([1,2,3,4,5,6,2],1)
# # l = [1,2,3,4,5,6,7,8,9,10]
# # print(l[: : 3])

# # Ejercicio 2: Suma acumulada: [1,2,3] -> [1,3,6]. el segundo elemento
# # es la suma del primero mas el 2do, el 3ro es eso mas el 3ro

# def sumaAcumulada (lista:"list"):
#     resultado = []
#     resultado.append(lista[0])
#     for i in range(len(lista[1:])):
#         elemento = resultado[i] + lista[i + 1]
#         resultado.append(elemento)
#     print(resultado)
# sumaAcumulada([1,2,3,4])


# # Ejercicio 3: elimina 
# def elimina_lista(lista:"list"):
#     ListaSinPrimeroNiUltimo = []
#     elimacion1 = lista[1:len(lista) - 1]
#     ListaSinPrimeroNiUltimo += elimacion1
#     print(ListaSinPrimeroNiUltimo)
# elimina_lista([1,2,3,4,55,6])

# # Ejercicio 4: ordenada? 
# def lista_ordenada (lista: "list"):
#     for i in range(len(lista) - 1):
#         if lista[i] > lista[i + 1]:
#             return False
#     return True
# print(lista_ordenada(["a","b"]))

# # Ejercicio 5: duplicado 

# def duplicado(lista:'list'):
#     for i in range(len(lista)):
#         for j in range(i+1,len(lista)):
#             if lista[i] == lista[j]:
#                 return True
#     return False
            
# print(duplicado([1,2,3,4,1])) 

# # Ejercicio 6: elimina duplicados 
# def elimina_duplicados(lista:"list"):
#     listaSinDuplicados = []
#     for i in lista:
#         if i not in listaSinDuplicados:
#             listaSinDuplicados.append(i)
#     print(listaSinDuplicados)
                
# elimina_duplicados([1,2,3,1,2]) 


# # Ejercicio 9: 
# def reverseString(palabra:str):
#     p = ""
#     h = palabra[0]
#     palabra = palabra[1:]
#     l = len(palabra)
#     for i in range(1,l + 1):
#         p +=palabra[-i]
#     for i in p:
#         print (i)
#     print (h)                   
# reverseString("Franco") 

# # Ejercicio 10: contar cuantas veces aparece x en S 

# def contar_caracter(string:str, caracter:int):
#     print(string.count(caracter))
               
# contar_caracter("hola","h")  
        
# # EJercicio 11: cuantas veces aparecen las vocales. 
# def cuenta_vocales(palabra:str):
#     vocales = "aeiou"
#     contador = 0
#     for i in palabra:
#         for j in vocales:
#             if i == j:
#                 contador += 1
#     print(contador)
# cuenta_vocales("aeioupo")

# # Ejercicio 12: recibe una cadena de palabras separadas
# # por espacios y duvuelve cuantas de estas tienen mas de 
# # 5 letras

# def masDeCincoLetras(espacio:str):
#     listaDeMayoresA5 = []
#     for i in espacio.split():
#         if len(i) > 5:
#             listaDeMayoresA5.append(i)
#     print(len(listaDeMayoresA5))
# masDeCincoLetras("hola me llamo Franco Pierabella")
        
# # ---------------------------
# # TUPLAS

# def  diaSiguiente(tupla:tuple):
#     if tupla[0] >= 1 and tupla[0]<=31:
#         if tupla[1] == 2 or tupla[1] == 4 or  tupla[1] == 6 or tupla[1] == 9 or tupla[1] == 11:
#             if tupla[1] == 2 and tupla[0] == 28:
#                 tuplaFebrero = (1,3,tupla[2])
#                 return tuplaFebrero   # Cambio de febreo a marzo
#             else: 
#                 if tupla[0] == 30:
#                     tupla30 = (1,tupla[1] + 1,tupla[2])
#                     return tupla30
#                 elif tupla[0] < 30:
#                     tuplaNo30 = (tupla[0] + 1,tupla[1],tupla[2])
#                     return tuplaNo30
#                 else:
#                     return "La tupla ingresada no es un dia del Año"
#         elif tupla[1] == 1 or tupla[1] == 3 or tupla[1] == 5 or tupla[1] == 7 or tupla[1] == 8 or tupla[1] == 10 or tupla[1] == 12:
#             if not tupla[1] == 12:
#                 if tupla[0] < 31:
#                     tupla31 = (tupla[0] + 1, tupla[1],tupla[2])
#                     return tupla31
#                 elif tupla[0] == 31:
#                     tuplaNo31 = (1,tupla[1] + 1,tupla[2])
#                     return tuplaNo31
#                 else:
#                     return "La tupla ingresada no es un dia del Año"
#             else:
#                 if tupla[0] == 31:
#                     tuplaAñoNuevo = (1,1,tupla[2] + 1)
#                     return tuplaAñoNuevo
#                 elif tupla[0] < 31:
#                     tuplaDiciembre = (tupla[0] + 1, tupla[1], tupla[2])
#                     return tuplaDiciembre
#                 else:
#                     return "La tupla ingresada no es un dia del Año"
#         else:
#             return "La tupla ingresada no es un dia del Año"
#     else:
#             return "La tupla ingresada no es un dia del Año"
# print(diaSiguiente((11,1,2023)))

# # # Ejercicio 11: dia suiguiente pero los meses son "Ene", "Feb", etc 

# # Funciones cambio de mes
# def posterior(mes):
#     if mes == "Ene":
#         return "Feb"
#     elif mes ==  "Feb":
#         return "Mar"
#     elif mes == "Mar":
#         return "Abr"
#     elif mes == "Abr":
#         return "May"
#     elif mes == "May":
#         return "Jun"
#     elif mes == "Jun":
#         return "Jul"
#     elif mes == "Jul":
#         return "Ago"
#     elif mes == "Ago":
#         return "Sep"
#     elif mes == "Sep":
#         return "Oct"
#     elif mes == "Oct":
#         return "Nov"
#     elif mes == "Nov":
#         return "Dic"
#     elif mes == "Dic":
#         return "Ene"
#     else:
#         return "Ingrese un mes"

# def siguienteDia(tupla:tuple):
#     if tupla[0] >= 1 and tupla[0]<=31:
#         if tupla[1] == "Feb" or tupla[1] == "Abr" or  tupla[1] == "Jun" or tupla[1] == "Sep" or tupla[1] == "Nov":
#             if tupla[1] == "Feb" and tupla[0] == 28:
#                 tuplaFebrero = (1,"Mar",tupla[2])
#                 return tuplaFebrero   # Cambio de febreo a marzo
#             else: 
#                 if tupla[0] == 30:    
#                     tupla30 = (1,posterior(tupla[1]),tupla[2])
#                     return tupla30
#                 elif tupla[0] < 30:
#                     tuplaNo30 = (tupla[0] + 1,tupla[1],tupla[2])
#                     return tuplaNo30
#                 else:
#                     return "La tupla ingresada no es un dia del Año"
#         elif tupla[1] == "Ene" or tupla[1] == "Mar" or tupla[1] == "May" or tupla[1] == "Jul" or tupla[1] == "Ago" or tupla[1] == "Oct" or tupla[1] == "Dic":
#             if not tupla[1] == "Dic":
#                 if tupla[0] < 31:
#                     tupla31 = (tupla[0] + 1, tupla[1],tupla[2])
#                     return tupla31
#                 elif tupla[0] == 31:
#                     tuplaNo31 = (1,posterior(tupla[1]),tupla[2])
#                     return tuplaNo31
#                 else:
#                     return "La tupla ingresada no es un dia del Año"
#             else:
#                 if tupla[0] == 31:
#                     tuplaAñoNuevo = (1,"Ene",tupla[2] + 1)
#                     return tuplaAñoNuevo
#                 elif tupla[0] < 31:
#                     tuplaDiciembre = (tupla[0] + 1, tupla[1], tupla[2])
#                     return tuplaDiciembre
#                 else:
#                     return "La tupla ingresada no es un dia del Año"
#         else:
#             return "La tupla ingresada no es un dia del Año"
#     else:
#             return "La tupla ingresada no es un dia del Año"

# print(siguienteDia((11,"Ene",2022)))
    
                
# def tuplasDomino(tupla1:tuple,tupla2:tuple):
#     if len(tupla1) and len(tupla2) == 2:
#   
# if tupla1[0] >= 0 and tupla2[0] >= 0 and tupla1[0] <= 6 and tupla2[0] <= 6:
#             if tupla1[1] == tupla2[1]:
#                 return True
#             else:
#                 return False
#     else:
#         return "La tupla ingresada no es una ficha del domino"
# print(tuplasDomino((3,4),(5,4)))

def tuplasDomStrings (string:str):
    string.split()
    ficha1 = string[0:5]
    ficha2 = string[5:]
    tuplaJugada1 = (ficha1)
    tuplaJugada2 = (ficha2)
    if len(tuplaJugada1) == 5 and len(tuplaJugada2) == 5:
        if int(tuplaJugada1[1]) >= 0 and int(tuplaJugada2[1]) >= 0:
            if tuplaJugada1[3] == tuplaJugada2[3]:
                return True
            else:
                return False
    else:
        return "No son fichas de domino"        
print(tuplasDomStrings("[3-4][2-5]"))
    
    
                
         
    
    

            