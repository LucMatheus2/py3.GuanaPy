'''
# Algoritmo : Menu
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''

#Variáveis e entrada
numero1 = int(input("\033[32mDigite um número : "))
numero2 = int(input("Digite outro número : "))
maior = 0
print("="*30)
opcaoDoMenu = 0
#Loop
while opcaoDoMenu != 5:
	print("""
	=======================
	| CALCULADORA SIMPLES |
	=======================
	| 1 | - Adição        |
	=======================
	| 2 | - Multiplicação |
	=======================
	| 3 | - Qual o maior? |
	=======================
	| 4 | - Novos números |
	=======================
	| 5 | - Encerrar      |
	=======================""")
	opcaoDoMenu = int(input("Qual a sua opção : "))
	print("="*30)

	#Opção 1 do menu - Adição
	if opcaoDoMenu == 1:
		print("{} + {} = {}".format(numero1,numero2,numero1+numero2))
	
	#Opção 2 do menu - Multiplicação
	elif opcaoDoMenu == 2:
		print("{} * {} = {}".format(numero1,numero2,numero1*numero2))
	
	#Opção 3 - Qual o número maior
	elif opcaoDoMenu == 3:
		if numero1>numero2:
			maior = numero1
		elif numero2>numero1:
			maior = numero2
			
		if (numero1 == numero2):
			print("Os dois são iguais")
		else:
			print("O maior número é o {}".format(maior))
	
	#Opção 4 - Novos Números
	elif opcaoDoMenu == 4:
		numero1 = int(input("Digite um novo valor para o 1º número : "))
		numero2 = int(input("Digite um novo valor para o 2º número : "))
	
	#Opção 5 - Fechar
	elif opcaoDoMenu == 5:
		print("Encerrando...")
	
	#Opção 6 ou outras - Não existe
	else:
		print("OPÇÃO INVALIDA")
print("(C) 2019 - Teclucas98")