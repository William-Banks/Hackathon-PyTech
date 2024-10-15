import os
os.system('cls')
print(10*'=', 'RETÂNGULO', 10*'=')

# Pedir ao usuário o valor da base e altura do retângulo:
base = int(input('Digite o valor da base retângulo:'))
altura = int(input('Digite o valor da altura do retângulo:'))

# Definir o calculo da área, perimetro e diagonal:
area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base**2 + altura**2)** 0.5
os.system('cls')

# Mostrar resultados:
print(10*'=', 'RESULTADO', 10*'=')
print(f'A área do retângulo vale: {area}.')
print(f'O perímetro do retângulo vale: {perimetro}.')
print(f'A diagonal do retângulo vale: {diagonal:.2f}.')