"""
#27 Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

quilosMorangos = float(input("Quantos quilos de morango você comprou? "))
quilosMacas = float(input("Quantos quilos de macas você comprou? "))
quilosTotal = quilosMorangos + quilosMacas

if quilosMorangos < 5:
    precoMorangos = 2.5
else:
    precoMorangos = 2.2

if quilosMacas < 5:
    precoMacas = 1.8
else:
    precoMacas = 1.5

total = (quilosMorangos * precoMorangos) + (quilosMacas * precoMacas)

if quilosTotal >= 8 or total >= 25:
    total = total - (total * 0.1)

print(f"Conta: R$ {total}")
