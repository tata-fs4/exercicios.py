# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
def somar(a,b,c):
    print(f"soma = {a+b+c}")

valor = []
for i in range(3):
    print(f"\nArgumento n° {i+1}")
    argumento = valor.append(int(input("valor: ")))

somar(valor[0],valor[1],valor[2])