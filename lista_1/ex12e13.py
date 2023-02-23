# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal
# Usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Insira sua altura em metros: "))
peso_ideal_homem = (72.7*altura) - 58
peso_ideal_mulher = (61.1*altura) - 44.7
print(f"Caso voce seja homem, seu peso ideal é {peso_ideal_homem}kg, caso seja mulher é {peso_ideal_mulher}kg.")