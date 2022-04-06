#18 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Informe uma data no formato dd/mm/aaaa: ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[8:11])


if dia > 0 and dia <= 31:
    if mes > 0 and mes <= 12:
        if ano > 0:
            print(f"{data} é uma data válida!")
else:
    print("Data inválida.")
