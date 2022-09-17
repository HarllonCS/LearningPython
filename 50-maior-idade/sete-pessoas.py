from datetime import date

cont_maior = 0
cont_menor = 0
ano_atual = date.today().year

for x in range(1, 8) :
    ano_nasc = int(input("\nDigite o ano de nascimento: "))
    
    print(f"\nTem {ano_atual - ano_nasc} anos.")
    
    if ano_atual >= 21 :
        cont_maior += 1
    else :
        cont_menor += 1

print(f"\nessoas que atingiram a maioride: {cont_maior}\nPessoas que não atingiram: {cont_menor}")
