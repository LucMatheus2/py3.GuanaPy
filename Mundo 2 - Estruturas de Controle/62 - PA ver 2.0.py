'''
# Algoritmo : PA
# Versão 1.2
# Autor: Lucas Matheus Costa
# Belém: 05 de Janeiro de 2020
'''
#Constantes
LIMITE_DA_PA = 10

#Variáveis
i = 1
an = 0
contadorDeTermos = 0
predecessorAnterior = 0
sucessorDeTermos = 1

#Dados de Entrada
a1 = int(input("Qual o primeiro termo (a1) da PA : "))
r = int(input("Qual a razão(r) : "))

while i <= LIMITE_DA_PA:
    an = a1 + (i - 1)*r
    print("{}".format(an),end=" => ")
    i += 1
print("...")
#---------------------------------------------------
#Predecessor da PA
predecessorAnterior = LIMITE_DA_PA
contadorDeTermos = LIMITE_DA_PA

while sucessorDeTermos > 0:
    sucessorDeTermos = int(input("Quantos termos mais você quer mostrar : "))
    for i in range(predecessorAnterior+1,(predecessorAnterior+sucessorDeTermos)+1):
        an = a1 + (i - 1)*r
        print("{}".format(an),end=" => ")
        i += 1
    print("...")
    contadorDeTermos += sucessorDeTermos
    predecessorAnterior += sucessorDeTermos
print("Progressão encerrada com {} termos apresentados".format(contadorDeTermos))
print("\nFim Do Programa")