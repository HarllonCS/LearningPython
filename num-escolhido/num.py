from random import randint as rd

num_escolhido = rd(0, 5)

print(f"\n{'-'*8}| Inicio |{'-'*8}")

num_adivinhado = int(input("\nAdivinhe o numero: "))

if num_adivinhado == num_escolhido :
    print("\nParabens, voce venceu!")
else :
    print(f"\nPoxa! Voce errou :(\n\nO numero certo era {num_escolhido}")
    
print(f"\n{'-'*8}| Fim de jogo |{'-'*8}")
