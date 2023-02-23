# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
def moldura(linha, coluna):
    print('+','-' * (linha-2),'+')
    for i in range(coluna-2):
        print('|',' ' * (linha-2),'|')
    print('+','-' * (linha-2),'+')

print("\n[Criador de Moldura]\n")

linha = int(input("Digite a quantidade de linhas: "))
while linha < 1 or linha > 20:
    print("Valor da linha invalido, digite entre [1-20]")
    linha = int(input("Digite a quantidade de linhas: "))
coluna = int(input("Digite a quantidade de colunas: "))
while coluna < 1 or coluna > 20:
    print("Valor da coluna invalido, digite entre [1-20]")
    coluna = int(input("Digite a quantidade de colunas: "))

moldura(linha,coluna)