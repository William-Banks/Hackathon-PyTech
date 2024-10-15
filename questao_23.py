# Importação da biblioteca OS para facilitar a visualização dos prints
import os
os.system('cls')

# Recebimento dos valores de peso e altura e armazenamento em suas respectivas variáveis
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

# Criação da variável de Índice de Massa Corpórea contendo sua fórmula
imc = peso / (altura ** 2)

# Criação de uma função responsável por retornar o Grau de Obesidade baseado no IMC recebido
def gdo(imc):
    if imc < 18.5:
        return('Magreza')

    elif 18.5 <= imc <= 24.9:
        return('Saudável')

    elif 25 <= imc <= 29.9:
        return('Sobrepeso')

    elif 30 <= imc <= 34.9:
        return('Obesidade Grau I')

    elif 35 <= imc <= 39.9:
        return('Obesidade Grau II')

    elif imc >= 40:
        return('Obesidade Grau III')

# Impressão final do IMC e do Grau de Obesidade de acordo com os dados recebidos
os.system('cls')
print(f'O seu índice de massa corpórea é: {imc:.2f}, que corresponde ao grau de obesidade {gdo(imc)}')