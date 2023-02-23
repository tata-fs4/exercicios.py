# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
gabarito = []
respostas_aluno = []
notas_tiradas = []
print("\nProfessor: ")
for i in range(10):
    print("Questão: ", i + 1)
    resposta_certa = gabarito.append(input("Digite a alternativa correta: "))
n_aluno = 1
continuar = True
while continuar != 'n':
    print("\n" * 5)
    print(f"Aluno n° {n_aluno}:")
    respostas_aluno.clear()
    for i in range(10):
        print("Questão: ", i + 1)
        resposta_aluno = respostas_aluno.append(input("Escolha a alternativa: "))
    nota = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1
    notas_tiradas.append(nota)
    continuar = input("Outro aluno vai utilizar o sistema? [s/n] : ")
    n_aluno += 1
print(f"{len(notas_tiradas)} alunos utilizaram o sistema")
print(f"\nA maior nota tirada foi: {max(notas_tiradas)}")
print(f"A menor nota tirada foi: {min(notas_tiradas)}")
print(f"A media de notas da turma foi de:{sum(notas_tiradas) / len(notas_tiradas)}")
print(notas_tiradas)