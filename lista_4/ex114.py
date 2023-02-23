# Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
colocado = 'Primeiro','Segundo','Terceiro','Quarto','Quinto'
melhor_salto = pior_salto = contagem = media_saltos = total_saltos = media= 0
atleta = ' '
while atleta != '':
    atleta = input("Atleta: ")
    if atleta == '':
        break
    for c in range(0, 5):
        salto = float(input(f"{colocado[c]} salto: "))
        contagem += 1
        media_saltos += 1
        if salto > melhor_salto:
            melhor_salto = salto
        if salto < pior_salto or contagem == 1:
            pior_salto = salto
        total_saltos += salto
        media = total_saltos / media_saltos

print('\n'+("="*30))
print(f"Melhor salto: {melhor_salto}")
print(f"Pior salto: {pior_salto}")
print(f"Media dos demais saltos: {media:.2f}")
print("\n")
print("Resultado final: ")
print(f"{atleta}: {media:.2f}")