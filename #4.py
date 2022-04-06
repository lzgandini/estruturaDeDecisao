#4 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = (input("Digite uma letra: ")).lower()
vogais = "aeiou"

if letra in vogais:
    print("Você digitou uma vogal.")
else:
    print("Você digitou uma consoante.")
