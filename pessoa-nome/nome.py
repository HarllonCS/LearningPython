nome = input("\nDigite um nome: ")
nome_split = nome.split()

print(f"\nMaiúsculo: {nome.upper()}")

print(f"Minúsculo: {nome.lower()}")

print(f"Quantidade de caracteres: {len(nome)}")

print(f"Quantidade de caracteres do primeiro nome: {len(nome_split[0])}")
