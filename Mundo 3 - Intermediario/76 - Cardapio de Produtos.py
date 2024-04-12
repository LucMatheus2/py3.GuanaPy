# Um algoritmo que exiba uma lista de produtos, usando apenas uma tupla
# @author Lucas Matheus C. Costa <lucasmccosta@outlook.com.br>
# @version 1.0.0
# @since 2024

# 1º passo - Capturando os dados
stringDeColecao = ""
indexadorDeControle = True


print("""
      DICA: Para fechar o programa, digite \"666\" no Nome do produto
      ===========================================================
      """)

while indexadorDeControle==True:

    # Declaração de variáveis
    resposta = ""
    gatilhoDeControle = ""
    
    resposta = input("Qual o nome do produto : ")    

    # Quebrar o programa
    if resposta=="666":
        indexadorDeControle = False
        break

    # Concatenando
    stringDeColecao += resposta+","
     
    resposta = input("Qual o preço : R$ ")
    stringDeColecao += resposta

    print("="*40)

# 2º Passo -  Convertendo em Tupla
cardapio = stringDeColecao.split(",") # Array<List>
cardapio = tuple(cardapio)

# 3º Passo - Imprimir o cardapio
print("==========================")
for indice in range(0,len(cardapio)-1,2):
    print("Item : {} | Preço: R$ {}".format(cardapio[indice],cardapio[indice+1]))