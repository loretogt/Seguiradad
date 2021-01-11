f = open("todo.txt", "r")
opciones=0
while(True):
    linea = f.readline()
    if   ("FINALMENTE" in linea) and ("END" in linea):
        print("\n---------")
        print (linea)
        opciones+=1
    if not linea:
        break
print(opciones)
f.close()