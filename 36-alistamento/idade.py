from ast import alias
from datetime import date as d

ano_nasc = int(input("\nDigite seu ano de Nascimento: "))
idade_alist = 18
idade = d.today().year - ano_nasc

print(f"\nVocê tem {idade} anos.")

if idade < idade_alist :
    txt = f"\nAinda faltam {idade_alist - idade} anos pra você se alistar."
    
elif idade == idade_alist :
    txt = f"\nHora de se alistar!"

else :
    txt = f"\nJá faz {idade - idade_alist} anos que seu alistamento passou do prazo."
    
print(txt)
    