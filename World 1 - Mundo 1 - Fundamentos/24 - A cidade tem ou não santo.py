'''
# Algoritmo : A Cidade começa com santo
# Autor: Lucas Matheus Costa
# Belém: ???/2017-19
'''

#Entrada
cidade = input("Digite o nome da sua cidade :").strip()

#Processamento

cidade = cidade.capitalize()
cidade = cidade.split()
isSanto = cidade[0] in "Santo"
temSanto = "Não"

if(isSanto):
    temSanto = "Sim"
else:
    temSanto = "Não"
    
#Saída
print("A sua cidade começa com 'Santo' no nome : {}".format(temSanto))