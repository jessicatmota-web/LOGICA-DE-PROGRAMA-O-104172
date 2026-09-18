import os
os.system('cls')

#ENTRADA
primeiro_numero = int(input("Digite o primeiro número:"))
segundo_numero = int(input("Digite o segundo número:"))

#PROCESSAMENTO
maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)

print(f' os dois numeros sao {primeiro_numero} e {segundo_numero}')
print(f'o maior numero é {maior}')
print(f'o menor numero é {menor}')


