import os
# Pedir ao usuário que digite 3 numeros:
os.system('cls')
print(10*'=', 'MAIOR E MENOR', 10*'=')
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
num3 = int(input('Digite outro número:'))

os.system('cls')

# Verificar qual é o maior número dos 3 e mostrar resultados:
if num1 > num2 and num1 > num3:
    print(10*'=', 'RESULTADO', 10*'=')
    print(f'O número {num1} é o maior número.')
elif num2 > num1 and num2 > num3:
    print(10*'=', 'RESULTADO', 10*'=')
    print(f'O número {num2} é o maior número.')
elif num3 > num1 and num3 > num2:
    print(10*'=', 'RESULTADO', 10*'=')
    print(f'O número {num3} é o maior número.')


# Verificar qual é o menor numero dos 3 e mostrar resultados:
if num1 < num2 and num1 < num3:
    print(f'O número {num1} é o menor número.')
elif num2 < num1 and num2 < num3:
    print(f'O número {num2} é o menor número.')
elif num3 < num1 and num3 < num2:
    print(f'O número {num3} é o menor número.')







