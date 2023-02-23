# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def executar(n, lista):
    for i in range(n):
         lista += str(i + 1) + "\t"     # \t é igual à TAB no teclado
         print(lista)
lista = ''
n = int(input("Digite n: "))
executar(n, lista)