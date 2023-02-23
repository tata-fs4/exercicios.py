# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso(n):
    numeroInvertido = int(str(n)[::-1])
    print(numeroInvertido)
n = int(input("Digite o número: "))
reverso(n)