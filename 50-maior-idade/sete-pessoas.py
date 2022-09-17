cont_maior = 0
cont_menor = 0

for x in range(1, 8) :
    ano_nasc = int(input("\nDigite o ano de nascimento: "))
    
    print(f"\nTem {2021 - ano_nasc} anos.")
    
    if (2021 - ano_nasc) >= 18 :5
        cont_maior += 1
        
    else :
        cont_menor += 1

print(f"\nessoas que atingiram a maioride: {cont_maior}\nPessoas que não atingiram: {cont_menor}")
