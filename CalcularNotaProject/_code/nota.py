# Iniciar variáveis.
nome = input('Insira o nome do aluno: ')
n1 = float(input('\nDigite a 1ª nota de {}: '.format(nome)))
n2 = float(input('Digie a 2ª nota do aluno: '))

# Calcular média.
media = (n1+n2)/2

print('\nMédia de {}: {:.1f}'.format(nome, media))

# Condição para verficar se o(a) aluno(a) foi aprovado(a) ou não.
if media >= 7.0 :
    txt = '{} foi aprovado(a).'.format(nome)
else :
    txt = '{} foi reprovado(a).'.format(nome)

# Exibir mensagem na tela.
print('\n', txt)