import os

#pedir ao usuário 2 numeros para que o primeiro seja elevado ao segundo (num1**num2):
os.system('cls')
print(10*'=', 'POTENCIAÇÃO', 10*'=')
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
os.system('cls')

#criar a condição que os numeros não podem ser menores que 0:
if num1 < 0 or num2 < 0:
    print(10*'=', 'RESULTADO', 10*'=')
    print('O numero não pode ser menor que 0.')
#mostrar o resultado:
else:
    print(10*'=', 'RESULTADO', 10*'=')
    potencia = num1 ** num2
    print(f'O primeiro numero elevado ao segundo é: {potencia}.')