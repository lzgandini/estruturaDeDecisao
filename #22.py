#22 Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

numero = int(input("Digite um número inteiro: "))

if numero % 2 != 0:
    print(f"{numero} é ímpar.")
else:
    print(f"{numero} é par.")
