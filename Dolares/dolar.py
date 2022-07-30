# Iniciar variáveis
dinheiro = float(input('Insira seu saldo: '))
# Converter de Real para Dólar
dolar = dinheiro/3.27

# Mostrar quantidade inserida
print('\nVocê tem R${:.2f}'.format(dinheiro))
print('Você pode comprar ${:.2f}'.format(dolar))
