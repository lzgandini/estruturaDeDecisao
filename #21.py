"""
#21 Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão 
fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar
com a quantidade de notas existentes na máquina.

 Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
 Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""

valor = input("Quanto você deseja sacar? ")

saqueMin = 10
saqueMax = 600
#sacar entre 10 e 600 reais

if int(valor) >= saqueMin and int(valor) <= saqueMax:
    digito1 = int(valor[0])
    digito2 = int(valor[1])
    digito3 = int(valor[2])

    if digito1 > 0:
        sentenca1 = f"{digito1} notas de 100"
    else:
        sentenca1 = ""

    if digito2 > 0:
        if digito2 < 5:
            sentenca2 = f"{digito2} notas de 10"
        elif digito2 == 5:
            sentenca2 = "1 nota de 50"
        else:
            notaDeDez = digito2 - 5
            sentenca2 = f"1 nota de 50\n{notaDeDez} notas de 10"
    else:
        sentenca2 = ""

    if digito3 > 0:
        if digito3 < 5:
            sentenca3 = f"{digito3} notas de 1"
        elif digito3 == 5:
            sentenca3 = "1 nota de 5"
        else:
            notaDeUm = digito3 - 5
            sentenca3 = f"1 nota de 5\n{notaDeUm} notas de 1"
    else:
        sentenca3 = ""

    print("\n".join([sentenca1, sentenca2, sentenca3]))
else:
    print("Valor fora do limite de saque, que deve ser entre R$ 10,00 e R$ 600,00.")
