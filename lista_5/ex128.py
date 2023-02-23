# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
def conversor(hora24):
    if hora24 == 24:
        hora12 = 0
    elif hora24 > 12:
        hora12 = hora24 - 12
    else:
        hora12 = hora24
    return hora12 
       
def saida(hora12,minuto12):
    if hora12 < 10:
        Tset = 'A'
        hora12 = '0' + str(hora12)
    else:
        Tset = 'P'
    
    if minuto12 < 10:
        minuto12 = '0' + str(minuto12)
    
    print(f'hora {hora12}:{minuto12} {Tset}') 

print("\n[Conversor de horas 24 para 12]")
while True:
    hora = int(input("\nDigite as horas: "))
    while hora > 24 or hora < 0:
        print("[Valor invalido!]")
        hora = int(input("Digite as horas: "))

    minuto = int(input("Digite as os minutos: "))    
    while minuto > 60 or minuto < 0:
        print("[Valor invalido!]")
        minuto = int(input("Digite as os minutos: "))

    hora12 = conversor(hora)
    saida(hora12,minuto)
    
    #repetidor de confirmação
    confirmador = str(input("\nDeseja inserir uma nova hora? [s/n]: "))
    while confirmador != 's' and confirmador != 'n':
        print("[Valor invalido!]")
        confirmador = str(input("\nDeseja inserir uma nova hora? [s/n]: "))
    if confirmador == 'n':
        break
    else:
        continue