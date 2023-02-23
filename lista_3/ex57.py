# Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = 0
if n1 > n2:
    for intervalo in range(n2+1,n1):
        print(intervalo)
        soma = soma + intervalo

elif n1 < n2:
    for intervalo in range(n1+1,n2):
        print(intervalo)
        soma = soma + intervalo
else:
    print('Os numeros são iguais.')
print(f'A soma dos numeros foi de {soma}')