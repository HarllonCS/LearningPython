# Inciar variáveis
preco = float(input('Insira o preço do produto: R$'))
desconto = preco - ((preco * 5) / 100)

# Mostrar preço sem e com desconto
print('\n{:=^50}'.format(' preço do produto ').upper())
print('\nSem desconto: R${:.2f}\nCom desconto(5%): R${:.2f}'.format(preco, desconto))
