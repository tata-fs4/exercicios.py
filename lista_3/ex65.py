# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
lista = []
count = 0

quantidade = int(input("Digite a quantidade de número que deseja: "))
while quantidade != count:
    numero = float(input("Digite um número: "))

    while numero > 1000 or numero < 0:
        numero = float(input("Digite um número: "))

    lista.append(numero)
    count += 1

maior = max(lista)
menor = min(lista)
print(f"Lista:{lista} " f"\nMaior: {maior}" f"\nMenor:{menor} ")
print(f"Soma: {sum(lista)}")