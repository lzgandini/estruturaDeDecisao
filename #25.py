"""
#25 Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
 O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""

print("Responda sim ou não para as perguntas abaixo:\n")

telefonou = input("Telefonou para a vítima? ")
esteveNoLocal = input("Esteve no local do crime? ")
moraPerto = input("Mora perto da vítima? ")
deviaDinheiro = input("Devia para a vítima? ")
trabalhouJunto = input("Já trabalhou com a vítima? ")

respostas = [telefonou.upper(), esteveNoLocal.upper(), moraPerto.upper(), deviaDinheiro.upper(), trabalhouJunto.upper()]

respostasAfirmativas = respostas.count("SIM")
if respostasAfirmativas == 2:
    status = "Suspeita"
elif respostasAfirmativas == 3 or respostasAfirmativas == 4:
    status = "Cúmplice"
elif respostasAfirmativas == 5:
    status = "Assassino"
else:
    status = "Inocente"

print(f"\n{status}")
