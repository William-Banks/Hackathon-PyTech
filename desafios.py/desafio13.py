import os
os.system('cls')
print(10*'=', 'RECEBIMENTO', 10*'=')
# Definir as regras do calculo do salário recebido:
horas = float(input('Digite quantas horas você trabalhou:'))
salario = float(input('Digite o valor do salário mínimo R$:'))
hora_trabalhada = salario / 2
salario_bruto = hora_trabalhada * horas
imposto = 0.03 * salario_bruto
receber = salario_bruto - imposto

os.system('cls')
# Mostrar resultados:
print(10*'=', 'RESULTADO', 10*'=')
print(f'O salário recebido foi de: {receber}R$.')