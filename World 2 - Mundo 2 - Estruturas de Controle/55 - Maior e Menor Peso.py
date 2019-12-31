'''
# Algoritmo : O Mais pesado e o menos pesado
# Versão 1.0
# Autor: Lucas Matheus Costa
# Belém: 2019-20
'''
#Variáveis
maisPesado = 0
menosPesado = 0
pesoAnterior = 0

#Entrada de dados
for i in range(0,5):
    numeroDoUsuario = float (input("{}/5 - Digite um peso (em kg) : ".format(i+1)))
    
    # Processamento

    # Caso inicial, para fins de comparação um pouco mais coerente
    if (i == 0):
        maisPesado = numeroDoUsuario
        menosPesado = numeroDoUsuario
        pesoAnterior = numeroDoUsuario
    else :
        #Comparação bruta dos pesos
        if (numeroDoUsuario > pesoAnterior and numeroDoUsuario > maisPesado):
            maisPesado = numeroDoUsuario
        elif (numeroDoUsuario < pesoAnterior and numeroDoUsuario < menosPesado):
            menosPesado = numeroDoUsuario
    #Armazenar o peso anterior para a comparação fazer sentido.
    pesoAnterior = numeroDoUsuario
#Saída de dados
print("="*35)
print("O mais \033[1mpesado\033[m tem {} kg e o \033[3mmenos\033[m pesado tem {} kg".format(maisPesado,menosPesado))
