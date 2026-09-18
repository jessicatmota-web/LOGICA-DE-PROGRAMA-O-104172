import os
os.system('cls')

peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

imc = peso /  (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 24.9 and 18.6:
    print("Peso ideal")
elif imc <= 29.9 and 25.0:
    print("Levemente acima do peso")
elif imc <= 34.9 and 30.00:
    print("Obesidade grau I")
elif imc <= 39.9 and 35.0:
    print("Obesidade grau II(severa)")
elif imc >=40:
    print("Obesidade III (mórbida)")

