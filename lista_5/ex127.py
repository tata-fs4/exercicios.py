# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto,custo):
    val_imposto = custo * taxaImposto / 100
    imposto_total = custo + val_imposto
    print(f"\nO imposto de {taxaImposto}% é de {val_imposto}\nO valor total é de {imposto_total}")

item =float(input("Digite o valor do item: "))
imposto =float(input("Digite o percentual do imposto: "))
somaImposto(imposto,item)