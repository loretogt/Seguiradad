import numpy as np
import os
from itertools import permutations
from itertools import combinations_with_replacement
from itertools import product
import math

letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M",
          "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
mat = []
l = np.zeros((5, 5))
print("Ingrese clave")
clave = input().upper()
for l in clave:
        if l in mat:
            continue
        else:
            mat.append(l)
for l in letras:
        if l in mat:
            continue
        else:
            mat.append(l)
matrix = np.array(mat).reshape((5, 5))
print(matrix)

descif = []
print("---------")
print("Cual es el texto a descifrar")
print("---------")
tex = input().upper()
for i in tex:
        if i != " " and i !="J":
            descif.append(i)
        if i =="J":
            descif.append("I")
if len(descif)%2 !=0:
    descif.append("X")
i = 0
res = []
for j in range(0, int(len(descif)/2)):
        l1 = descif[i]
        i += 1
        '''
        if (i == len(descif)):
            l2 = 'X'
        else:
        '''
        l2 = descif[i]
        i += 1
        (x1, y1) = (int(mat.index(l1)/5), mat.index(l1) % 5)  # x es la fila y es la columna, contando en 0
        (x2, y2) = (int(mat.index(l2)/5), mat.index(l2) % 5)
        if (y1 == y2):  # es la misma columna")
            newx1 = x1+1
            if newx1 == 5:
                newx1 = 0
            newx2 = x2+1
            if newx2 == 5:
                newx2 = 0
            res.append(matrix.item(newx1, y1))
            res.append(matrix.item(newx2, y1))

        elif (x1 == x2):  # es la misma fila
            newy1 = y1+1
            if newy1 == 5:
                newy1 = 0
            newy2 = y2+1
            if newy2 == 5:
                newy2 = 0
            res.append(matrix.item(x1, newy1))
            res.append(matrix.item(x2, newy2))

        else:  # no coincide ninguna
            res.append(matrix.item(x1, y2))
            res.append(matrix.item(x2, y1))
print("".join(res))
