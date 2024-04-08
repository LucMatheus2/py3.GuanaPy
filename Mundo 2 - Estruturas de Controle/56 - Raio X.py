'''
# Algoritmo : Raio X, na verdade relatório
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20
'''
#Importações
import os

#Constantes
LIMITE = 4

#Variáveis
nomeDoHomemMaisVelho = ""
idadeDoHomemMaisVelho = 0
numeroDeMulheresComMenosDeVinteAnos = 0
mediaDeIdadeDoGrupo = 0
somatorioDoGrupo = 0

for i in range(0,LIMITE):
    #Entrada de dados
    os.system("clear")
    print("FORMULÁRIO {}/{}".format(i+1,LIMITE))
    print("="*30)
    nomeDoUsuario = input("Digite o seu nome : ")
    sexoBiologicoDoUsuario = input("Agora digite o seu sexo biológico (M/F) : ")
    idadeDoUsuario = int(input("Agora, digite quantos anos você tem : "))
    
    #Lógica
    
    # Somatório para depois tirar a média de idade do grupo
    somatorioDoGrupo+=idadeDoUsuario
    
    # Qual o homem mais velho
    if idadeDoUsuario >= idadeDoHomemMaisVelho and sexoBiologicoDoUsuario == 'M':
        nomeDoHomemMaisVelho = nomeDoUsuario
        idadeDoHomemMaisVelho = idadeDoUsuario
    
    # Contabilizando o número de mulheres com menos de 20 anos
    if sexoBiologicoDoUsuario == "F" and idadeDoUsuario < 20:
        numeroDeMulheresComMenosDeVinteAnos+=1
        
#Saída de dados
mediaDeIdadeDoGrupo = somatorioDoGrupo/LIMITE
print("="*30)
print("""
MÉDIA DE IDADE DO GRUPO : {:.1f} ANOS
NOME DO HOMEM MAIS VELHO : {}
MULHERES COM MENOS DE 20 ANOS : {} PESSOAS""".format(mediaDeIdadeDoGrupo,nomeDoHomemMaisVelho,numeroDeMulheresComMenosDeVinteAnos))
