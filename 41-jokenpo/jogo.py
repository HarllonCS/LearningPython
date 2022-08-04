from random import randint as rd

print("\nPredra - Papel - Tesoura")

pc = rd(1, 3)

print("\nEscolha:\n\n1 - Pedra\n2 - Papel\n3 - Tesoura")

usuario = int(input("\nUsuário: "))

if pc == 1 :
    esc_pc = "Pedra"

elif pc == 2 :
    esc_pc = "Papel"
    
else :
    esc_pc = "Tesoura"
    
    
if usuario == 1 :
    esc_usu = "Pedra"
    
elif usuario == 2 :
    esc_usu = "Papel"
    
elif usuario == 3 :
    esc_usu = "Tesoura"
    
else :
    print("\nEssa opção não existe!")
