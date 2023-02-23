# Faça um programa que leia 5 números e informe o maior número.
numeros = []
for num in range(1, 6):
    numeros.append(int(input("Digite um número: ")))

maiorNumero = numeros[0]

cont = 1
while cont < len(numeros):
    if numeros[cont] > maiorNumero:
        maiorNumero = numeros[cont]
    cont = cont + 1
        
print (f"O maior número é {maiorNumero}")