# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
nota1=float(input("Digite nota 1: "))
nota2=float(input("Digite nota 2: "))
media=(nota1+nota2)/2
if media >=9:
   conceito = "A"
elif media >= 7.5:
   conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
elif media >= 0:
    conceito = "E"
if conceito in ("A","B","C"):
    resultado = "Aprovado!"
elif conceito in ("D", "E"):
    resultado = "Reprovado"
print(f"Nota 1: {nota1:.2f}\nNota 2: {nota2:.2f}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito:.2f}")
print(f"Resultado: {resultado:.2f}")