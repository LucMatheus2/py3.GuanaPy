'''
# Algoritmo : Jogo do Gênio
# Versão 2.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Bibliotecas
from random import randint
contador = 0

#Entrada de dados
numeroDoUsuario = int(input("Estou pensando em um número entre 0 e 10, qual o número :"))

#Processamento
numeroDoComputador = randint(0,10)

while numeroDoUsuario!=numeroDoComputador:
	print("="*20)
	contador +=1
	if numeroDoUsuario>numeroDoComputador:	
		print("O número é menor que {}".format(numeroDoUsuario))
	elif numeroDoUsuario<numeroDoComputador:
		print("O número é maior que {}".format(numeroDoUsuario))
	numeroDoUsuario = int(input("Digite outro número : "))

#Saída de dados
print("="*20)
if (numeroDoUsuario == numeroDoComputador):
    print("Parabéns, você acertou, de {} tentativas".format(contador))