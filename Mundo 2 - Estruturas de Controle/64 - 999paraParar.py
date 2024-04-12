# Algoritmo : Somarização dos números, digite 999 para parar
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 05 de Janeiro de 2020

numero = soma = contagemDeNumeros = 0

print("Digite um número inteiro e Aperte [ENTER]")
print("(i) - Digite 999 para parar as solicitações")
print("====================")
while numero != 999:
    numero = int(input("Numero : "))
    if numero != 999:
        contagemDeNumeros += 1
        soma += numero
print("=================")
print("Contagem de números : {}".format(contagemDeNumeros))
print("Sumarização (Soma total) : {}".format(soma))
