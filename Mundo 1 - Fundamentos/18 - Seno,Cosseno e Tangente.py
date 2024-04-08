'''
# Algoritmo : Calculo de Seno,Cosseno e Tangente
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''

#Bibliotecas
from math import sin,cos,tan,radians

#Entrada de dados
angulo = float(input("Qual o valor do ângulo :"))

#Processamento
angulo = radians(angulo)

senoDoAngulo = sin(angulo)
cossenoDoAngulo = cos(angulo)
tangenteDoAngulo = tan(angulo)

#Saída de dados
print("Seno : {:.2f}".format(senoDoAngulo))
print("Cosseno : {:.2f}".format(cossenoDoAngulo))
print("Tangente : {:.2f}".format(tangenteDoAngulo))