"""
#11 As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
 Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
 
 a)salários até R$ 280,00 (incluindo) : aumento de 20%
 b)salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
 c)salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
 d)salários de R$ 1500,00 em diante : aumento de 5%
 
 Após o aumento ser realizado, informe na tela:
 e)o salário antes do reajuste;
 f)o percentual de aumento aplicado;
 g)o valor do aumento;
 h)o novo salário, após o aumento.
"""

salarioInicial = float(input("Qual é o teu salário? "))

if salarioInicial <= 280:
    percentual = 0.2
    aumento = salarioInicial * percentual
    salarioAumentado = salarioInicial + aumento

elif salarioInicial > 280 and salarioInicial <= 700:
    percentual = 0.15
    aumento = salarioInicial * percentual
    salarioAumentado = salarioInicial + aumento

elif salarioInicial > 700 and salarioInicial <= 1500:
    percentual = 0.1
    aumento = salarioInicial * percentual
    salarioAumentado = salarioInicial + aumento

else:
    percentual = 0.05
    aumento = salarioInicial * percentual
    salarioAumentado = salarioInicial + aumento

print(f"- Seu salário era inicialmente de R$ {salarioInicial}.")
print(f"- Você recebeu um aumento de R$ {percentual}, que dá R$ {aumento}")
print(f"- Seu novo salário é de R$ {salarioAumentado}.")
