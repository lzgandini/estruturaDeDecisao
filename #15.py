"""
#15 Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, 
se o mesmo é: equilátero, isósceles ou escaleno.

Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

lado1 = float(input("Informe o primeiro lado do triângulo: "))
lado2 = float(input("Informe o segundo lado do triângulo: "))
lado3 = float(input("Informe o terceiro lado do triângulo: "))

if (lado1 + lado2) > lado3:
    triangulo = True
elif (lado1 + lado3) > lado2:
    triangulo = True
elif (lado2 + lado3) > lado1:
    triangulo = True
else:
    triangulo = False

if triangulo == True:
    if lado1 == lado2 == lado3:
        print("É um triângulo Equilátero!")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo Isósceles!")
    else:
        print("É um triângulo Escaleno")
else:
    print("Não é um triângulo!")
