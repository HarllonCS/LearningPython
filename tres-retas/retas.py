r1 = float(input("\nReta 1: "))
r2 = float(input("\nReta 2: "))
r3 = float(input("\nReta 3: "))

if r2 + r3 > r1 and r1 + r3 > r2 and r1 + r2 > r3 :
    print(f"\nÉ um triângulo")
else :
    print(f"\nNão é um triângulo")