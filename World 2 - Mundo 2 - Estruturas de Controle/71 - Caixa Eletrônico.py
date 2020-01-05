#Obs - ele ainda tá com um problema na seção dos 50 reais
from math import trunc

copiaDoValor = 0
numeroDeNotasDe100 = numeroDeNotasDe50 = numeroDeNotasDe20 = numeroDeNotasDe10 = 0
opcaoDoUsuario = ""
valorIncorreto = False

print("== CAIXA ELETRÔNICO 24 HORAS ==")
valorDeSaque = float(input("Qual o valor que você quer sacar : R$ "))

valorDeSaque = trunc(valorDeSaque)
copiaDoValor = valorDeSaque
while copiaDoValor > 10:
    if (copiaDoValor%10 != 0):
        valorIncorreto = True
        break

    if (copiaDoValor%100 == 0):
        numeroDeNotasDe100 += 1
        copiaDoValor -= 100
    elif (copiaDoValor%50 == 0):
        numeroDeNotasDe50 += 1
        copiaDoValor -= 50
    elif (copiaDoValor%20 == 0):
        numeroDeNotasDe20 += 1
        copiaDoValor -= 20
    elif (copiaDoValor%10 == 0):
        numeroDeNotasDe10 += 1
        copiaDoValor -= 10
if (valorIncorreto):
    print("TRANSAÇÃO NEGADA")
    print("O Valor digitado não é possível, este caixa trabalha apenas com notas de R$ 50, R$ 20 e R$ 10")
else:
    print("TRANSAÇÃO AUTORIZADA")
    print(f"""
    VALOR DE SAQUE = R$ {valorDeSaque}
    -------------------------------
    {numeroDeNotasDe100} x R$ 100 |
    {numeroDeNotasDe50} x R$ 50   |
    {numeroDeNotasDe20} x R$ 20   |
    {numeroDeNotasDe10} x R$ 10   |
    -------------------------------
    """)
print("Obrigado por utilizar")