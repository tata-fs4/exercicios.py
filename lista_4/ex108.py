# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
elementos = 10
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
for i in range(elementos):
    vetor1.append(int(input(f"Entre com o {i+1}º número inteiro para o vetor 1: ")))

for i in range(elementos):
    vetor2.append(int(input(f"Entre com o {i+1}º número inteiro para o vetor 2: ")))

for i in range(elementos) : vetor3.append(int(input(f"Entre com o {i+1}º número inteiro para o vetor 3: ")))

for i in range(elementos):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])

print("O vetor com os elementos intercalados dos vetores 1, 2 e 3 é: ")

for i in range(elementos * 3):
    print(vetor4[i], end=" ")