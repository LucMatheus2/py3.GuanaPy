'''
# Algoritmo : Calculo de Fatorial
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''

#Entrada
fatorial = int(input("\033[32mDigite um número para mostrar o seu fatorial : "))
produtoTotal = 0

#Processamento
produtoTotal = fatorial
print ("{}! = ".format(fatorial))
while fatorial >= 1:
	print(fatorial, end="x")
	if produtoTotal != fatorial:
		produtoTotal = produtoTotal * fatorial
	fatorial-=1
	
#Sair
print("\n=================")
print("O produto do fatorial é {}".format(produtoTotal))