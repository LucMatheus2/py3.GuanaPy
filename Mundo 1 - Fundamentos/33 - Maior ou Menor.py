# Algoritmo : Maior número ou menor número
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19

# Entrada de dados
numero1 = float(input("Digite um número :"))
numero2 = float(input("Digite outro número :"))
numero3 = float(input("Digite mais um número :"))

# Processamento
lista = [numero1,numero2,numero3]
lista.sort()

# Saída de dados
print("O Maior número é : {}".format(lista[2]))
print("O Menor número é : {}".format(lista[0]))