# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
populaçãoA=float(input("informe a população da país A "))
populaçãoB=float(input("informe a população da país B "))
ano=0
taxa_crescimentoA=float(input("informe a taxa de crescimento da população da país A "))
taxa_crescimentoB=float(input("informe a taxa de crescimento da população da país B "))
while populaçãoA < populaçãoB:
	populaçãoA+=round((populaçãoA*taxa_crescimentoA)/100)
	populaçãoB+=round((populaçãoB*taxa_crescimentoB)/100)
	ano=ano+1

print(f"levará {ano} anos para população da país A ser maior que a país B")
print(f"populaçãoB: {populaçãoB} habitantes")
print(f"populaçãoA: {populaçãoA} habitantes")