# Faça um programa que calcule o mostre a média aritmética de N notas.
numero_notas = int(input("Digite o número de notas que deseja: "))
count = 0
todas_notas = []

while count < numero_notas:
    notas = todas_notas.append(float(input("Digite a nota: ")))
    count += 1

media = sum(todas_notas) / numero_notas
print(f"A média é igual a {media}")