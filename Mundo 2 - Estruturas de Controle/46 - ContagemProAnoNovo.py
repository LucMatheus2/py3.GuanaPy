# Algoritmo : Contagem pro Ano Novo
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20

# Importação de bibliotecas
import time

# Contagem regressiva
for segundos in range(10,0,-1):
    print("=====")
    print(":{}".format(segundos))
    time.sleep(1)
print("Feliz Ano Novo")