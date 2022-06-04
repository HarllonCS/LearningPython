# Iniciar variáveis
dias = int(input('Insira os dias alugados: '))
km = float(input('Insira os quilômetros rodados: '))
totalPagar = (dias * 60.00) + (km * 0.15)

# Mostrar resultado
print('\n{:=^50}'.format(' Preço ').upper())
print('\nDias alugados: {}\nQuilômetros rodados: {:.2f}km.\nTotal à pagar: R${:.2f}'.format(dias, km, totalPagar))
