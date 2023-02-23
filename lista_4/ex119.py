# Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
# necessita da esfera;
# necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
# Quantidade de mouses: 100

# Situação                        Quantidade              Percentual
# 1- necessita da esfera                  40                     40%
# 2- necessita de limpeza                 30                     30%
# 3- necessita troca do cabo ou conector  15                     15%
# 4- quebrado ou inutilizado              15                     15%
print('Defeitos:\n1 - Necessita de Esfera\n2 - Necessita de limpeza\n3 - Necessita troca de cabo ou conector\n4 - Quebrado ou inutilizado')
defeitos_ = ['Necessita de Esfera','Necessita de limpeza','Necessita troca de cabo ou conector','Quebrado ou inutilizado']


num_mouses = int(input("Quantos mouses defeituosos existem: "))
defeitos = 4*[0]

print('')
for idx in range(num_mouses):
    
    validacao = True
    while validacao:
        defeito = int(input("Qual o código do problema do mouse "+str(idx+1)+": "))
        if (defeito == 1) or (defeito == 2) or (defeito == 3) or (defeito == 4):
            validacao = False
        else:
            print("Número inválido, tente outro!")
    defeitos[defeito-1] = defeitos[defeito-1] + 1

for idx in range(len(defeitos_)):
    print(defeitos_[idx]+" - " +str(defeitos[idx])+ " defeitos - " +str(defeitos[idx]*100/num_mouses)+"%" )