# Algoritmo : Triângulo
# Versão 2.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19

# Bibliotecas
import os

# Variáveis
isTriangulo = False # boolean
tipoDoTriangulo = "" # string

confirmacaoDoTriangulo = 0 # integer
triangulo = ["0","0","0"] # Array(3) <integer>
destaque = 0 # integer
ladosIguais = 0 # integer

# Entrada de dados
try:
    for i in range(0,3):
        triangulo[i] = int(input("Digite um valor para um lado : "))
except ValueError:
    print("\033[1;7;31mNÃO DIGITE LETRAS, APENAS NÚMEROS!")

# Processamento
os.system("clear")

# É Triângulo
try:
    if (triangulo[0] < triangulo[1]+triangulo[2] and triangulo[0] > abs(triangulo[1]-triangulo[2])):
        confirmacaoDoTriangulo+=1
    if (triangulo[1] < triangulo[0]+triangulo[2] and triangulo[1] > abs(triangulo[0]-triangulo[2])):
        confirmacaoDoTriangulo+=1
    if (triangulo[2] < triangulo[1]+triangulo[0] and triangulo[2] > abs(triangulo[1]-triangulo[0])):
        confirmacaoDoTriangulo+=1
    if (confirmacaoDoTriangulo == 3):
        isTriangulo = True

    destaque = triangulo[0]

    #Lados Iguais
    for i in range(0,3):
        if destaque == triangulo[i]:
            ladosIguais+=1

    #Condição Especial - ISÓCELES
    if triangulo[1] == triangulo[2] and triangulo[1] != triangulo[0]:
        ladosIguais = 2

    if ladosIguais == 1:
        tipoDoTriangulo = "Escaleno"
    elif ladosIguais == 2:
        tipoDoTriangulo = "Isóceles"
    elif ladosIguais == 3:
        tipoDoTriangulo = "Equilátero"

    # Saída de dados
    if (isTriangulo == False):
        print("Não forma um triângulo")
    else:
        print("Sim, forma um triângulo e é um triângulo {}".format(tipoDoTriangulo))
except TypeError:
    print("\033[mERRO DE TIPAGEM, DIGITE APENAS NÚMEROS, NÃO LETRAS! E NÃO DEIXE O ESPAÇO EM BRANCO")

