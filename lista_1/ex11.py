# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

ni = int(input("Diga um número inteiro: "))
ni2 = int(input("Diga outro número inteiro:" ))
nr = float(input("Diga um número real: "))
p = (ni * 2) + ni2
s = (ni * 3) + nr
c = nr ** 3
print(f"O produto do dobro do primeiro com metade do segundo é {p},")
print(f"a soma do triplo do primeiro com metade do segundo é {s},")
print(f"o terceiro elevado ao cubo é {c}.")