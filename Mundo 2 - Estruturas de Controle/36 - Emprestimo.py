'''
# Algoritmo : Empréstimo
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''

#Apresentação
print("=== PROGRAMA DE EMPRÉSTIMO ===")

#Entrada de dados
valorDaCasa = float(input("Quanto é o valor da casa? (Em R$) : "))
salarioDoComprador = float(input("Qual o seu salário? (Em R$) : "))
periodoDeCompra = int(input("Em quantos anos você irá pagar? : "))
mensagem = ""

#Processamento
valorDaPrestacao = valorDaCasa / (periodoDeCompra*12)
if valorDaPrestacao > (0.3*salarioDoComprador) :
	mensagem = "\033[1;7;31mEMPRÉSTIMO RECUSADO"
else:
	mensagem = "\033[1;7;32mEMPRÉSTIMO APROVADO"
mensagem += "\033[m"

#Saida de dados
print(mensagem)
print(" (c) 2019-20 - Lucas Matheus Costa (Luk)")
