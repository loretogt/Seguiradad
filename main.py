
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

def pb(): #Porta/Bellaso
    while True:
        bloque1= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
        bloque2= ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
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

        print("---------")
        print("Que quieres hacer?")
        print("1. Introducir texto a descifrar")
        print("2. Decime a que bloque pertenece")
        print("3. Descifrar")
        print("4. Sacar coincidencias")
        print("5. Sacar fragmento")
        print("6. Me esta tocando las narices")
        le=input()
        descif=[]
        if(le=="1"):
            print("---------")
            print("Cual es el texto a descifrar")
            print("---------")
            tex= input().upper()
            for i in tex:
                if i != " ":
                    descif.append(i)
            
        if(le=="2"):
            print("---------")
            print("Que texto?")
            print("---------")
            texto=input().upper()
            res=[]
            for l in texto:
                if l in bloque1:
                    res.append(1)
                if l in bloque2:
                    res.append(2)
            print(res)

        if (le=="3"):
            if not descif: 
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
                print("--------")
                if get_key(letra,diccionarios.get(clave[i])) != -1:
                    resultado.append(get_key(letra,diccionarios.get(clave[i])))
                else:
                    resultado.append(diccionarios.get(clave[i]).get(letra))

                if i == len(clave)-1:
                    i=0
                else:
                    i+=1
            print(resultado)
        
        if(le=="4"):
            if not descif: 
                print("---------")
                print("Cual es el texto a descifrar")
                print("---------")
                tex= input().upper()
                for i in tex:
                    if i != " ":
                        descif.append(i)
            frag=[]
            for i in descif:
                if i != " ":
                    frag.append(i)
            texto=[]
            for l in frag:
                if l in bloque1:
                    texto.append(1)
                if l in bloque2:
                    texto.append(2)
            print("Que palabra se que aparece")
            pal=input().upper()
            palabra=[]
            for l in pal:
                if l in bloque1:
                    palabra.append(2)
                if l in bloque2:
                    palabra.append(1)

            for pos in range(0,len(texto)):
                i = 0
                entext=""
                for l in palabra:
                    if pos+i<len(frag):
                        entext+=str(frag[pos+i])
                        if (l!=texto[pos+i]):
                            break
                        i+=1
                #while (i < (len(palabra)) & (palabra[i]==texto[pos+i])):
                #    print("se mete")
                #    entext+=str(frag[pos+i])
                #    print(entext)
                #    i+=1
                if i == (len(palabra)):
                    print(entext)
                pos+=1

                    
        if (le=="5"):       
            print("Cual es el fragmento?")
            frag=input().upper()
            print("Cual es el trozo conocido?")
            pal=input().upper()
            r=[]
            i = 0
            for i in range(0,len(pal)):
                for k in diccionarios:
                    if get_key(pal[i],diccionarios.get(k)) != -1:
                        if get_key(pal[i],diccionarios.get(k))==frag[i] :
                            r.append(k)
                            continue
                    elif diccionarios.get(k).get(pal[i])==frag[i]:
                        r.append(k)
                        continue
            print (r)
        
        if (le=="6"):
            if not descif: 
                print("---------")
                print("Cual es el texto a descifrar")
                print("---------")
                tex= input().upper()
                for i in tex:
                    if i != " ":
                        descif.append(i)
                        
            print("Cual es la clave sin saber el orden?")
            clave=input().upper()
            resultado=[]
            i = 0
            for j in range(0,len(clave)):
                for letra in descif:
                    if get_key(letra,diccionarios.get(clave[i])) != -1:
                        resultado.append(get_key(letra,diccionarios.get(clave[i])))
                    else:
                        resultado.append(diccionarios.get(clave[i]).get(letra))
                    if i == len(clave)-1: #para volver a repetir la clave
                        i=0
                    else:
                        i+=1
                i=0
                print(resultado)
                print("---------------")
                clave=clave[-1:] + clave[:-1]
                print ("----------CLAVE "+ clave+"-----------")
                
'''
def vi(): #vigenere
    print("1. Añade el texto en claro")
    c=input().upper()
    claro=[]
    for i in c:
        if i!=" ":
            claro.append(i)
    print("2. Añade el texto criptado")
    cr=input().upper()
    cript=[]
    for i in cr:
        if i!=" ":
            cript.append(i)
    
    print(len(claro))
    print(len(cript))
    for i in range(0,len(cript)):
        print (claro[i]+"\t "+cript[i]) 
    #if(le=="1"): #Text-autokey
        
    #else: #Key-autokey
'''
def pl(): #playfair
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    mat=[]
    l = np.zeros((5, 5))
    print("Conoces texto y clave: ")
    print("1. Si")
    print("2. No")
    le=input()
    if(le=='1'):
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
            #print(str(x1)+","+str(y1))
            #print(str(x2)+","+str(y2))
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


    if(le=="2"):
        descif=[]
        #print("Cual es el texto a descifrar")
        #tex= input().upper()
        tex= "TLKYZ TACEM ZTZES WGTSL WEXTI ZTCOU NBGEG ETVEW DGSOK GGTOV SYVWM TGDXL SKXTG ESMTM XDMHT GEWEM TMTGQ RMYCT XSUYX VSMTM XYGEV ITKMR EMGKD MECYD TZIVY WCTLX SWXZS LECMD GTXVW GUKGA VXTCG YGTVU RYLXK STZGA XSUYW GEIVS MXMYS LKRCG RMLGZ EZCMD UKCTL XTMLT GASLX AGDRY GTQXK SMDVI WTSLX CGASM ZELXY UACEC LILXW CHLEC MDGTP QMNIR KCLZT WCTGT ZHMDI VCTLI TZTMZ TTIYM GTZXE CLTRG XCVOM YVLBF VIDMG KOUMR NMOUZ ELXMR GKREZ TWSTG QMWTZ LEDMT TIDQ"
        for i in tex:
            if i != " ":
                descif.append(i)

        #perm = permutations(["A", "B", "C", "E", "G", "H", "I", "K", "M", "O", "P", "S", "T", "U", "V"], 5) 
        perm = product(["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], repeat=5) 
        vueltas = 0
        for i in list(perm):  
            clave=["F","N","D","Q","-","-","R","Y","W","-","Z","L","—","-","X"]
            #clave[2]=i[0]
            clave[4]=i[0]
            clave[5]=i[1]
            clave[9]=i[2]
            clave[12]=i[3]
            clave[13]=i[4]
            #print(clave)
            mat=[]
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
            #print(matrix)

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

            if (vueltas%100000==0):
                print("Vas por " + str(vueltas)+ " vueltas")
            
            
            if ((str(res[-3])=='E' ) and (str(res[-2])=='N') and (str(res[-1])=='D')):
                print("Se ha encontrado END")
                print(clave)
                #print(matrix)
                print("".join(res))
                #text_file.write("Se ha encontrado END \n")
                text_file.write("En la vuelta "+ str(vueltas)+"\n")
                text_file.write(str(clave)+"\n")
                text_file.write(str("".join(res))+"\n")
                text_file.write("-------------\n\n")
                #if (vueltas%100000==0):
                #    text_file.write("\n\nVAS POR " + str(vueltas)+ " VUELTAS\n\n")
                
            
          
            vueltas+=1
            
        print("-------HE TERMINDADO -------- CON LAS SIGUIENTES VUELTAS: "+ str(vueltas))       
        

            
def ic(): #indice de coincidencia
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
    print(sum/(len(descif)*(len(descif)-1)))
                        
def tc(tex,clave):#transposicion columnar sencilla
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    descif=[]
    #print("Cual es el texto a descifrar")
    #tex= input().upper()
    for i in tex:
        if i != " ":
            descif.append(i)
    #print("Cual es la clave?")
    #clave=input().upper()
    res=[]
    tras={}
    ordenclave=[None] * len(clave)
    i = 1
    for elem in letras:
        for k in range(0,len(clave)):
            if clave[k] == elem:
                ordenclave[k]= i
                i+=1
    #print(ordenclave)
    longitud=int(len(descif)/len(clave))
    extralong=int(len(descif)%len(clave))
    #print(len(descif))
    #print("Longitud columnas " + str(longitud))
    #print("Numero columnas mas largas " + str(extralong))

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
    #print(tras)

    for fila in range(0,longitud+1): #contador de filas
        for column in range(0,len(ordenclave)): #contador de filas
            if (fila == longitud): #si son los de la ultima fila que no esta completa
                if column<extralong: #si esta coluna tine esa fila extra
                    res.append(tras[ordenclave[column]][fila])
            else: 
                res.append(tras[ordenclave[column]][fila])

    #print (res)
    restring="".join(res)
    print (restring)
    return restring
            

def vi(): #viggener
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
    #print (dic)
    print("Que quieres hacer")
    print("Cual es el texto")
    desfif= []
    tex= input().upper()
    for i in tex:
        if i != " ":
            desfif.append(i)
    '''
    print("1. Descifrar con clave")
    print("2. Encontrar palabra")
    le = input()
    if (le=="1"):
        '''
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
    print (res)
    '''
    if (le=="2"): #encontrar palabra
        print("Cual es la clave")
        c = input().upper()
        palabra=[]
        for i in c:
            if i != " ":
                palabra.append(i)
        res=[]
        #for elem in desfif:

        print(res)
        '''

def sc(): # Straddling Checkerboard
    descif=[]
    print("Cual es el texto a convertir")
    tex= input().upper()
    '''
    dic={"8":"A",  "3":"T",          "9":"O",   "2":"N",   "6":"E",          "4":"S",  "1":"I",  "7":"R",
        "58":"B", "53":"C", "55":"D", "59":"F", "52":"G", "56":"H", "50":"J", "54":"K", "51":"L", "57":"M",
        "08":"P", "03":"Q", "05":"U", "09":"V", "02":"W", "06":"X", "00":"Y", "04":"Z", "01":".", "07":" "}
    '''
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


def adfgvx(tex, clave):
    letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    adfgvx= ["A", "D", "F", "G", "V", "X"]
    mat=[]
    l = np.zeros((6, 6))
    #print("Ingrese clave")
    #clave= input().upper()
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
    #print("".join(mat))
    matrix= np.array(mat).reshape((6, 6))
    #print(matrix)

    #print("Cual es el texto")
    desfif= []
    #tex= input().upper()
    for i in tex:
        if i != " ":
            desfif.append(i)
    des=[]
    i=0
    for elem in range(0,int(len(desfif)/2)): #los ejementos se cogen de dos en dos
        #print(adfgvx.index(desfif[i]))
        #print(adfgvx.index(desfif[i+1]))
        des.append(matrix[adfgvx.index(desfif[i])][adfgvx.index(desfif[i+1])])
        i+=2
    #print("".join(des))
    return ("".join(des))

def ej2():
    #perm = combinations_with_replacement(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], 5) 
    perm = product(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],  repeat=5) 
    numeros=["0","1","2","3","4","5","6","7","8","9"]
    vueltas = 0
    clave=[]
    texto="VAAFF AFDAA ADFAA FAXDA AAFDF DADDD GXXGA VVAFA XAVAF VGFXV GFGXX GVFFV FFDFX GDXVD FFVAA FVFVD AXVFX VDDVF VDDGF DDAAA DFGFF FFFFV VGXAV XAFGF AGAAD FDGGA FXGFG FDFVF GFGGG VXGXA FAAAA ADVFA FXAFA XGAGG FFGVA XADAF GFXAA AXADX GXFFA FAAGA XVAVF AAVAD FDVDD DVDAA FAXFD VAFAA FAADX AFD"
    for i in list(perm):  
        clave=["A","T","T","-","H","-","T","E","-","Q","-","-","L","I","H","Q"]
        clave[3]=i[0]
        clave[5]=i[1]
        clave[8]=i[2]
        clave[10]=i[3]
        clave[11]=i[4]
        clave="".join(clave)
        #print(clave)
        trans=str(tc(texto,clave))
        res=adfgvx(trans,"COLABORACIONES")
        #print(res)
        if (vueltas%10000==0):
            print("Numero de vueltas "+ str(vueltas))
            text_file.write("\n\n Numero de vueltas "+ str(vueltas))

        if ((str(res[-3])=='E' ) and (str(res[-2])=='N') and (str(res[-1])=='D')):
            notnum=True
            for elem in res:
                if elem in numeros:
                    notnum=False
                    break
            if notnum==True:
                print("Se ha encontrado END")
                print(clave)
                print(res)
                text_file.write("Se ha encontrado END \n")
                text_file.write("En la vuelta"+ str(vueltas)+"\n")
                text_file.write(str(clave)+"\n")
                text_file.write(str(res)+"\n")
                text_file.write("-------------\n\n")
        vueltas+=1
    print("He terminado con las siguientes vuetas: "+ str(vueltas))
    print(clave)

if __name__ == "__main__":
    print("---------")
    print("Con algoritmo quiers?")
    print("1. Porta/Bellaso")
    print("2. Vigenere")
    print("3. Transposición playfair")
    print("4. Indice de coincidencia")
    print("5. Trans columnar sencilla")
    print("6. Vigenere")
    print("7. Straddling Checkerboard")
    print("8. ADFGVX")
    print("9. Ejercicio 2")
    le=input()
    text_file = open("Output.txt", "w")
    if(le=="1"):
        pb()
    if(le=="2"):
        vi()
    if(le=="3"):
        pl()
    if(le=="4"):
        ic()
    if(le=="5"):
        print("Cual es el texto a descifrar")
        tex= input().upper()
        print("Cual es la clave?")
        clave=input().upper()
        tc(tex,clave)
    if(le=="6"):
        vi()
    if(le=="7"):
        sc()
    if(le=="8"):
        print("Ingrese clave")
        clave= input().upper()
        print("Cual es el texto")
        texto= input().upper()   
        adfgvx(texto, clave)
    if (le=="9"):
        ej2()
    text_file.close()
