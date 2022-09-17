frase = input("\nDigite uma frase: ").strip().upper()

frase = frase.split()
frase = ''.join(frase)
inverso = ''

for letra in range(len(frase) - 1, -1, -1) :
    inverso += frase[letra]
    
print(inverso)

if inverso == frase :
    print("\nTemos um palíndromo!")
else :
    print("\nNão é um palíndromo!")