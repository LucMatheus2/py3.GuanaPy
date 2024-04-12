# Algoritmo : Progressão Aritmética
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20

# Entrada de dados
print("=== PROGRESSÃO ARITMÉTICA ===")
a1 = int(input("Digite o primeiro termo (a1) : "))
r = int(input("Agora digite a razão (r) : "))
limite = 10

# Saída de dados
print("="*30)
print(a1)
for i in range(a1,limite+1):
    an = a1 + (i-1)*r
    print(an, end = ',')
