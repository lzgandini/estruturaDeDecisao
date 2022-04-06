"""
#16 Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer 
as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""

import math

print("Equação de Segundo Grau")
a = float(input("Informe o valor de A: "))
b = float(input("Informe o valor de B: "))
c = float(input("Informe o valor de C: "))

if a == 0:
    print("Como não há valor de A, é uma Equação de Primeiro Grau. Não é possível continuar o cálculo.")
else:
    delta = pow(b, b) - (4 * a * c)
    if delta < 0:
        print("A equação não possui raízes reais. Não é possível continuar o cálculo.")
    elif delta == 0:
        print("A equação possui apenas uma raiz real, que é zero.")
    else:
        raizDelta = math.sqrt(delta)
        x1 = (-b + raizDelta) / (2 * a)
        x2 = (-b - raizDelta) / (2 * a)
        print(f"A equação possui duas raízes reais, {x1} e {x2}")
