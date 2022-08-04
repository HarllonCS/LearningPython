r1 = float(input("\nReta 1: "))
r2 = float(input("\nReta 2: "))
r3 = float(input("\nReta 3: "))

if (r2 + r3 > r1) and (r1 + r3 > r2) and (r1 + r2 > r3) :
    if r1 == r2 == r3 :
        txt = "\n\nTriângulo Equilátero."
        
    elif r1 != r2 != r3 :
        txt = "\n\nTriângulo Escaleno."
    
    else :
        txt = "\n\nTriângulo Isósceles"
    
else :
    txt = "\nNão é um triângulo!"
    
print(txt)
