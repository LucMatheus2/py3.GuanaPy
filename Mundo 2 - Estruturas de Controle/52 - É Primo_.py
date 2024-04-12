# Algoritmo : É Primo?
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20

# Variáveis e Entrada de dados
numero = int(input("Digite um número : "))
isPrimo = False
cont = 0

# Processamento
for i in range(1,numero+1):
    if(numero%i == 0):
        cont+=1
        if (cont == 2):
            isPrimo = True
        else:
            isPrimo = False
            
# Saída de dados
if (isPrimo):
    print("O Número é Primo")
else:
    print("O Número NÃO é Primo")