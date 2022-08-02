from datetime import date as d

ano = int(input("\nDigite o ano: "))

if ano == 0 :
    ano = d.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f"\n{ano} é Bissexto!")
else :
    print(f"\n{ano} não é Bissexto!")
