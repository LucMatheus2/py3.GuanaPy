# Algoritmo que descobre par ou impar
# @autor Lucas Matheus C. Costa <lucasmccosta@outlook.com.br>
# @version 1.0.1
# @since 2019? - Revisão 2024

# Bibliotecas
from random import randint
numeroDoUsuario = somaDoJogo = numeroDeVitoriasDoUsuario = 0
resultadoDoJuiz = ""
isGanhou = True

#Pegando os dados do usuário
while isGanhou:
    numeroDoUsuario = 0
    print("Jogar Par Ou Impar")
    while numeroDoUsuario < 1 or numeroDoUsuario > 10:
        numeroDoUsuario = int(input("Digite um número inteiro (entre 1 e 10) : "))
    while True:
        opcaoDoUsuario = input("[P]ar ou [I]mpar? : ")
        opcaoDoUsuario = opcaoDoUsuario.lower()
        if (opcaoDoUsuario == "p" or opcaoDoUsuario == "i"):
            break

    #Pegando o resultado da maquina
    numeroDaMaquina = randint(1,10)

    #Conferindo se é par ou impar
    somaDoJogo = numeroDoUsuario + numeroDaMaquina
    if somaDoJogo%2 == 0:
        resultadoDoJuiz = "p"
    elif somaDoJogo%2 == 1:
        resultadoDoJuiz = "i"

    #Imprimindo o resultado
    if resultadoDoJuiz == "p":
        print(f"Deu um total de {somaDoJogo}, o resultado é PAR")
    else:
        print(f"Deu um total de {somaDoJogo}, o resultado é IMPAR")
    #Checando para ver se ganhou
    if opcaoDoUsuario == resultadoDoJuiz:
        print("Você Ganhou!")
        isGanhou = True
        numeroDeVitoriasDoUsuario+=1
        print("..................")
        print("A Maquina quer uma revanche")
        print("."*19)
    else:
        print("Você Perdeu!")
        print("Você ganhou um total de {} partidas".format(numeroDeVitoriasDoUsuario))
        isGanhou = False
print("Encerrando o programa")