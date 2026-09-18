import os
os.system('cls')

#ENTRADA
nome = (input("Digite o nome do aluno:"))
primeira_nota = float(input("Digite a Primeira nota:"))
segunda_nota = float(input("Digite a Segunda nota:"))
media = (primeira_nota + segunda_nota) / 2

print(f"\n Nome do aluno: {nome}")


#PROCESSAMENTO

if media >= 9:
    print("Seu conceito é A, aprovado")
elif media >= 7.5 and 9:
    print("Seu conceito é B, aprovado")
elif media >= 6 and 7.5:
    print("Seu conceito é C, aprovado")
elif media >= 4 and 6:
    print("Seu conceito é D, reprovado")
else:
    print("Seu conceito é E, reprovado")

