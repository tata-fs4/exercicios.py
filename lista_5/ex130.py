# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def contador(n):
    n = str(n)
    print(len(n))

num = int(input("Digite o numero: "))
contador(num)