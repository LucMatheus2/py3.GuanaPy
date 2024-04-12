# Algoritmo : Tabuada
# Versão 3.0
# Autor: Lucas Matheus Costa
# OBS: É possivel com teste lógico simples, este visa apenas usando o break 
# que é possível com alguns ifs
# Belém: 05 de Janeiro de 2020

numeroDaTabuada = 0

while True:
    print("="*30)
    print(""" TABUADA Ver 3.0/20
    Digite um NÚMERO INTEIRO e aperte ENTER para ver a sua Tabuada
    (i) - Para fechar o programa digite um valor negativo e Aperte ENTER
    """)
    numeroDaTabuada = int(input("Qual número? : "))
    if (numeroDaTabuada < 0):
        break
    for i in range(1,11):
        print(f"{numeroDaTabuada} x {i} = {numeroDaTabuada*i}")
print("="*30)
print("ENCERRANDO O PROGRAMA...Obg por utilizar")