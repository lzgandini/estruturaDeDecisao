"""
#28 O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente, receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tipoDaCarne = (input("Qual carne você deseja comprar? ")).upper()

if tipoDaCarne == "FILE DUPLO" or tipoDaCarne == "ALCATRA" or tipoDaCarne == "PICANHA":
    quilos = float(input("Quantos quilos? "))
    pagamentoCartaoTabajara = (input("O pagamento será feito no cartão Tabajara (sim/nao)? ")).upper()

    if tipoDaCarne == "FILE DUPLO":
        if quilos < 5:
            preco = 4.9
        else:
            preco = 5.8
    elif tipoDaCarne == "ALCATRA":
        if quilos < 5:
            preco = 5.9
        else:
            preco = 6.8
    else:
        if quilos < 5:
            preco = 6.9
        else:
            preco = 7.8

    precoTotal = quilos * preco

    if pagamentoCartaoTabajara == "SIM":
        desconto = precoTotal * 0.05
        tipoPagamento = "CARTÃO TABAJARA"
    else:
        desconto = 0
        tipoPagamento = "OUTRO"

    valorAPagar = precoTotal - desconto

    print("\n")
    print("Tipo da Carne:                     {}".format(tipoDaCarne))
    print("Quantidade de Carne:               {:.2f} kg".format(quilos))
    print("Preço Total:                       R$   {:.2f}".format(precoTotal))
    print("Tipo de Pagamento:                 {}".format(tipoPagamento))
    print("Valor do Desconto:                 R$   {:.2f}".format(desconto))
    print("Valor a pagar:                     R$   {:.2f}".format(valorAPagar))

else:
    print("Valor inválido!")
