n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("\nDigite o segundo número: "))
n3 = int(input("\nDigite o terceiro número: "))

maior = n1
menor = n1

# Maior
if n2 > n1 and n2 > n3 :
    maior = n2
    
if n3 > n2 and n3 > n2 :
    maior = n3
    
print(f"\nO maior número é {maior}!")

# Menor
if n2 < n1 and n2 < n3 :
    menor = n2
    
if n3 < n1 and n3 < n2 :
    menor = n3

print(f"O menor número é {menor}!")
