import os
os.system('cls')
print(10*'=', 'MULTIPLO', 10*'=')

# Pedir ao usuário que digite um número:
num = int(input('Digite um número:'))

# Definir se esse numero é multiplo de 3 ou não e mostrar resultados:
if num % 3 == 0:
    os.system('cls')
    print(10*'=', 'RESULTADO', 10*'=')
    print(f'O número {num} é múltiplo de 3. ')
   
else:
    os.system('cls')
    print(10*'=', 'RESULTADO', 10*'=')
    print(f'O número {num} não é múltiplo de 3. ')
    