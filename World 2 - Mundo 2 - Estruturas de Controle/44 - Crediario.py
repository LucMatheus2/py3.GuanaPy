'''
# Algoritmo : Crediário
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Importação de pacotes
import os

#Entrada de dados
precoDoProduto = input("Digite o preço do produto (em R$) : ")
precoDoProduto = float(precoDoProduto.replace(",","."))
precoAPagar = 0
print("""
    Qual a forma de pagamento?
    
    (D) - Dinheiro
    (C) - Cartão de Débito
    (CC) - Cartão de Crédito
    (CH) - Cheque

""")
opcaoEscolhida = input("Escolha a sua opçao : ")

#Processamento
if (opcaoEscolhida == "C" or opcaoEscolhida == "CC"):
    parcela = int(input("""Quantas parcelas?
        (1) - A Vista.
        (2 ou mais) - Parcelado no crediário.

        Digite : """))
    if parcela == 1:
        precoAPagar = precoDoProduto - 0.05*precoDoProduto
    elif parcela >= 3:
        precoAPagar = parcela*(precoDoProduto/(parcela*1.2))
else:
    precoAPagar = precoDoProduto - 0.1*precoDoProduto

#Saída de dados
print("=== CUPOM FISCAL ELETRÔNICO ===")
print("Valor da Compra : R$ {:.2f}".format(precoDoProduto))
if (precoAPagar-precoDoProduto > 0):
    print("Juros : R$ {:.2f}".format(precoAPagar-precoDoProduto))
print("Desconto : R$ {:.2f}".format(precoDoProduto-precoAPagar))
if(opcaoEscolhida == "C" or opcaoEscolhida == "CC"):
    print("Parcelas : {} x R$ {:.2f}".format(parcela,precoAPagar/parcela))
print("TOTAL A PAGAR : R$ {:.2f}".format(precoAPagar))
