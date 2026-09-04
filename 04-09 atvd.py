import os
os.system('cls')

#ENTRADA
login = ('Judas')
senha = ('caguetemorrecedo')

#PROSSESSAMENTO
login1 = input('Digite seu login: ')
senha2 = input('Digite sua senha: ')

#SAÍDA
if login == login1 and senha == senha2:
    print('Bem-Vindo')
else:
    print('Senha ínvalida')
