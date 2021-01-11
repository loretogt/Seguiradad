from itertools import permutations
text_file = open("Ej7.txt", "w")
todo = open("todo.txt", "w")
descif = []
tex = "ZEIFE LLDSS NTMAT NOORG ASIUI DEEUD SURSS ENREJ ROOOR VSASU IDAZA LOQTB IOPJU SNOIE UCOEE ESEEE NPTEO DCPAD ITFUL IUSLA QAOEA ETAAI AYEET RDELJ UCAAO CSOEO OBALP RLHDI DANBR SAELO TSDSD AOSZP INCAD IORBM ONCND SUINA ONYNO ETMFE CEEAM OLUIR LYOOE AITAD SOINP OEDLT IADEA SNEOS TOEDE CCTOE EOOEI PNZTS DEDCN IOILR ASMRA GUETI DQREL SZRJD ARMAE ISTAL SLOFD ADELT SLSAM HOAQE ASVSL ELRMV UNGAE ELEUN IDLRS SNNSC RBERG OO"
for i in tex:
    if i != " ":
        descif.append(i)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#letras = ["A", "B","C"]
vueltas = 0
# for num in range(8, 12):
#letras= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#perm = product(["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], repeat=6)
perm = permutations(numeros[:10], 10)
for per in list(perm):
        res = []
        tras = {}
        ordenclave = [None] * len(per)
        for e in range(0, len(per)):
            ordenclave[e] = per[e]
        #print(ordenclave)

        #print("long descif " + str(len(descif)))
        #print("long clave " + str(len(clave)))

        longitud = int(len(descif)/len(ordenclave))
        extralong = int(len(descif) % len(ordenclave))

        # print(longitud)
        # print(extralong)

        for elem in ordenclave:
            tras[elem] = []

        elemtexto = 0
        # print(len(descif))
        # para ir rellenadno cada una de las columnas
        for column in range(1, len(ordenclave)+1):
            # la columna itiene longitud normal
            if ordenclave.index(column)+1 > extralong:
                for j in range(0, longitud):
                    tras[column].append(descif[elemtexto])
                    elemtexto += 1
            else:  # esa columna tiene un elemento más
                for j in range(0, longitud+1):
                    tras[column].append(descif[elemtexto])
                    elemtexto += 1
        # print(tras)

        for fila in range(0, longitud+1):  # contador de filas
            for column in range(0, len(ordenclave)):  # contador de filas
                if (fila == longitud):  # si son los de la ultima fila que no esta completa
                    if column < extralong:  # si esta coluna tine esa fila extra
                        res.append(tras[ordenclave[column]][fila])
                else:
                    res.append(tras[ordenclave[column]][fila])

        resconj = "".join(res)
        #print(ordenclave)
        #print(resconj)
        # print("--------")
        #todo.write(str(resconj))
        if ("FINALMENTE" in resconj) and ("END" in resconj):
            print("\n--------")
            print(ordenclave)
            print(resconj)
            text_file.write(str(resconj)+"\n")

        if (vueltas % 10000 == 0):
            print("Vas por las siguientes vueltas: " + str(vueltas))
            print("La clave va por " + str(ordenclave))
        vueltas += 1

text_file.close()
todo.close()