# Inciar variáveis
largura = float(input('Insira a largura da parede em metros: '))
altura = float(input('Insira a altura da parede em metros: '))
# Calcular a área da parede
area = largura * altura
# Litros necessários de tinta
litroTinta = area / 2

# Mostrar resultado
print('\nSua parede tem tem uma dimensão de {:.2f} X {:.2f}\nPortanto, é necessário {:.2f}L de tinta para pintá-la.'.format(largura, altura, litroTinta))
