# Iniciar variáveis
salario = float(input('Insira o salário: R$'))
# Cálculo do aumento
salAumento = salario + (salario * 15 / 100)

# Mostrar salário
print('\n{:=^50}'.format(' Salário ').upper())
print('\nSalário sem aumento: R${:.2f}\nSalário com aumento (15%): R${:.2f}'.format(salario, salAumento))
