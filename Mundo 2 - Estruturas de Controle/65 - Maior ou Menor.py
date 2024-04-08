'''
# Algoritmo : Somarização dos números, digite 999 para parar
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 05 de Janeiro de 2020
'''
opcao = "S"
limiteDoLaco = 10

menorNumero = 0
maiorNumero = 0
media = 0
soma = 0
numero = 0
contador = 0
valorExtra = 0

while opcao == "S":
    while contador < limiteDoLaco:
        contador += 1
        print(f"[{contador}/{limiteDoLaco}] ",end='')
        numero = float(input("Digite um número real : "))
        soma += numero
        if contador == 1 or numero > maiorNumero:
            maiorNumero = numero
        if contador == 1 or numero < menorNumero:
            menorNumero = numero
    opcao = input("Voce quer continuar (s/n) : ")
    opcao = opcao.upper()
    if opcao == "S":
        valorExtra = int(input("Quantos números mais você quer : "))
        limiteDoLaco += valorExtra
media = soma/limiteDoLaco
print(f"""
====================================
A Média entre eles é {media:.1f}   |
O Maior número é {maiorNumero:.1f} |
O Menor número é {menorNumero:.1f} |
====================================
""")
