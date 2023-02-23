# Faça um Programa que verifique se uma letra digitada é vogal ou consoante
alfa = input("Informe uma letra:").upper()

if alfa.isalpha():
    if alfa in "AEIOU":
        print("Vogal")
    else:
        print("Consoante")
else:
    print("Não é uma letra!")