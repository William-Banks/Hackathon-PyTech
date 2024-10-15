# Importação da biblioteca OS para facilitar a visualização dos prints

import os

# Recebimento dos dados base para o recibo do empréstimo

os.system('cls')
print('Bem-vindo ao sistema da biblioteca Branca Adjuto Botelho!')
livro = str(input('Digite o nome do livro: '))
usuario = int(input('Você é um:\n 1. Aluno\n 2. Professor\n'))
dia = int(input('Digite o dia do empréstimo (5, 17, 26): '))
mes = int(input('Digite o número do mês do empréstimo (2, 6, 12): '))
data = (f'{dia}/{mes}')
tipo = ''

# Criação da função responsável por calcular a data, dependendo do número do dia e do mês

def calcular_data(dia, mes):

    # Aqui o código verifica se o usuário é aluno ou professor, por conta da variação dos dias disponíveis para devolução

    if usuario == 1:

        # Aqui o código verifica o mês que foi digitado, sendo estes os meses que tem 31 dias

        if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:

            # Aqui o código verifica se com os dias de devolução já tendo passado o mês acabou ou não, determinando se ele deve mudar o mês

            if dia + 15 > 31:

                # Aqui é definido o resto, quantidade de dias passados no mês SEGUINTE caso houve a troca de mês, retornando a data de devolução

                resto = (dia + 15) - 30
                dia = resto
                mes += 1
                return(f'{dia}/{mes}')
            else:
                dia += 15
                return(f'{dia}/{mes}')

        # Aqui o código verifica o mês que foi digitado, sendo estes os meses que tem 30 dias

        elif mes == 4 or 6 or 9 or 11:

            # Aqui o código verifica se com os dias de devolução já tendo passado o mês acabou ou não, determinando se ele deve mudar o mês

            if dia + 15 > 30:

                # Aqui é definido o resto, quantidade de dias passados no mês SEGUINTE caso houve a troca de mês, retornando a data de devolução

                resto = (dia + 15) - 29
                dia = resto
                mes += 1
                return(f'{dia}/{mes}')
            else:
                dia += 15
                return(f'{dia}/{mes}')

        # Aqui o código verifica o mês que foi digitado, sendo estes os meses que tem 28 dias (fevereiro)

        elif mes == 2:

            # Aqui o código verifica se com os dias de devolução já tendo passado o mês acabou ou não, determinando se ele deve mudar o mês

            if dia + 15 > 28:

                # Aqui é definido o resto, quantidade de dias passados no mês SEGUINTE caso houve a troca de mês, retornando a data de devolução

                resto = (dia + 15) - 27
                dia = resto
                mes += 1
                return(f'{dia}/{mes}')
            else:
                dia += 15
                return(f'{dia}/{mes}')
        else:
            print('Valor inválido')
    else:

        # Aqui é iniciado o bloco para caso o usuário seja professor

        # Aqui o código verifica o mês que foi digitado, sendo estes os meses que tem 31 dias

        if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if dia + 20 > 31:

                # Aqui é definido o resto, quantidade de dias passados no mês SEGUINTE caso houve a troca de mês, retornando a data de devolução

                resto = (dia + 20) - 30
                dia = resto
                mes += 1
                return(f'{dia}/{mes}')
            else:
                dia += 20
                return(f'{dia}/{mes}')

        # Aqui o código verifica o mês que foi digitado, sendo estes os meses que tem 30 dias

        elif mes == 4 or 6 or 9 or 11:
            if dia + 20 > 30:

                # Aqui é definido o resto, quantidade de dias passados no mês SEGUINTE caso houve a troca de mês, retornando a data de devolução

                resto = (dia + 20) - 29
                dia = resto
                mes += 1
                return(f'{dia}/{mes}')
            else:
                dia += 20
                return(f'{dia}/{mes}')

        # Aqui o código verifica o mês que foi digitado, sendo estes os meses que tem 28 dias (fevereiro)
        
        elif mes == '2':
            if dia + 20 > 28:

                # Aqui é definido o resto, quantidade de dias passados no mês SEGUINTE caso houve a troca de mês, retornando a data de devolução

                resto = (dia + 20) - 27
                dia = resto
                mes += 1
                return(f'{dia}/{mes}')
            else:
                dia += 20
                return(f'{dia}/{mes}')
        else:
            print('Valor inválido')

# É convertido em texto o que foi inserido pelo usuário em resposta ao tipo

if usuario == 1:
    tipo = 'Aluno'
else:
    tipo = 'Professor'

# Impressão do recibo com chamamento da função de calcular data

os.system('cls')
print(10*'=', 'RECIBO', 10*'=')
print(f'> Nome do livro: {livro}')
print(f'> Tipo de usuário: {tipo}')
print(f'> Data do empréstimo: {data}')
print(f'> Data da devolução: {calcular_data(dia, mes)}')
print(28*'=')