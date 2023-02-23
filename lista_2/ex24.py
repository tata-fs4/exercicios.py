# Faça um Programa que leia três números e mostre o maior deles.
num1=int(input("Primeiro numero: "))
num2=int(input("Segundo numero: "))
num3=int(input("Terceiro numero: "))

if num1 > num2 and num1 > num3:
    print(f"O número um é o maior: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O número dois é o maior: {num2}")
elif num3 > num1 and num3 > num2:
    print(f"O número três é o maior: {num3}")