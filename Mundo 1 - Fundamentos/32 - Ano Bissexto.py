'''
# Algoritmo : Ano Bissexto
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Entrada
ano = int(input("Qual o ano de hoje :"))

#Processamento e Saída
if ano%4==0:
    print("É um ano bissexto")
else:
    print("É um ano comum")