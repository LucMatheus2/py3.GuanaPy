# Algoritmo para colocar palavras numa tupla e contar suas respectivas vogais
# 
# @author Lucas Matheus C. Costa <lucasmccosta@outlook.com.br>
# @version 1.0.0
# @since 2024

# 1º Passo - Separar as informações
tuplaVogais = ("a","e","i","o","u") # Tupla<Char>
palavras = "" # String
gatilhoRepeticao = True

# Colocar palavras
print("Para encerrar o programa é só apertar ENTER sem nenhuma palavra, ou seja vazio")

while gatilhoRepeticao==True:
    novaPalavra = ""
    novaPalavra = input("Digite uma nova palavra : ")
        
    if novaPalavra=="":
        gatilhoRepeticao = False
    else:
        palavras += novaPalavra + ","

palavras = palavras[0:-1]
palavras = palavras.split(",")
palavras = tuple(palavras)

for item in palavras:
    vogaisEncontradas = "[" # String

    for vogal in tuplaVogais:
        VALOR_NAO_ENCONTRADO = -1
        resposta = VALOR_NAO_ENCONTRADO
        resposta = item.find(vogal)

        if resposta!=VALOR_NAO_ENCONTRADO:
            vogaisEncontradas += vogal+" "
    vogaisEncontradas += "]"

    print("A palavra {} tem as vogais {}".format(
        item.upper(),
        vogaisEncontradas
    ))