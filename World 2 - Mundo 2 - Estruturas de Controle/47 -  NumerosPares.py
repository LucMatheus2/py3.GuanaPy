'''
# Algoritmo : Contagem pro Ano Novo
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20
'''
#Entrada
pares = int(input("\033[32mDigite um número para descobrir todos os pares :"))

#Processamento e Saída
for i in range(1,pares+1):
    if(i%2 == 0):
        print(i)
print("(C) 2019-20 - Teclucas98")