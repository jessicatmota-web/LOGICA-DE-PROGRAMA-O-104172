import os
os.system('cls')


maca= int(input("Digite a quantidade de maçãs desejadas:"))

if maca >= 12:
    valor_da_maca = 1.00
else:
    valor_da_maca = 1.30

valor_total = maca * valor_da_maca

print(f"A quantidade de maçãs foram: {maca}")
print(f"Valor total das maçãs foram: R$ {valor_total:.2f}")
