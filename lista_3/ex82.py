# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
##Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.##
n_tabuada = int(input("\nDigite o número para fazer a tabuada: "))
n_inicial = int(input("Iniciar a tabuada no : "))
n_final = int(input("Finalizar a tabuada no : "))

caminho = n_inicial

for i in range(n_inicial, n_final + 1):
    print(f"{n_tabuada}  X  {caminho}  =  {n_tabuada * caminho}")
    caminho += 1