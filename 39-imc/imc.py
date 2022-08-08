peso = float(input("\nDigite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

print(f"\nSeu índice de Massa Corporal(IMC) é de {imc:.1f}kg/m2")

if imc < 18.5 :
    txt = "\nVocê tem Magreza."

elif imc >= 18.5 and imc < 25 :
    txt = "\nSeu peso está Normal."
    
elif imc >= 25 and imc < 30 :
    txt = "\nVocê está no Sobrepeso."
    
elif imc >= 30 and imc <= 40 :
    txt = "\nVocê está com Obesidade."

else :
    txt = "\nVocê está com Obesidade Morbida."
    
print(txt)
