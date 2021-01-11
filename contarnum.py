num=["0","1","2","3","4","5","6","7","8","9"]
descif=[]
apariciones=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print("Cual es el texto")
tex= input().upper()
for i in tex:
    if i != " ":
        descif.append(i)

for i in range(0,len(num)):
    for l in descif:
        if num[i]==l:
            apariciones[i]+=1

for i in range(0,len(num)):
    print("Numero " + str(num[i])+ ", " + str(apariciones[i])+ " apariciones")
#print(num)
#print(apariciones)