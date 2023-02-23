# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:
# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
opcao = 10
lista_opcoes = 6*[0]
num_votos = 0
while opcao != 0:    
    opcao = int(input("Digite a opção de sistema opercional utilizado na sua organização:\n1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro\nOpção escolhida:  "))
    
    if opcao > 6 or num_votos < 0:
        print("Número inválido, tente outra opção!")
    elif opcao == 0:
        print("\nPesquisa finalizada!")
        break
    else:
        lista_opcoes[opcao-1] = lista_opcoes[opcao-1] + 1 
        num_votos = num_votos + 1   

opcoes = ["Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro"]



melhor = 0
print("Sistema Operacional     Votos  %")
print("----------------------------------")
for idx in range(len(lista_opcoes)):
    porcentagem = (lista_opcoes[idx]/num_votos)*100
    print(f'{opcoes[idx]}   -  {str(lista_opcoes[idx])}  -  {porcentagem:.2f}')
    if lista_opcoes[idx] > lista_opcoes[melhor]:
        melhor = idx
    
        
    

    
print(f"\nTotal de votos: {num_votos}")
porcentagem_melhor = (lista_opcoes[melhor]/num_votos)*100
print(f"O Sistema Operacional mais votado foi o {opcoes[melhor]}, com {lista_opcoes[melhor]} votos, correspondendo a {porcentagem_melhor:.2f}")