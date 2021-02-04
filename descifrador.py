import numpy as np
import os
from itertools import permutations  
from itertools import combinations_with_replacement 
from itertools import product
import math

# function to return key for any value
def get_key(val,my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key
    return -1

def portaBellaso():
    diccionarios= { 'A':{'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z'},
                    'B':{'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z'},
                    'C':{'A':'Z','B':'N','C':'O','D':'P','E':'Q','F':'R','G':'S','H':'T','I':'U','J':'V','K':'W','L':'X','M':'Y'},
                    'D':{'A':'Z','B':'N','C':'O','D':'P','E':'Q','F':'R','G':'S','H':'T','I':'U','J':'V','K':'W','L':'X','M':'Y'},
                    'E':{'A':'Y','B':'Z','C':'N','D':'O','E':'P','F':'Q','G':'R','H':'S','I':'T','J':'U','K':'V','L':'W','M':'X'},
                    'F':{'A':'Y','B':'Z','C':'N','D':'O','E':'P','F':'Q','G':'R','H':'S','I':'T','J':'U','K':'V','L':'W','M':'X'},
                    'G':{'A':'X','B':'Y','C':'Z','D':'N','E':'O','F':'P','G':'Q','H':'R','I':'S','J':'T','K':'U','L':'V','M':'W'},
                    'H':{'A':'X','B':'Y','C':'Z','D':'N','E':'O','F':'P','G':'Q','H':'R','I':'S','J':'T','K':'U','L':'V','M':'W'},
                    'I':{'A':'W','B':'X','C':'Y','D':'Z','E':'N','F':'O','G':'P','H':'Q','I':'R','J':'S','K':'T','L':'U','M':'V'},
                    'J':{'A':'W','B':'X','C':'Y','D':'Z','E':'N','F':'O','G':'P','H':'Q','I':'R','J':'S','K':'T','L':'U','M':'V'},
                    'K':{'A':'V','B':'W','C':'X','D':'Y','E':'Z','F':'N','G':'O','H':'P','I':'Q','J':'R','K':'S','L':'T','M':'U'},
                    'L':{'A':'V','B':'W','C':'X','D':'Y','E':'Z','F':'N','G':'O','H':'P','I':'Q','J':'R','K':'S','L':'T','M':'U'},
                    'M':{'A':'U','B':'V','C':'W','D':'X','E':'Y','F':'Z','G':'N','H':'O','I':'P','J':'Q','K':'R','L':'S','M':'T'},
                    'N':{'A':'U','B':'V','C':'W','D':'X','E':'Y','F':'Z','G':'N','H':'O','I':'P','J':'Q','K':'R','L':'S','M':'T'},
                    'O':{'A':'T','B':'U','C':'V','D':'W','E':'X','F':'Y','G':'Z','H':'N','I':'O','J':'P','K':'Q','L':'R','M':'S'},
                    'P':{'A':'T','B':'U','C':'V','D':'W','E':'X','F':'Y','G':'Z','H':'N','I':'O','J':'P','K':'Q','L':'R','M':'S'},
                    'Q':{'A':'S','B':'T','C':'U','D':'V','E':'W','F':'X','G':'Y','H':'Z','I':'N','J':'O','K':'P','L':'Q','M':'R'},
                    'R':{'A':'S','B':'T','C':'U','D':'V','E':'W','F':'X','G':'Y','H':'Z','I':'N','J':'O','K':'P','L':'Q','M':'R'},
                    'S':{'A':'R','B':'S','C':'T','D':'U','E':'V','F':'W','G':'X','H':'Y','I':'Z','J':'N','K':'O','L':'P','M':'Q'},
                    'T':{'A':'R','B':'S','C':'T','D':'U','E':'V','F':'W','G':'X','H':'Y','I':'Z','J':'N','K':'O','L':'P','M':'Q'},
                    'U':{'A':'Q','B':'R','C':'S','D':'T','E':'U','F':'V','G':'W','H':'X','I':'Y','J':'Z','K':'N','L':'O','M':'P'},
                    'V':{'A':'Q','B':'R','C':'S','D':'T','E':'U','F':'V','G':'W','H':'X','I':'Y','J':'Z','K':'N','L':'O','M':'P'},
                    'W':{'A':'P','B':'Q','C':'R','D':'S','E':'T','F':'U','G':'V','H':'W','I':'X','J':'Y','K':'Z','L':'N','M':'O'},
                    'X':{'A':'P','B':'Q','C':'R','D':'S','E':'T','F':'U','G':'V','H':'W','I':'X','J':'Y','K':'Z','L':'N','M':'O'},
                    'Y':{'A':'O','B':'P','C':'Q','D':'R','E':'S','F':'T','G':'U','H':'V','I':'W','J':'X','K':'Y','L':'Z','M':'N'},
                    'Z':{'A':'O','B':'P','C':'Q','D':'R','E':'S','F':'T','G':'U','H':'V','I':'W','J':'X','K':'Y','L':'Z','M':'N'}}
    descif=[]
    print("---------")
    print("Cual es el texto a descifrar")
    print("---------")
    tex= input().upper()
    for i in tex:
        if i != " ":
            descif.append(i)            
    print("Cual es la clave?")
    clave=input().upper()
    resultado=[]
    i = 0
    for letra in descif:
        if get_key(letra,diccionarios.get(clave[i])) != -1:
            resultado.append(get_key(letra,diccionarios.get(clave[i])))
        else:
            resultado.append(diccionarios.get(clave[i]).get(letra))
        if i == len(clave)-1:
            i=0
        else:
            i+=1
    print("".join(resultado))

def adfgvx(tex, clave):
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    adfgvx= ["A", "D", "F", "G", "V", "X"]
    mat=[]
    l = np.zeros((6, 6))
    for l in clave:
        if l in mat:
            continue
        else:
            mat.append(l)
            if l == "A": mat.append("1")
            if l == "B": mat.append("2")
            if l == "C": mat.append("3")
            if l == "D": mat.append("4")
            if l == "E": mat.append("5")
            if l == "F": mat.append("6")
            if l == "G": mat.append("7")
            if l == "H": mat.append("8")
            if l == "I": mat.append("9")
            if l == "J": mat.append("0")

    for l in letras:
        if l in mat:
            continue
        else:
            mat.append(l)
            if l == "A": mat.append("1")
            if l == "B": mat.append("2")
            if l == "C": mat.append("3")
            if l == "D": mat.append("4")
            if l == "E": mat.append("5")
            if l == "F": mat.append("6")
            if l == "G": mat.append("7")
            if l == "H": mat.append("8")
            if l == "I": mat.append("9")
            if l == "J": mat.append("0")
    matrix= np.array(mat).reshape((6, 6))
    desfif= []
    for i in tex:
        if i != " ":
            desfif.append(i)
    des=[]
    i=0
    for elem in range(0,int(len(desfif)/2)): #los ejementos se cogen de dos en dos
        des.append(matrix[adfgvx.index(desfif[i])][adfgvx.index(desfif[i+1])])
        i+=2
    print(matrix)
    print ("".join(des))

def transColSen(tex,clave):#transposicion columnar sencilla
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    descif=[]
    for i in tex:
        if i != " ":
            descif.append(i)
    res=[]
    tras={}
    ordenclave=[None] * len(clave)
    i = 1
    for elem in letras:
        for k in range(0,len(clave)):
            if clave[k] == elem:
                ordenclave[k]= i
                i+=1
    longitud=int(len(descif)/len(clave))
    extralong=int(len(descif)%len(clave))

    for elem in ordenclave:
        tras[elem]=[]

    elemtexto=0

    for column in range(1,len(ordenclave)+1): #para ir rellenadno cada una de las columnas
        if ordenclave.index(column)+1>extralong: #la columna itiene longitud normal
            for j in range(0,longitud):
                tras[column].append(descif[elemtexto])
                elemtexto+=1
        else: #esa columna tiene un elemento más
            for j in range(0,longitud+1):
                tras[column].append(descif[elemtexto])
                elemtexto+=1

    for fila in range(0,longitud+1): #contador de filas
        for column in range(0,len(ordenclave)): #contador de filas
            if (fila == longitud): #si son los de la ultima fila que no esta completa
                if column<extralong: #si esta coluna tine esa fila extra
                    res.append(tras[ordenclave[column]][fila])
            else: 
                res.append(tras[ordenclave[column]][fila])

    #print (res)
    restring="".join(res)
    print("-------Resultado transposición columnar sencilla-------")
    print (str(restring))
    print ("-------Tabla del descifrado-------")
    for i in tras:
        print(str(i) + " : "+ str(tras[i]))
    print("------")
    return restring

def vigenere():
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letrasnew= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    dic={}
    dic["A"]=letras
    i = 0
    for elem in letras:
        if elem != "A":
            letrasnew= letrasnew[1:] + letrasnew[:1] 
            dic[elem]=letrasnew
            i+=1
    print("Cual es el texto")
    desfif= []
    tex= input().upper()
    for i in tex:
        if i != " ":
            desfif.append(i)

    print("Cual es la clave")
    c = input().upper()
    clave=[]
    for i in c:
        if i != " ":
            clave.append(i)
        
    i=0
    res=[]
    for elem in desfif:
        res.append(letras[dic.get(clave[i]).index(elem)])
        i+=1
        if i >= len(clave):
            i=0
    print ("".join(res))

def playfair():
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    mat=[]
    l = np.zeros((5, 5))
    print("Ingrese clave")
    clave= input().upper()
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
    matrix= np.array(mat).reshape((5, 5))
    print(matrix)

    descif=[]
    print("---------")
    print("Cual es el texto a descifrar")
    print("---------")
    tex= input().upper()
    for i in tex:
        if i != " ":
            descif.append(i)
    i=0
    res=[]
    for j in range(0,int(len(descif)/2)):
            l1=descif[i]
            i+=1
            if (i==len(descif)):
                l2='X'
            else:
                l2=descif[i]
            i+=1
            (x1,y1)=(int(mat.index(l1)/5),mat.index(l1)%5) #x es la fila y es la columna, contando en 0
            (x2,y2)=(int(mat.index(l2)/5),mat.index(l2)%5)
            if (y1==y2): #es la misma columna")
                newx1= x1-1
                if newx1==-1:
                    newx1=4
                newx2= x2-1
                if newx2==-1:
                    newx2=4
                res.append(matrix.item(newx1,y1))
                res.append(matrix.item(newx2,y1))

            elif (x1==x2): #es la misma fila
                newy1=y1-1
                if newy1==-1:
                    newy1=4
                newy2=y2-1
                if newy2==-1:
                    newy2=4
                res.append(matrix.item(x1,newy1))
                res.append(matrix.item(x2,newy2))

            else: #no coincide ninguna
                res.append(matrix.item(x1,y2))
                res.append(matrix.item(x2,y1))
    print("".join(res))
    
def ubchi():
    print("Cual es el texto")
    desfif= []
    tex= input().upper()
    for i in tex:
        if i != " ":
            desfif.append(i)

    print("Cual es la clave 2")
    c = input().upper()
    clave2=[]
    for i in c:
        if i != " ":
            clave2.append(i)
    
    print("Cual es la clave 1")
    c = input().upper()
    clave1=[]
    for i in c:
        if i != " ":
            clave1.append(i)

    res=transColSen(desfif,clave2)
    transColSen(res,clave1)           

def indiceCoincidencia():
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    descif=[]
    apariciones=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Cual es el texto")
    tex= input().upper()
    for i in tex:
        if i != " ":
            descif.append(i)

    for i in range(0,len(letras)):
        for l in descif:
            if letras[i]==l:
                apariciones[i]+=1
    sum=0
    
    for i in apariciones:
        sum+= (i*(i-1))
    print (letras)
    print(apariciones)
    print("----Apariencia de las letras----")
    for i in range(0,len(letras)):
        print(str(letras[i]) + " = " + str(apariciones[i]) )
    print("----Numero de elementos (N)----")
    print(len(descif))
    print("----IC----")
    print(str(sum)+"/"+str(len(descif)*(len(descif)-1))+"=")
    print(sum/(len(descif)*(len(descif)-1)))

def straddlingCheckerboard(): 
    descif=[]
    print("Cual es el texto a convertir")
    tex= input().upper()
    #Hay que poner a mano la clave

    dic={"4":"A",  "6":"T",          "2":"O",   "7":"N",   "3":"E",          "1":"S",  "0":"I",  "5":"R",
        "94":"B", "96":"C", "99":"D", "92":"F", "97":"G", "93":"H", "98":"J", "91":"K", "90":"L", "95":"M",
        "84":"P", "86":"Q", "89":"U", "82":"V", "87":"W", "83":"X", "88":"Y", "81":"Z", "80":".", "85":" "}
    for i in tex:
        if i != " ":
            descif.append(i)
    i= 0
    res=[]
    while i < len(descif):
        if descif[i]=="9" or  descif[i]=="8":
            res.append(dic[ descif[i]+ descif[i+1]])
            i+=2
        else: 
            res.append(dic[descif[i]])
            i+=1
    restring="".join(res)
    print (res)
    print(restring)

def kullback():
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    descif=[]
    apariciones=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Cual es el texto")
    tex= input().upper()
    for i in tex:
        if i != " ":
            descif.append(i)

    for i in range(0,len(letras)):
        for l in descif:
            if letras[i]==l:
                apariciones[i]+=1

    pEsperado=len(descif)*(len(descif)-1)*0.0667 #si fuese en español cambiar el numero a 0,0775
    rEsperado=len(descif)*(len(descif)-1)*0.0385 #si es una distribución random
    
    observada=0
    for i in apariciones:
        observada+= (i*(i-1))

    print("----Apariencia de las letras----")
    for i in range(0,len(letras)):
        print(str(letras[i]) + " = " + str(apariciones[i]) )
    print("----N y N·(N-1)----")
    print("N= "+str(len(descif)))
    print("N·(N-1)= "+ str(len(descif)*(len(descif)-1)))

    print("----φ esperados vs observado----")
    print ("φp (si un mensaje en lenguaje natural o una sustitución monoalfabética): " + str(pEsperado))
    print ("φr (si es aleatorio una sustitución o polialfabética): " + str(rEsperado))
    print ("φobs (Resultado experimental): " + str(observada))

def xTest():
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    descif1=[]
    descif2=[]
    apariciones1=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    apariciones2=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    print("Cual es el texto n1")
    tex= input().upper()
    for i in tex:
        if i != " ":
            descif1.append(i)
    print("Cual es el texto n2")
    tex= input().upper()
    for i in tex:
        if i != " ":
            descif2.append(i)

    #frecuencia de aparición en cada uno de los text
    for i in range(0,len(letras)):
        for l in descif1:
            if letras[i]==l:
                apariciones1[i]+=1
    for i in range(0,len(letras)):
        for l in descif2:
            if letras[i]==l:
                apariciones2[i]+=1

    xObs=0
    for i in range(0,len(apariciones1)):
        xObs+= int((apariciones1[i])*(apariciones2[i]))
   
    print("----Apariencia de las letras----")
    for i in range(0,len(letras)):
        print(str(letras[i]) + " : Texto1= " + str(apariciones1[i]) + " Texto2= " + str(apariciones2[i])+ " X-obs= "+ str(apariciones1[i]*apariciones2[i]) )
    print("----Numero de elementos (N)----")
    print("Texto1= "+ str(len(descif1)))
    print("Texto2= "+ str(len(descif2)))
    print("----Resultados----")
    print("Xr (N1·N2·kr)= " + str(0.0385*len(descif1)*len(descif2)))
    print("Xp (N1·N2·kP)= "+  str(0.0667*len(descif1)*len(descif2))) #este valor puede cambiar ingles=0.0667, español= 0,0775
    print("Xobs= "+ str(xObs))

if __name__ == "__main__":
    print("---------")
    print("Con algoritmo quiers?")
    print("1. Porta/Bellaso")
    print("2. ADFGVX")
    print("3. Trans columnar sencilla")
    print("4. Vigenere")
    print("5. Playfair")
    print("6. Cifrado Ubchi (doble transp columnar)")
    print("7. Indice de coincidencia")
    print("8. Straddling Checkerboard")
    print("9. Test de Kullback")
    print("10. X-Test")

    le=input()
    text_file = open("Output.txt", "w")
    if(le=="1"):
        portaBellaso()
        
    if(le=="2"):
        print("Ingrese clave para construir la tabla")
        clave= input().upper()
        print("Cual es el texto")
        texto= input().upper()
        print("Cual es la clave de la tranposición")
        trans=input().upper()   
        adfgvx(transColSen(texto,trans), clave)

    if(le=="3"):
        print("Cual es el texto a descifrar")
        tex= input().upper()
        print("Cual es la clave?")
        clave=input().upper()
        transColSen(tex,clave)
       
    if(le=="4"):
        vigenere()
        
    if(le=="5"):
        playfair()

    if(le=="6"):
        ubchi()
     
    if(le=="7"):
        indiceCoincidencia()
    
    if(le=="8"):
        straddlingCheckerboard()

    if (le=="9"):
        kullback()
    
    if (le=="10"):
        xTest()
        
  
    
