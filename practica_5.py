N=int(input("Ingrese un numero par: "))

if N%2==0:
    row=[]
    veces = 0
    for i in range(1,N + 1):
        row.append(str(i))
        row.append("\t")
        x = i - 1
        y = i
        z = x + y
        a = x * y
        veces = veces + 1
        if veces == 2:
            row.append(str(z))
            row.append("\n")
        elif veces == 4:
            row.append(str(a))
            row.append("\n")
            veces = 0
            
matrix = "".join(row)       
with open('text.txt','w') as file:
    file.writelines(matrix)