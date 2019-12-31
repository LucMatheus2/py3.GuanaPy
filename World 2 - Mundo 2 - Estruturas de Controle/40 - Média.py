'''
# Algoritmo : Boletim Eletrônico da UEPA
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Importação de pacotes
from math import ceil,floor,trunc

#Entrada de dados
print("\033[32m=== BOLETIM ELETRÔNICO (DA UEPA) ===")
primeiraAvaliacao = float(input("Digite a primeira avaliação : "))
segundaAvaliacao = float(input("Digite a nota da segunda avaliação : "))
mediaDaFaculdade = 8
estado = "Cursando..."

#Processamento - verificando a nota para ver se fica de terceira
Soma = primeiraAvaliacao + segundaAvaliacao
media = Soma/2

if (media < mediaDaFaculdade):
    isTerceira = input("Você já fez a terceira avaliação? (S/N) : ")
    if isTerceira == 'S':
        terceiraAvaliacao = float(input("Digite a nota da terceira avaliação : "))
        Soma += terceiraAvaliacao
        mediaDaFaculdade = 6
    else:
        terceiraAvaliacao = 0
else:
    terceiraAvaliacao = 0

#Processamento - Gerando a média
if (terceiraAvaliacao == 0):
    media = Soma/2
elif (terceiraAvaliacao > 0):
    media = Soma/3

#Processamento - Arredondando a média
diferenca = media - trunc(media)

if ((diferenca >= 0.1) and (diferenca <= 0.3)):
    media = floor(media)
elif ((diferenca == 0.4) or (diferenca == 0.6)):
    media = trunc(media) + 0.5
elif (diferenca >= 0.7):
    media = ceil(media)

#Processamento - Avaliando o Aluno
if (media >= mediaDaFaculdade):
    estado = "\033[1;7;32m APROVADO"
else:
    if isTerceira != "S":
        estado = "\033[1;7;33mFALTA A 3ª AVALIAÇÃO"
    else:
        estado = "\033[1;7;31m REPROVADO"


#Saida de dados
print("""
     === RESULTADO FINAL ===
     | AV 1 | AV 2 | AV 3 | SOMA | MÉDIA | ESTADO |
     ----------------------------------------------
     | {:.1f} | {:.1f} | {:.1f} | {:.1f} | {:.1f} | {}  
""".format(primeiraAvaliacao,segundaAvaliacao,terceiraAvaliacao,Soma,media,estado))