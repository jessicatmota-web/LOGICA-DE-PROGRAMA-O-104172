import os
os.system('cls')

#ENTRADA
primeiro_inteiro = float(input('Primeiro Inteiro:'))
segundo_inteiro = float(input('Segundo Inteiro:'))

#PROCESSAMENTO
soma = primeiro_inteiro + segundo_inteiro
media = soma / 2
produto = primeiro_inteiro * segundo_inteiro

if primeiro_inteiro > segundo_inteiro:
    maior = primeiro_inteiro
    menor = segundo_inteiro
    
else:
    maior = segundo_inteiro
    menor = primeiro_inteiro

#SAÍDA
print(f'\nMédia: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')

if primeiro_inteiro == segundo_inteiro:
    print('os numeros são iguais')
else:
    print('os numeros não são iguais')