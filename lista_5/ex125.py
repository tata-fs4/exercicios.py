# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def somar(a,b,c):
    print(f"soma = {a+b+c}")

valor = []
for i in range(3):
    print(f"\nArgumento n° {i+1}")
    argumento = valor.append(int(input("valor: ")))

somar(valor[0],valor[1],valor[2])