# Algoritmo : PA
# Versão 1.2
# Autor: Lucas Matheus Costa
# Belém: 05 de Janeiro de 2020

# Constantes
LIMITE_DA_PA = 10

# Variáveis
i = 1
an = 0

# Dados de Entrada
a1 = int(input("Qual o primeiro termo (a1) da PA : "))
r = int(input("Qual a razão(r) : "))

while i <= LIMITE_DA_PA:
    an = a1 + (i - 1)*r
    print("{}".format(an),end=" => ")
    i += 1
print("...")
print("\nFim Do Programa")