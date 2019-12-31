'''
# Algoritmo : Jogo - Pedra,Papel e Tesoura :D
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Importação de pacotes
from random import choice

#Entrada
opcoes = ["Pedra","Papel","Tesoura"]
playerGanhou = False

escolhaDoJogador = input("Escolha : Pedra, Papel ou Tesoura? :")
escolhaDaMaquina = choice(opcoes)


#Regras
if escolhaDoJogador == "Pedra":
	if escolhaDaMaquina == "Tesoura":
		playerGanhou = True
	else:
		playerGanhou = False
elif escolhaDoJogador == "Papel":
	if escolhaDaMaquina == "Pedra":
		playerGanhou = True
	else:
		playerGanhou == False
elif escolhaDoJogador == "Tesoura":
	if escolhaDaMaquina == "Papel":
		playerGanhou = True
	else:
		playerGanhou = False
else:
	print("Esta opção não existe")

#Saída de dados
print("A MAQUINA ESCOLHEU {}".format(escolhaDaMaquina))
if playerGanhou:
	print("\033[1;7;32m VOCÊ VENCEU! ")
elif escolhaDaMaquina == escolhaDoJogador:
	print("\033[1;7;33m EMPATOU! ")
else:
	print("\033[1;7;31m VOCÊ PERDEU! ")

print("\033[m(C) 2019 - Teclucas98")
