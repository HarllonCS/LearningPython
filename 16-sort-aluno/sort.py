from random import choice

al1 = input("\nAluno(a) 1: ")
al2 = input("Aluno(a) 2: ")
al3 = input("Aluno(a) 3: ")
al4 = input("Aluno(a) 4: ")

lista = [al1, al2, al3, al4]

print(f"Escolhido(a): {choice(lista)}")
