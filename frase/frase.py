frase = input("\nDigite uma frase qualquer: ").upper().strip()

print(f"\nQuantidade de vezes que aparece a letra 'A': {frase.count('A')}")

print(f"Posição em que a letra 'A' aparece pela primeria vez: [{frase.find('A')+1}]")

print(f"Posição em que a letra 'A' aparece pela última vez: [{frase.rfind('A')+1}]")