# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
horas = float(input("Quanto voce ganha por hora trabalhada? R$ "))
nh = float(input("Quantas horas voce trabalhou no mes? "))
salario = horas * nh
print(f"Voce recebeu no mes um total de R$ {salario}")