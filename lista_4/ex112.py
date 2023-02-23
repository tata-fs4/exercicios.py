# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;
valores = []
media_alta = []
valores_7 = []
cont = 1
rep = True

while rep != 0:
    print(f"\nValor nº ",cont) 
    val = (int(input("\nDigite o valor: ")))
    if val == -1:
       break
    else:
       valores.append(val)
    cont += 1

print('\n' * 2)
print(f"Quantidade de valores: {len(valores)} \n")
print(f"Os valores: {valores} \n")
valores.reverse()                #invertendo a lista
print(f"Os valores na ordem inversa {valores} \n")
print(f"A soma dos valores: {sum(valores)}\n")

media = sum(valores) / len(valores)
valores.reverse()                #invertendo novamente para a posição original

for i in range(len(valores)):
    if valores[i] > media:
        media_alta.append(valores[i])
    if valores[i] < 7:
        valores_7.append(valores[i])

print(f"A média dos valores: {media} \n")
print(f"A quantidade de valores acima da média calculada: {media_alta} \n")
print(f"A quantidade de valores abaixo de sete: {valores_7} \n")
print(f"\nPrograma concluido!")