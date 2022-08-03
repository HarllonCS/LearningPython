print(f"\n{'-'*8}| Inicio |{'-'*8}")

vel_carro = float(input("\nVelocidade do carro: "))
vel_limite = 80.0
multa = (vel_carro - vel_limite) * 7.00

print(f"\nVoce esta correndo em {vel_carro}km/h")

if vel_carro > vel_limite :
    print(f"\nA velocidade limite eh de {vel_limite}km/h")
    print(f"Voce tera que pagar uma multa de R${multa:.2f}")
else :
    print(f"\nTudo certo!\n\nPode seguir.")
    
print(f"\n{'-'*8}| Fim do Programa |{'-'*8}")