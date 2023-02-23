# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
quant_cds = int(input("Quantidade de CD's: "))
cds = []
n_cd = 1

for i in range(quant_cds):
    print(f"CD número {n_cd}")
    valor_cd = cds.append(float(input("Digite o valor do CD: ")))
    n_cd += 1

media_cd = sum(cds) / len(cds)
print(f"A media para cada CD é: {media_cd}")