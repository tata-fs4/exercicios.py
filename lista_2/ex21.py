#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
resposta=input('M ou F: ')

if resposta == 'M':
    print('Masculina')
else:
    if resposta == 'F':
          print('Feminina')
    else:
        print('Sexo Inválido')