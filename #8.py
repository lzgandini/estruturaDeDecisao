#8 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

print("Semana da Beleza no Guanabara!\n")

marcas = ["Dove", "Seda", "Loreal"]

shampoo1 = float(input(f"Informe o preço do shampoo {marcas[0]}: "))
shampoo2 = float(input(f"Informe o preço do shampoo {marcas[1]}: "))
shampoo3 = float(input(f"Informe o preço do shampoo {marcas[2]}: "))

menor = min(shampoo1, shampoo2, shampoo3)

if menor == shampoo1:
    print(f"Hoje é dia de comprar o {marcas[0]}")
elif menor == shampoo2:
    print(f"Hoje é dia de comprar o {marcas[1]}")
else:
    print(f"Hoje é dia de comprar o {marcas[2]}")
