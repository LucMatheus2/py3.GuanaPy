'''
# Algoritmo : Fibbonachi
# Versão 1.2
# Autor: Lucas Matheus Costa
# Belém: 05 de Janeiro de 2020
'''
print("\033[32m=*=SEQUÊNCIA DE FIBONACHII =*=")
limiteDaSequencia = int(input("Digite quantos termos você quer : "))
t1 = 0
t2 = 1
t3 = 0
print(t1," =>",t2," =>",end='')
for i in range(1,limiteDaSequencia+1):
    t3 = t2 + t1
    print(t3,end=" => ")
    t1 = t2
    t2 = t3
print("...")
print("Fim do Programa")
