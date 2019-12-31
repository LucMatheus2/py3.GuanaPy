'''
# Algoritmo : Conversor de números para binario, octal e hexadecimal
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Entrada de dados
print("== CONVERSOR DE NÚMEROS ==")
numeroAleatorio = int(input("Digite um número inteiro e aperte ENTER : "))
opcao = int(input("""\033[32m
Qual a base númerica de conversão:

[1] - Binário
[2] - Octal
[3] - Hexadecimal

Digite a opção : """))

#Processamento e Saida
if (opcao == 1) :
    print("O número em binário é {}".format(bin(numeroAleatorio)))
elif (opcao == 2):
    print("O número em octal é {}".format(oct(numeroAleatorio)))
elif (opcao == 3):
    print("O número em hexadecimal é {}".format(hex(numeroAleatorio)))
else:
    print("\033[1;7;31mOPÇÃO INVÁLIDA, LEIA O MENU NOVAMENTE E DIGITE ALGUMA DAS OPÇÕES INDICADAS")
print("\033[mObrigado por utilizar!")
print("(C) 2019 - Tecluca98")