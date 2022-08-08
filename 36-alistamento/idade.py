from datetime import date as d

ano_nasc = int(input("\nDigite seu ano de Nascimento: "))
idade_alist = 18
ano_atual = d.today().year
idade = ano_atual - ano_nasc

print(f"\nVocê tem {idade} anos.")

if idade < idade_alist :
    saldo = idade_alist - idade
    ano = ano_atual + saldo
    txt = f"\nAinda faltam {saldo} anos pra você se alistar.\nVocê vai se alistar em {ano}."
    
elif idade == idade_alist :
    txt = "\nHora de se alistar!"

else :
    saldo = idade - idade_alist
    ano = ano_atual - saldo
    txt = f"\nJá faz {saldo} anos que seu alistamento passou do prazo.\nVocê já se alistou em {ano}."
    
print(txt)
    