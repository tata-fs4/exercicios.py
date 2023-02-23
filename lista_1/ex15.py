# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
# 
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
qnt_ganha = float(input("Quanto ganha por hora? "))
horas_trabalhadas = int(input("Horas trabalhadas por mês: "))

salario_bruto = qnt_ganha * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print (f"\n-Salário Bruto : R$ {salario_bruto}")
print (f"\n- IR: R$ {ir}")
print (f"\n- INSS: R$ {inss}")
print (f"\n- Sindicato: R$ {sindicato}")
print (f"\nSalário Liquido: R$ {(salario_bruto - ir - inss - sindicato)}")