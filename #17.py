#17 Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

from calendar import isleap

ano = int(input("Digite um ano com 4 dígitos: "))

if isleap(ano):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")
