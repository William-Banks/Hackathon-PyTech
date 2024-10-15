import os
# Pedir ao usuário que digite um número inteiro:
os.system('cls')
print(10*'=', 'PAR E IMPAR', 10*'=')
num = int(input('Digite um numero inteiro:'))

# Definir se o numero é par ou impar vendo se o resto da divisão por 2 é igual 0, e mostrar resultados:
os.system('cls')
if num % 2 == 0:
    print(10*'=', 'RESULTADO', 10*'=')
    print('O número digitado é par.')
else:
    print(10*'=', 'RESULTADO', 10*'=')
    print('O número digitado é impar.')