# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
lista_caract = []
consoantes = 0
print ("Informe os caracteres")
for i in range(1, 11):
	lista_caract.append(input(f"Caracter {i}:").lower())
for caracter in lista_caract:
    if caracter not in ["a", "e", "i", "o", "u"]:
        consoantes += 1
try:
    lista_caract.remove('a')
except:
    pass
try:
    lista_caract.remove('e')
except:
    pass
try:
    lista_caract.remove('i')
except:
    pass
try:
    lista_caract.remove('o') 
except:
    pass
try:
    lista_caract.remove('u')
except:
    pass
print(f"Existem {consoantes} consoantes")
print(f"Essas consoantes são: {lista_caract}")
