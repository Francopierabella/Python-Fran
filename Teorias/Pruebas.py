l = [1,2,3,4]
tupla = (1,l)
l.append(5)
l[0] = 6
print(tupla) # Si se modifica la tupla

t = (1,l)
t[1].append("5") # Esto si, pues estoy cambiando la lista y no la tupla
print(t)
# t[1] = [1,2,3] # Esto no se puede


l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# l[1000] = 1 # index out of range
print(l)
print(l[2:5:10])
l[::]

