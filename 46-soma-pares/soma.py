soma = 0

for x in range(1, 7) :
    num = int(input(f"\nDigite o {x}º número: "))
    
    if num % 2 == 0 :
        
        soma += num
        
print(f"\nSoma dos Nº pares: {soma}")
