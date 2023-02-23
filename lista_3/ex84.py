# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
salario = float(input("Dgite o salario inicial do funcionario: "))
aumento = 1.5

for i in range(1996, 2018 + 1):
    aumento = aumento * 2
    salario_atual = salario + (salario * (aumento / 100))
    print("Salario em ", i, " = ", salario_atual)