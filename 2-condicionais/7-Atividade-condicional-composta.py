import os
os.system ('cls')

#ENTRADA
primeira_nota = float(input("Digite a Primeira nota:"))
segunda_nota = float(input("Digite a Segunda nota:"))
terceira_nota = float(input("Digite a Terceira nota:"))
media = (primeira_nota + segunda_nota + terceira_nota) / 3

#PROCESSAMENTO

if media >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")

#SAÍDA
print("Fim do Programa")

