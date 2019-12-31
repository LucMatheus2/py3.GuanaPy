'''
# Algoritmo : Contagem pro Ano Novo
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20
'''
#Importação de bibliotecas
import time
import os

#Contagem regressiva
for segundos in range(10,0,-1):
    os.system("clear")
    print(":{}".format(segundos))
    time.sleep(1)
print("Feliz Ano Novo")