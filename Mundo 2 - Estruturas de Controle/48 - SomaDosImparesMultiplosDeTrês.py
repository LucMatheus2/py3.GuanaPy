# Algoritmo : Soma dos Multiplos de Três
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20

# Variaveis Globais
limite = 500
soma = 0

# Processamento
for i in range(0,limite+1):
    if(i%2 == 1 and i%3 == 0):
        soma += i
print("A Somatoria de todos os impares multiplos de três até {} é {}".format(limite,soma))