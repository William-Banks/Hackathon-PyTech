# Importação da biblioteca OS para facilitar a visualização dos prints
import os

# Recebimento dos números por meio do input do usuário
os.system('cls')
num1 = int(input('Digite o primeiro número: '))
os.system('cls')
num2 = int(input('Digite o segundo número: '))
os.system('cls')

# Verifica-se se o número A é divisível pelo B por meio do módulo
if num1 % num2 == 0:
    print('='*10, 'RESULTADO', '='*10)
    print(f'{num1} é divisível por {num2}.')
    print('='*30)
else:
    print('='*10, 'RESULTADO', '='*10)
    print(f'{num1} NÃO é divisível por {num2}.')
    print('='*30)