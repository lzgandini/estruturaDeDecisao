"""
#26 Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro
 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool,G-gasolina)
Calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o preço do litro do álcool é R$ 1,90.
"""

print("POSTO SONHO BRASILEIRO\n")

combustivel = (input("Informe qual combustível foi vendido (A-álcool e G-gasolina): ")).upper()
litros = float(input("Quantos litros foram vendidos? "))
precoGasolina = 2.5
precoAlcool = 1.9

if combustivel == "A":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco = litros * precoAlcool
else:
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco = litros * precoGasolina

precoTotal = preco - (preco * desconto)
print(f"O preço total é R$ {precoTotal}")
