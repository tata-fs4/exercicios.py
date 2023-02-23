#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math
    
print("Equaçao do 2o grau da forma: ax² + bx + c")
    
coef_a = float(input("Coeficiente a: "))

if(coef_a==0):
    print("Se a=0, não é equação do segundo grau.")
else:
    coef_b = float(input("Coeficiente b: "))
    coef_c = float(input("Coeficiente c: "))
delta = coef_b**2 - (4*coef_a*coef_c)

if delta<0:
    print("Delta menor que 0. Raízes imaginárias.")
elif delta==0:
    raiz = -coef_b / (2*coef_a)
    print(f"Delta=0 , raiz = {raiz}")
else:
    raiz1 = (-coef_b + math.sqrt(delta)) / (2*coef_a)
    raiz2 = (-coef_b - math.sqrt(delta)) / (2*coef_a)
print(f"Raizes: {raiz1} e {raiz2}")

#### 1
#### 2
#### -15

#### 6
#### 3.5
#### -1.4

# def get_float(input_message):
#     while True:
#         try:
#             return float(input(input_message))
#         except:
#             print("Insira um número Real!")

# def get_coef_a():
#     while True:
#         input_val = get_float("Coeficiente a: ")
#         if input_val != 0:
#             return input_val

# def get_coef_b():
#     return get_float("Coeficiente b: ")

# def get_coef_c():
#     return get_float("Coeficiente c: ")

# def calculate_delta(coef_a, coef_b, coef_c):
#     return pow(coef_b, 2) - (4 * coef_a * coef_c)

# def calculate_square(coef_a, coef_b, type = None, delta = None):
#     if not delta or not type:
#         return (-coef_b / (2 * coef_a))
#     elif type == "+":
#         return (-coef_b + pow(delta, 0.5)) / (2 * coef_a)
#     else:
#         return (-coef_b - pow(delta, 0.5)) / (2 * coef_a)

# def calculate_formula(coef_a, coef_b, coef_c):
#     delta = calculate_delta(coef_a, coef_b, coef_c)
#     if delta < 0:
#         return "Delta menor que 0. Raízes imaginárias."
#     elif delta == 0:
#         return f"Resultado: {calculate_square(coef_a, coef_b)}"
#     else:
#         return f"Resultados: {calculate_square(coef_a, coef_b, '+', delta)} e {calculate_square(coef_a, coef_b, '-', delta)}"

# print("Equaçao do 2o grau da forma: ax² + bx + c")
# print(calculate_formula(get_coef_a(), get_coef_b(), get_coef_c()))

#### 1
#### 2
#### -15

#### 6
#### 3.5
#### -1.4


# ------------- // ---------------------- // ------------------------

# import math

# def delta(coef_a,coef_b,coef_c):
#      return coef_b**2 - (4*coef_a*coef_c)

# def validaCoef(coef_a):
#     return coef_a != 0

# def calculoRaizZero(coef_a,coef_b):
#     raiz = -coef_b / (2*coef_a)
#     return print(f"Delta=0 , raiz = {raiz}")

# def calculoRaizez(coef_a, coef_b,calc_delta):
#     raiz1 = (-coef_b + math.sqrt(calc_delta)) / (2*coef_a)
#     raiz2 = (-coef_b - math.sqrt(calc_delta)) / (2*coef_a)
#     return print(f"Raizes: {raiz1} e {raiz2}")    

# coef_a = float(input("Coeficiente a: "))
# coef_b = float(input("Coeficiente b: "))
# coef_c = float(input("Coeficiente c: "))

# print("Equaçao do 2o grau da forma: ax² + bx + c")
# if validaCoef(coef_a):
#     calc_delta = delta(coef_a, coef_b, coef_c)
#     if calc_delta<0:
#         print("Delta menor que 0. Raízes imaginárias.")
#     elif calc_delta ==0:
#         calculoRaizZero(coef_a,coef_b)
#     else:
#         calculoRaizez(coef_a,coef_b,calc_delta)
# else:
#     print("valor de A invalido")
    
# ------------- // ---------------------- // ------------------------

