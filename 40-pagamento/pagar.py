preco = float(input("\nPreço total dos produtos: "))

print("\nInisira a forma de pagamento: ")
print("\n1 - Á vista no dinheiro/cheque\n2 - Á vista no cartão\n3 - Até 2x no cartão\n4 - 3x ou mais no cartão\n")

op = int(input("Digite aqui: "))

if op == 1 :
    preco -= (preco * (10 / 100))
    txt = f"\nVocê recebeu 10% de desconto.\nPreço Total: R${preco:.2f}!"
    
elif op == 2 :
    preco -= (preco * (5 / 100))
    txt = f"\nVocê recebeu 5% de desconto.\nPreço Total: R${preco:.2f}!"
    
elif op == 3 :
    preco /= 2
    txt = f"\nVocê terá que pagar parcelado 2x.\nPreço Total: R${preco:.2f}!"
    
elif op == 4 :
    preco += (preco * (20 / 100))
    parcelas = int(input("\nParcelas à pagar: "))
    preco /= parcelas
    txt = f"\nVocê terá que pagar parcelado em {parcelas}x com 20% de juros.\nPreco Total: R${preco:.2f}!"
    
else :
    txt = f"\nEssa opção não existe!"
    
print(txt)
