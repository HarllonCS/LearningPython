salario = float(input("\nInforme o salário do(a) funcionário(a): "))

if salario > 1250 :
    sal_aumento = salario + (salario * 10 / 100)
    print(f"\nReceberá um aumento de 10%")
    print(f"\nReceberá um aumento de: R${sal_aumento:.2f}")
else :
    sal_aumento = salario + (salario * 15 / 100)
    print(f"\nReceberá um aumento de 15%")
    print(f"\nReceberá um aumento de: R${sal_aumento:.2f}")
