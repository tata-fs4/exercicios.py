# A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# alexandre       456123789
# anderson        1245698456
# antonio         123456456
# carlos          91257581
# cesar           987458
# rosemary        789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# ACME Inc.               Uso do espaço em disco pelos usuários
# ------------------------------------------------------------------------
# Nr.  Usuário        Espaço utilizado     % do uso

# 1    alexandre       434,99 MB             16,85%
# 2    anderson       1187,99 MB             46,02%
# 3    antonio         117,73 MB              4,56%
# 4    carlos           87,03 MB              3,37%
# 5    cesar             0,94 MB              0,04%
# 6    rosemary        752,88 MB             29,16%

# Espaço total ocupado: 2581,57 MB
# Espaço médio ocupado: 430,26 MB
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
def toMB(tamanho_em_bytes):
   tamanho_em_bytes = float(tamanho_em_bytes)
   return (float(tamanho_em_bytes/(1024*1024)))
   
def percentual_por_usuario(lista, total):
   percentual = (lista[3]/total)*100
   #percentual = f"{percentual:.2f}")
   lista.insert((len(cada_usuario)),percentual)

def espaco_medio_ocupado(lista, total):
   media = 0
   elementos = len(lista)
   media = (total)/(elementos+1)
   #media = f"{media:.2f}"
   return media

#MAIN
usuarios = []
posicao = 1
total = media = 0
with open ("usuarios.txt","r") as arquivo:
   valor = 0
   for linha in arquivo:
      usuarios.append(linha.split()) 

   for cada_usuario in usuarios:
      cada_usuario.insert(0,posicao)
      valor = toMB(float(cada_usuario[2]))
      total += valor
      cada_usuario.insert((len(cada_usuario)),valor)
      posicao+=1

   for cada_usuario in usuarios:
      percentual_por_usuario(cada_usuario, total)

media = espaco_medio_ocupado(cada_usuario,total)

with open ("relatorio.txt","w") as arquivo:
   arquivo.write("ACME Inc.               Uso do espaço em disco pelos usuários.\n")
   arquivo.write("--------------------------------------------------------------\n")
   arquivo.write("Nr.\tUsuário        \tEspaço utilizado\t% do uso\n\n")

   for cada_usuario in usuarios:
      percentagem= f"{round(cada_usuario[3],2):.2f}"
      arquivo.write(f"{cada_usuario[0]}\t{cada_usuario[1]:<15}\t{percentagem:<16}MB \t{cada_usuario[4]:.2f}%\n")

   arquivo.write(f"\nEspaço Total Ocupado: {total:.2f} MB")
   arquivo.write(f"\nEspaço Médio Ocupado: {media:.2f} MB")
   arquivo.close()

with open ("relatorio.txt","r") as arquivo:
   print(arquivo.read())