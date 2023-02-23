# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
lista = []
count = 0

quantidade = int(input("Digite a quantidade de número que deseja: "))
while quantidade != count:
    lista.append(float(input("Digite um número: ")))
    count += 1
maior = max(lista)
menor = min(lista)
print(f"Lista:{lista} " f"\nMaior: {maior}" f"\nMenor:{menor} ")
print(f"Soma: {sum(lista)}")