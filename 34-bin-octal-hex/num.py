num = int(input("\nDigite um número: "))

print("\nDigite a base de conversão: ")
print("\n1 - Binário\n2 - Octal\n3 - Hexadecimal")

op = int(input("\nDigite aqui: "))

if op == 1 :
    txt = f"\nBinário: {bin(num)}"
    
elif op == 2 :
    txt = f"\nOctal: {oct(num)}"
    
elif op == 3 :
    txt = f"\nHexadecimal: {hex(num)}"
    
else :
    txt = "\nNão existe essa opção!"

print(txt)
