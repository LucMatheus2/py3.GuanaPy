'''
# Algoritmo : Aluguel de Carros
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''

#Constantes
precoDaDiariaDoCarro = 60
precoDoKmRodado = 0.15

#Entrada de dados
diasAlugados = int(input("Quantos dias foram alugados :"))
kmsRodados = float(input("Quantos quilometros foram rodados :"))

#Processamento
totalAPagar = diasAlugados * precoDaDiariaDoCarro # <- Incluindo o calculo da diaria
totalAPagar = totalAPagar + kmsRodados * precoDoKmRodado # <- Incluindo o calculo do quilometro rodado

#Saída de dados
print("O Total a pagar é R$ {:.2f}".format(totalAPagar))