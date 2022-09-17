pri_termo = int(input("\nDigite o Primeiro Termo da P.A: "))
razao = int(input("Digite a Razão: "))
dec_termo = pri_termo + (10 - 1) * razao

for x in range(pri_termo, dec_termo, razao) :
    print(x)
    