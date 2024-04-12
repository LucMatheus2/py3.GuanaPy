# Algoritmo : Calcula o dobro, triplo e a raiz quadrada
# Autor : Lucas Matheus Costa
# Belém, ???/2017

# Importação
from math import sqrt

# Entrada de dados
numero = int(input("Digite um número inteiro :"))

# Saida de dados
print("Dobro : {} \nTriplo : {} \nRaiz quadrada : {:.1f}".format(numero*2,numero*3,sqrt(numero)))
