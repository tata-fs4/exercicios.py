# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

while nome == senha:
    print("A senha definida não pode ser igual ao nome de usuário!")
    senha = input("Digite a senha: ")