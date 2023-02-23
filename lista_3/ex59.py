# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
base=int(input("Base: "))
expoente=int(input("Expoente: "))

potencia=1

for count in range(expoente):
    potencia *= base
    count += 1

print(f"{base} ˆ {expoente} = {potencia}")