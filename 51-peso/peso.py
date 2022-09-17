maior_peso = 0
menor_peso = 0

for x in range(1, 6) :
    peso = float(input("\nDigite o peso: "))
    
    if x == 1 :
        maior_peso = peso
        menor_peso = peso
    else :
        if peso > maior_peso :
            maior_peso = peso
            
        if peso < menor_peso :
            menor_peso = peso
            
print(f"\nMaior peso: {maior_peso}Kg.\nMenor peso: {menor_peso}Kg.")
        
