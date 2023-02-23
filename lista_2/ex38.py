# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.
nota1 = input('Digite sua nota: ')
nota2 = input('Digite sua 2° nota: ')

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:     
    print ("Aprovado") 
elif media >= 10:
    print ("Você foi Aprovado com Distinção!")
else:
    print ("Reprovado")