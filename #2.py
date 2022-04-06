#2 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("Escolha um número real: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print(f"O número é zero e não quero orbigá-lo a ser um ou outro!")
