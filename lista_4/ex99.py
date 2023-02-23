# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista_num = []

for i in range(0,10):
    num = float(input("Digite um número: "))
    lista_num.append(num)
lista_num.reverse()

print(lista_num)