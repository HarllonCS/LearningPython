preco = 400.00

print("\nInisira a forma de pagamento: ")
print("\n1 - Á vista no dinheiro/cheque\n2 - Á vista no cartão\n3 - Até 2x no cartão\n4 - 3x ou mais no cartão\n")

op = int(input("Digite aqui: "))

if op == 1 :
    preco -= ((preco * 10) / 100)
    txt = f"\nVocê recebeu 10% de desconto.\nO preço ficou por R${preco:.2f}!"
    
elif op == 2 :
    preco -= ((preco * 5) / 100)
    txt = f"\nVocê recebeu 5% de desconto.\nO preço ficou por R${preco:.2f}!"
    
elif op == 3 :
    txt = f"\nVocê não recebeu desconto e nem juros.\nPreço: R${preco:.2f}!"
    
elif op == 4 :
    txt = f"\nVocê terá que pagar 20x de juros."
    
else :
    txt = f"\nEssa opção não existe!"
    
print(txt)
