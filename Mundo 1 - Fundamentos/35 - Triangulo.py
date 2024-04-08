'''
# Algoritmo : Triângulo!
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Bibliotecas
import os

#Entrada de dados
reta1 = int(input('Digite o valor da reta 1 :'))
reta2 = int(input('Digite o valor da reta 2 :'))
reta3 = int(input('Digite o valor da reta 3 :'))
confirmacaoDoTriangulo = 0
isTriangulo = False

#Processamento
os.system("clear")

if (reta1 < reta2+reta3 and reta1 > abs(reta2-reta3)):
    confirmacaoDoTriangulo+=1
if (reta2 < reta1+reta3 and reta2 > abs(reta1-reta3)):
    confirmacaoDoTriangulo+=1
if (reta3 < reta2+reta1 and reta3 > abs(reta2-reta1)):
    confirmacaoDoTriangulo+=1
if (confirmacaoDoTriangulo == 3):
    isTriangulo = True

#Saida de dados - FORMA UM TRIÂNGULO
if (isTriangulo):
    print("Forma um triângulo")
else:
    print("Não forma um triângulo")