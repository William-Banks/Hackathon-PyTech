
# Declaração das notas
num1 = int(input('Digite a 1° nota: '))
num2 = int(input('Digite a 2° nota: '))
num3 = int(input('Digite a 3° nota: '))

# Calculo feito para encotrar a média das notas
média = (num1 + num2 + num3) / 3

# impressão da média das notas
if num1 > 0 and num2 > 0 and num3 > 0:
    print(f'A média do aluno foi de: {média:.2f}')
else:
    print('Nota inválida, tente novamente')
