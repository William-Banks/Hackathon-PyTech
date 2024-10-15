

# Declaraçõa do salário
salário = float(input('Digite o salário: '))

# Calculo  feito para descobrir o novo salário
aumento = float(input('Digite o percentual do aumento: '))
final = (aumento / 100) +1
salario_final = salário * final

# impressão do valor final
print(f'O valor final do salário com o aumento foi de: {salario_final}')
