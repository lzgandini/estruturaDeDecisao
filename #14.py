"""
#14 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de c
onceitos obedece à tabela abaixo:

  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o 
conceito for D ou E.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
elif media < 4:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    aprovacao = "APROVADO"
else:
    aprovacao = "REPROVADO"

print(f"Suas notas foram {nota1} e {nota2}")
print(f"A média final ficou em {media} pontos")
print(f"Você obtece o conceito {conceito} e está {aprovacao}")
