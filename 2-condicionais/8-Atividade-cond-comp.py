import os
os.system('cls')

#ENTRADA
primeiro_numero = float(input('Primeiro Número:'))
segundo_numero = float(input('Segundo Número:'))

#PROCESSAMENTO
soma = primeiro_numero + segundo_numero
media = soma / 2 
produto = primeiro_numero * segundo_numero

if primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero

#SAÍDA
print(f'\nMédia: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
