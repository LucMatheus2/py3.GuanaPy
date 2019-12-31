'''
# Algoritmo : Programa do Detran-PA
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: ???/2018-19
'''
#Entrada de dados
print("=== DETRAN-PA ===")
velocidadeDoCondutor = int(input("Qual a velocidade do motorista (em km/h) :"))

#Processamento e Saída
limiteDeVelocidade = 80

if (velocidadeDoCondutor > limiteDeVelocidade):
    print("\033[1;7;31mVOCÊ ULTRAPASSOU O LIMITE DA VELOCIDADE NA RODOVIA\033[m")
    print("Rodovia : BR-316 (Trecho Belém-Ananindeua)")
    print("Velocidade permitida: {} km/h".format(limiteDeVelocidade))
    print("\033[1;5mVelocidade registrada {} km/h".format(velocidadeDoCondutor))
    print("\033[mValor da Multa : R$ {:.2f}".format(7 * (velocidadeDoCondutor - limiteDeVelocidade)))
    print("Pontos na carteira : +5 (INFRAÇÃO GRAVISSIMA)")
    print("\n DIRIGE COM PRUDÊNCIA, FAÇA DO TRÃNSITO SEGURO")
else:
    print("\033[1;7;32mVocê está dentro da velocidade permitida de {} km/h".format(limiteDeVelocidade))
print("\033[1;7;34m=== PREFEITURA DE BELÉM | SECRETÁRIA DE MOBILIDADE URBANA ===")
print("=== DEPARTAMENTO DE TRÂNSITO DO ESTADO DO PARÁ ===\033[m")