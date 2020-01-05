#Variáveis
nomeDoProduto = ""
precoDoProduto = 0

nomeDoProdutoMaisBarato = ""
qtdeDeProdutosDeMaisDeMilReais = 0
totalDeGastoDasCompras = 0
numeroDeProdutos = 0
precoDoMaisBarato = 0
opcaoDoMenu =  ""

while True:
    print("*="*15)
    nomeDoProduto = input("Qual o nome do Produto : ")
    precoDoProduto = float(input("Quanto custa : R$ "))
    numeroDeProdutos+=1
    if numeroDeProdutos == 1 or precoDoProduto < precoDoMaisBarato:
        nomeDoProdutoMaisBarato = nomeDoProduto
        precoDoMaisBarato = precoDoProduto
    if precoDoProduto > 1000:
        qtdeDeProdutosDeMaisDeMilReais+=1
    totalDeGastoDasCompras += precoDoProduto
    opcaoDoMenu = input("Quer continuar (s/n) : ")
    opcaoDoMenu = opcaoDoMenu.lower()
    if opcaoDoMenu == "n":
        break
print("===RESULTADO FINAL ===")
print("Total : R$ {:.2f}".format(totalDeGastoDasCompras))
print("====================================================")
print(f"Quantidade de compras acima de 1000 reais : {qtdeDeProdutosDeMaisDeMilReais} produtos")
print("O produto mais barato é o {}".format(nomeDoProdutoMaisBarato))
print("=================================================")
print("Encerrando o programa...")