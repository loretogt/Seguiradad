import numpy as np
letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
descif=[]
print("Cual es el texto a descifrar")
tex= input().upper()
for i in tex:
    if i != " ":
        descif.append(i)
print("Cual es la clave?")
clave=input().upper()
res=[]
tras={}
ordenclave=[None] * len(clave)
i = 1
for elem in letras:
    for k in range(0,len(clave)):
        if clave[k] == elem:
            ordenclave[k]= i
            i+=1
print(ordenclave)
longitud=int(len(descif)/len(clave))
extralong=int(len(descif)%len(clave))
print(len(descif))
print("Longitud columnas " + str(longitud))
print("Numero columnas mas largas " + str(extralong))

for elem in ordenclave:
    tras[elem]=[]

elemtexto=0
#print(len(descif))
for column in range(1,len(ordenclave)+1): #para ir rellenadno cada una de las columnas
    if ordenclave.index(column)+1>extralong: #la columna itiene longitud normal
        for j in range(0,longitud):
            tras[column].append(descif[elemtexto])
            elemtexto+=1
    else: #esa columna tiene un elemento más
        for j in range(0,longitud+1):
            tras[column].append(descif[elemtexto])
            elemtexto+=1
print(tras)

for fila in range(0,longitud+1): #contador de filas
    for column in range(0,len(ordenclave)): #contador de filas
        if (fila == longitud): #si son los de la ultima fila que no esta completa
            if column<extralong: #si esta coluna tine esa fila extra
                res.append(tras[ordenclave[column]][fila])
        else: 
            res.append(tras[ordenclave[column]][fila])

print (res)
restring="".join(res)
print (restring)
        


