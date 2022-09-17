soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
totmulher20 = 0

for x in range(1, 5) :
    nome = input(f"\nPessoa {x} > Digite o nome: ")
    idade = int(input(f"Pessoa {x} > Digite a idade: "))
    sexo = input(f"Pessoa {x} > Digite o sexo: ")
    
    soma_idade += idade
    
    if x == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    
    if sexo in 'Mm' and idade > maior_idade_homem :
        maior_idade_homem = idade
        nome_velho = nome
        
    if sexo in 'Ff' and idade > 20 :
        totmulher20 += 1
    
media_idade = soma_idade / 4

print(f"\nA média de idade é {media_idade}.")
print(f"\nO homem mais velho tem {idade} anos e no nome dele é {nome}.")
print(f"\n{totmulher20} mulher tem menos de 20 anos.")
    