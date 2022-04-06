#9 Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

todosOsNumeros = [numero1, numero2, numero3]
todosOsNumeros.sort(reverse=True)

print(f"A ordem decrescente dos números é {todosOsNumeros[0]}, {todosOsNumeros[1]} e {todosOsNumeros[2]}.)
