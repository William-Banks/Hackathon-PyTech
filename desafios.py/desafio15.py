import os
# Pedir ao usuário que digite o valor inicial, taxa de juros e tempo de atraso da prestação:
os.system('cls')
print(10*'=', 'PRESTAÇÃO', 10*'=')
inicial = float(input('Digite o valor inicial da prestação R$:'))
taxa = float(input('Digite a taxa de juros:'))
tempo = float(input('Digite o tempo de atraso em dias:'))

# Definir o cálculo da prestação em atraso:
prestacao = inicial + (inicial * (taxa/100) * tempo)

os.system('cls')
# Mostrar resultados:
print(10*'=', 'RESULTADO', 10*'=')
print(f'O valor da prestação em atraso é: {prestacao:.2f}R$.')