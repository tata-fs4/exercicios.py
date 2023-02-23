# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd':
print("Utilize letras minúsculas :)")

nome=""
while (len(nome) <=  2):
	nome = input("Minimo 3 letras - Informe um nome: ")

#Idade: entre 0 e 150;

idade = int(input("Válido entre 0 e 150 - Informe a idade: "))
while ( idade >= 150 or idade < 0 ):
	idade=int(input("Válido entre 0 e 150 - Informe a idade: "))
	
	
#Salário: maior que zero;
salario=float(input("Informe um salário: "))
while ( salario < 0 ):
	salario=float(input("Informe um salário: "))
	
#Sexo: 'f' ou 'm';

sexo=""
while  ( sexo !="f" and sexo !="m" ):
	sexo = input("f ou m - Informe a inicial do seu sexo: ").lower()
	
#Estado Civil: 's', 'c', 'v', 'd';

estado_civil=""
while ( estado_civil !="s" and estado_civil !="c" and estado_civil !="v" and estado_civil !="d" ):
	estado_civil=input("s - Solteiro(a), c - Casado(a), v - Viúvo(a), d - Divorciado(a) - Informe a inicial do seu estado civil: ").lower()