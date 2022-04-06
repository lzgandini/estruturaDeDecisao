"""
#12 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) 
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
         Salário Bruto: (5 * 220)        : R$ 1100,00
         (-) IR (5%)                     : R$   55,00
         (-) INSS ( 10%)                 : R$  110,00
         FGTS (11%)                      : R$  121,00
         Total de descontos              : R$  165,00
         Salário Liquido                 : R$  935,00
"""

valorHora = float(input("Informe quanto você ganha por hora: "))
horasDia = float(input("Informe quantas horas você trabalha por dia: "))
horasMes = horasDia * 20
salarioBruto = valorHora * horasMes

if salarioBruto <= 900:
    iR = 0
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11

elif salarioBruto > 900 and salarioBruto <= 1500:
    iR = salarioBruto * 0.05
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11

elif salarioBruto > 1500 and salarioBruto <= 2500:
    iR = salarioBruto * 0.05
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11

else:
    iR = salarioBruto * 0.05
    inss = salarioBruto * 0.1
    fgts = salarioBruto * 0.11

totalDeDescontos = iR + inss
salarioLiquido = salarioBruto - totalDeDescontos

print(f"Salário Bruto:                    : R$   {salarioBruto}")
print(f"(-) IR (5%)                       : R$   {iR}")
print(f"(-) INSS ( 10%)                   : R$   {inss}")
print(f"FGTS (11%)                        : R$   {fgts}")
print(f"Total de descontos                : R$   {totalDeDescontos}")
print(f"Salário Liquido                   : R$   {salarioLiquido}")
