num = int(input("\nDigite um número: "))

mult = 0

for x in range(1, num+1) :
    
    if num % x == 0 :
        print(f"\n{num} é mútiplo de: {x}")
        mult += 1

if mult == 2 :
    print(f"\n{num} é primo!\nPois, ele divisível apenas por {mult} números: 1 e {num}")

else :
    print(f"\n{num} não é número primo, pois ele é mútiplo de {mult} números.")
