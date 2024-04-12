# Algoritmo : Jogo do Gênio
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19

# Bibliotecas
from random import randint

# Entrada de dados
numeroDoUsuario = int(input("Estou pensando em um número entre 0 e 5, qual o número :"))

# Processamento
numeroDoComputador = randint(0,5)

# Saída de dados
if (numeroDoUsuario == numeroDoComputador):
    print("Parabéns, você acertou")
else:
    print("Errou, o número que eu pensei era o {}".format(numeroDoComputador))