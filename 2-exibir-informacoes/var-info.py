# Iniciar variável
var = input('Digite algo: ')

# Exibir valor da variável
print('\nDigitado: ', var)

# Exibir tipo da variável
print('Tipo da variável: ', type(var))

# Exbir informações da variável no console
print('\nAlfabeto: ', var.isalpha())
print('Numérico: ', var.isnumeric())
print('Alfanumérico: ', var.isalnum())
print('Decimal: ', var.isdecimal())
print('Maiúsculo: ', var.isupper())
print('Minúsculo: ', var.islower())
print('Captalizada: ', var.istitle())
print('Espaço: ', var.isspace())
print('Printável: ', var.isprintable())
print('Ascii: ', var.isascii())
print('Dígito: ', var.isdigit())
