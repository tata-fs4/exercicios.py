# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
lista_notas = []

for i in range(0,4):
    notas = float(input("Digite as notas: "))
    lista_notas.append(notas)
media = (sum(lista_notas)) / 4
print(f"As suas notas são: {lista_notas}")
print(media)