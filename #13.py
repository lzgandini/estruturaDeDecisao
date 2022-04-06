#13 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

diaNumero = int(input("Digite o dia da semana conforme o número (1-Domingo, 2- Segunda, etc.): "))

if diaNumero == 1:
    print("O dia de hoje é Domingo")
elif diaNumero == 2:
    print("O dia de hoje é Segunda")
elif diaNumero == 3:
    print("O dia de hoje é Terça")
elif diaNumero == 4:
    print("O dia de hoje é Quarta")
elif diaNumero == 5:
    print("O dia de hoje é Quinta")
elif diaNumero == 6:
    print("O dia de hoje é Sexta")
elif diaNumero == 7:
    print("O dia de hoje é Sábado")
else:
    print("Valor inválido")
