print(f"\n|{'-'*8}> Início <{'-'*8}|")

viagem = float(input("\nDigite a viagem em km: "))

if viagem <= 200 :
    preco = viagem * .50
    print(f"\nO preço da viagem custará: R${preco:.2f}")
else :
    preco = viagem * .45
    print(f"\nViagens mais longas como essa custarão menos!")
    print(f"\nO preço da viagem custará: R${preco:.2f}")
    
print(f"\n|{'-'*8}> Fim <{'-'*8}|")