# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
qtd_temperaturas = int(input("Quantas temperaturas: "))
temperaturas = []
qtd_temperatura = 1
for i in range(qtd_temperaturas):
    print("Temperatura n° ", qtd_temperatura)
    temperatura = temperaturas.append(float(input("Digite a temperatura: ")))
    qtd_temperatura += 1

print("Maior temperatura = ", max(temperaturas))
print("Menor temperatura = ", min(temperaturas))
print("Média = ", round(sum(temperaturas) / len(temperaturas), 2))