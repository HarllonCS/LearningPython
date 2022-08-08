from random import randint as rd

print("\nPredra - Papel - Tesoura")

pc = rd(1, 3)

if pc == 1 :
    esc_pc = "Pedra"

elif pc == 2 :
    esc_pc = "Papel"

else :
    esc_pc = "Tesoura"


print("\nEscolha:\n\n1 - Pedra\n2 - Papel\n3 - Tesoura")

usuario = int(input("\nEscolha: "))

if usuario == 1 :
    esc_usu = "Pedra"

elif usuario == 2 :
    esc_usu = "Papel"

elif usuario == 3 :
    esc_usu = "Tesoura"

else :
    print("\nEssa opção não existe!")
    
    
#print("\nResultado".upper())

usu_perdeu = (pc == 1 and usuario == 3) or (pc == 2 and usuario == 1) or (pc == 3 and usuario == 2)

usu_venceu = (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2)

print(f"\nPC: {esc_pc}\nUsuário: {esc_usu}")

if usu_venceu :
    print("\nVocê é foda!".upper())

elif usu_perdeu :
    print("\nPerdeu otário!! Mais sorte na próxima vez...")

else :
    print("\nEmpate!!".upper())
    