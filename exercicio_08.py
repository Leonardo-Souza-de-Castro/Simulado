n =  int(input())

v1 = 0
v2 = 0
lista = []

for i in range(1,n):
    v3 = v1+v2
    v1 = v2
    v2 = v3

    if(v1 == 0 and v2 == 0):
        v1 = 1

    lista.append(v3)

print(*lista)
