

# Declaraçõa  do número positivo
num1 = int(input('Digite um número positivo: '))


# Calculos para encontrar os valores desejado
quadrado = (num1 ** 2)
cubo = (num1 ** 3)
raiz = (num1 ** 0.5)
cúbica = (num1 ** 0.33)
if num1 > 0:
    print(f'O número ao quadrado é: {quadrado}')
    print(f'O número ao cubo é: {cubo}')
    print(f'A raiz do número  é: {raiz}')
    print(f'A raiz cúbica do número é: {cúbica:2f}')
else:
    print('Digite um número maior que zero!')
