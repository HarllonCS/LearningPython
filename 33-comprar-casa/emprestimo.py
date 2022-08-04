casa_valor = float(input("\nInforme o valor da casa: "))
salario = float(input("Informe seu salário: "))
anos = int(input("Digite em quantos anos você vai pagar: "))

valor = (casa_valor / anos) / 12
minimo = salario * 30 / 100

print(f"\nValor da Prestação Mensal: R${valor:.2f}")

print("\nEmpréstimo pode ser consedido." if valor <= minimo else "\nEmpréstimo negado.")