# Algoritmo : 999 para Parar :D
# Versão 2.0
# Autor: Lucas Matheus Costa
# OBS: É possivel com teste lógico simples, este visa apenas usando o break 
# que é possível com alguns ifs
# Belém: 05 de Janeiro de 2020

numero = soma = contagemDeNumeros = 0

print("Digite um número inteiro e Aperte [ENTER]")
print("(i) - Digite 999 para parar as solicitações")
print("====================")
while True:
    numero = int(input("Numero : "))
    if numero != 999:
        contagemDeNumeros += 1
        soma += numero
    else:
        break
print("=================")
print("Contagem de números : {}".format(contagemDeNumeros))
print("Sumarização (Soma total) : {}".format(soma))