import os
# Pedir ao usuário que digite o seu peso:
os.system('cls')
print(10*'=', 'ENGORDAR E EMAGRECER', 10*'=')
peso = float(input('Digite o seu peso em KG:'))

# Definir o calculo de peso caso engorde 15% de sua masssa total ou emagreça 20%:
engordar = peso * 1.15
emagrecer = peso * 0.20
emagrecer = peso - emagrecer

os.system('cls')

# Mostrar resultados:
print(10*'=', 'RESULTADO', 10*'=')
print(f'O seu peso caso engorde 15% de sua masssa total será de: {engordar:.2f}KG.')
print(f'O seu peso caso emagreça 20% de sua masssa total será de: {emagrecer:.2f}KG.')