'''
# Algoritmo : É maior idade?
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20
'''

#Importação de pacotes
import os
from datetime import date

#Constantes
LIMITE = 7 # <- Considerando 7 Pessoas
MAIOR_IDADE = 21 # <- E a maior idade como 21 anos

#Variaveis
hoje = date.today().year
quantidadeDeMenores = 0
quantidadeDeMaiores = 0

#Entrada de dados
for i in range(0,LIMITE):
    anoDeNascimento = int(input("Digite o seu ano de nascimento ({}/{}) : ".format(i+1,LIMITE)))
    #Processamento
    if (hoje - anoDeNascimento < MAIOR_IDADE):
        quantidadeDeMenores+=1
    else:
        quantidadeDeMaiores+=1
    os.system("clear")
    
#Saída de dados
print("""
=== RESULTADO FINAL ===
Idade referencial atual : {} Anos

Número de maiores : {} pessoas
Número de menores : {} pessoas""".format(MAIOR_IDADE,quantidadeDeMaiores,quantidadeDeMenores))
