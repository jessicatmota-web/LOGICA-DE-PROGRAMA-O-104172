import os
os.system('cls')

#ENTRADA
idade = int(input("Digite sua idade: "))

#PROCESSAMENTO
if idade < 16:
    print("Não podem votar.")

elif idade < 18:
    print("Opcional votar.")

elif idade <= 65:
    print("Voto Obrigatório.")

else:
    print("Não é obrigatório votar.")

