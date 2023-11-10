posicoes = int(input('Digite o valor de N:'))

x = []

menor = 0

for i in range(1,posicoes+1):
    x.append(int(input(f'Digite o {i} valor de X:')))

menor = x[0]
posicao = 0
for i in range(len(x)):
    if x[i] < menor:
        menor = x[i]
        posicao = i
print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")
