# Iniciar variáveis
cel = float(input('Digite o valor em Celsius (°C): '))
fah = (cel * (9/5)) + 32

# Mostrar temperaturas
print('\n{:=^50}'.format(' temperaturas ').upper())
print('\nTemperatura em °C: {:.1f}°C\nTemperatura em °F: {:.1f}°F'.format(cel, fah))
