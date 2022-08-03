# Iniciar variáveis.
n1 = float(input("\nDigite a 1ª nota: "))
n2 = float(input("Digie a 2ª nota: "))

# Calcular média.
media = (n1 + n2) / 2

print(f"\nSua média é  {media:.1f}")

# Condição para verficar se o(a) aluno(a) foi aprovado(a) ou não.
if media >= 7.0 :
    txt = "\nVocê foi aprovado(a)."
    
elif media == 5.0 and media <= 6.9 :
    txt = "\nVocê está em recuperação."
    
else :
    txt = "\nVocê foi reprovado(a)."

# Exibir mensagem na tela.
print(txt)