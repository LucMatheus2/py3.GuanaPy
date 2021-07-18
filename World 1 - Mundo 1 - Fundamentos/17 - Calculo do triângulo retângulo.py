'''
# Algoritmo : calculo da hipotenusa do triângulo retângulo.
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''
#bibliotecas
from math import sqrt

#Entrada de dados
catetoOposto = float(input("Qual o valor do cateto oposto :"))
catetoAdjacente = float(input("Qual o valor do cateto adjacente :"))

#Processamento
hipotenusa = catetoOposto**2 + catetoAdjacente**2
hipotenusa = sqrt(hipotenusa)

#Saida de dados
print("O Valor da hipotenusa é {:.2f}".format(hipotenusa))