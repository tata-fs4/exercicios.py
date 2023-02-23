# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
def pos_ou_neg(n):
    if n > 0:
        print('P')
    else:
        print('N')

arg = int(input("valor: "))
pos_ou_neg(arg)