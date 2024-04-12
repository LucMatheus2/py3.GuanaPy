# Um algoritmo que exiba uma lista de produtos, usando apenas uma tupla
# @author Lucas Matheus C. Costa <lucasmccosta@outlook.com.br>
# @version 1.0.0
# @since 2024

# 1º passo - Capturando os dados
stringDeColecao = ""
indexadorDeControle = True

while indexadorDeControle==True:

    # Declaração de variáveis
    resposta = ""
    gatilhoDeControle = ""
    
    resposta = input("Qual o nome do produto : ")    

    # Concatenando
    stringDeColecao += resposta+","
     
    resposta = input("Qual o preço : R$ ")
    stringDeColecao += resposta

    # Gatilho da repetição
    gatilhoDeControle = input("Você quer continuar montando o cardapio (S/N) : ")
    if (gatilhoDeControle == ""):
        gatilhoDeControle = "n"
    gatilhoDeControle = gatilhoDeControle[0].lower()

    if gatilhoDeControle != "s":
        indexadorDeControle = False
    else:
        stringDeColecao += ","
    print("="*40)


cardapio = () # Array<Tupla>