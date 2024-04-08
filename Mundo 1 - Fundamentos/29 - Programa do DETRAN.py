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
    print("VOCÊ ULTRAPASSOU O LIMITE DA VELOCIDADE NA RODOVIA")
    print("Rodovia : BR-316 (Trecho Belém-Ananindeua)")
    print("Velocidade permitida: {} km/h".format(limiteDeVelocidade))
    print("Velocidade registrada {} km/h".format(velocidadeDoCondutor))
    print("Valor da Multa : R$ {:.2f}".format(7 * (velocidadeDoCondutor - limiteDeVelocidade)))
    print("Pontos na carteira : +5 (INFRAÇÃO GRAVISSIMA)")
    print("\n DIRIGE COM PRUDÊNCIA, FAÇA DO TRÃNSITO SEGURO")
else:
    print("Você está dentro da velocidade permitida de {} km/h".format(limiteDeVelocidade))
print("=== PREFEITURA DE BELÉM | SECRETÁRIA DE MOBILIDADE URBANA ===")
print("=== DEPARTAMENTO DE TRÂNSITO DO ESTADO DO PARÁ ===")