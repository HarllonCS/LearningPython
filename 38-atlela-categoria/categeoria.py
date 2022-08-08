from datetime import date as d

ano_nasc = int(input("\nInforme o ano de nascimento do(a) atleta: "))
idade = d.today().year - ano_nasc

print(f"\nTem {idade} anos.")

if idade == 9 :
    txt = "\nAtleta Mirim."

elif 14 >= idade >= 10 :
    txt = "\nAtleta Infantil."
    
elif idade >= 15 and idade <= 19 :
    txt = "\nAlteta junior."
    
elif idade == 20 :
    txt = "\nAtleta Sênior."

elif idade > 20 :
    txt = "\nAtleta Master."

else :
    txt = "\nNão poder ser Atleta!"

print(txt)
