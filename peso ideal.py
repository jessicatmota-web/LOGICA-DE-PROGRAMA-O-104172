import os
os.system('cls')

sexo = input('Digite o sexo (M\F): ').upper()
altura = float(input('Digite a altura:' ))

match sexo:
    case 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f'Seu peso ideal é: {peso_ideal: .2f}')

    case 'F':
        peso_ideal = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é: {peso_ideal: .2f}')
