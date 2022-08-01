from math import hypot

ca_oposto = float(input("\nDigite o cateto oposto: "))
ca_adjacente = float(input("\nDigite o cateto adjacente: "))

print(f"\nHipotenusa: {hypot(ca_oposto, ca_adjacente):.2f}")
