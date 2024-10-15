# Importação da biblioteca OS para facilitar a visualização dos prints
import os

# Aqui é pedida a placa do automóvel, somente os 4 números
os.system('cls')
placa = str(input('Digite a placa do automóvel (somente os 4 números): '))
numeros = []

# São armazenados os números da placa na lista para a verificação
for i in placa:
    numeros.append(i)

# Aqui são realizadas a verificações do número final da placa, retornando o mês de vencimento do IPVA
if numeros[3] == '0':
    print('O mês de vencimento do seu IPVA é em Janeiro')

elif numeros[3] == '1':
    print('O mês de vencimento do seu IPVA é em Fevereiro')

elif numeros[3] == '2':
    print('O mês de vencimento do seu IPVA é em Março')

elif numeros[3] == '3':
    print('O mês de vencimento do seu IPVA é em Abril')

elif numeros[3] == '4':
    print('O mês de vencimento do seu IPVA é em Maio')

elif numeros[3] == '5':
    print('O mês de vencimento do seu IPVA é em Junho')

elif numeros[3] == '6':
    print('O mês de vencimento do seu IPVA é em Julho')

elif numeros[3] == '7':
    print('O mês de vencimento do seu IPVA é em Agosto')

elif numeros[3] == '8':
    print('O mês de vencimento do seu IPVA é em Setembro')

elif numeros[3] == '9':
    print('O mês de vencimento do seu IPVA é em Outubro')

else:
    print('Placa inválida')
