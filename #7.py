#7 Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f"O maior número é o {maior} e o menor é o {menor}")
