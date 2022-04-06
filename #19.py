"""
#19 Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
 Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
 
 a)326 = 3 centenas, 2 dezenas e 6 unidades
 b)12 = 1 dezena e 2 unidades
 
 Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""

numeros = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

i = 0
while i < len(numeros):
    unitarioInt = numeros[i]
    unitarioStr = str(unitarioInt)

    if unitarioInt == 1:
        print(f"{unitarioStr} = {unitarioStr} unidade")
    elif unitarioInt > 1 and unitarioInt < 10:
        print(f"{unitarioStr} = {unitarioStr} unidades")
    elif unitarioInt >= 10 and unitarioInt < 100:
        print(f"{unitarioStr} = {unitarioStr[0]} dezenas e {unitarioStr[1]} unidades")
    else:
        print(f"{unitarioStr} = {unitarioStr[0]} centenas, {unitarioStr[1]} dezenas e {unitarioStr[2]} unidades")
    i += 1
