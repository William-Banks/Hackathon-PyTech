# Importação da biblioteca OS para facilitar a visualização dos prints
import os

# Criação do loop para a exibição contínua do menu de opções da calculadora
while True:
    print('-'*10, 'Calculadora', '-'*10)
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('5. Potenciação')
    print('6. Sair da calculadora\n')

    # Recebimento da opção escolhida pelo usuário, determinando qual bloco será executado
    opcao = input('Escolha uma das opções: ')

    # Bloco de soma

    if opcao == '1':

        # São pedidos os dois números

        os.system('cls')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        # Impressão do resultado da operação a partir dos valores recebidos

        os.system('cls')
        print(f'O resultado da soma entre {num1} e {num2} é: ',num1 + num2)

    # Bloco de subtração
    elif opcao == '2':

        # São pedidos os dois números

        os.system('cls')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        # Impressão do resultado da operação a partir dos valores recebidos

        os.system('cls')
        print(f'O resultado da subtração entre {num1} e {num2} é: ',num1 - num2)

    # Bloco de multiplicação
    elif opcao == '3':

        # São pedidos os dois números

        os.system('cls')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        # Impressão do resultado da operação a partir dos valores recebidos

        os.system('cls')
        print(f'O resultado da multiplicação entre {num1} e {num2} é: ',num1 * num2)

    # Bloco de divisão
    elif opcao == '4':

        # São pedidos os dois números

        os.system('cls')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        # Impressão do resultado da operação a partir dos valores recebidos

        os.system('cls')
        print(f'O resultado da divisão entre {num1} e {num2} é: ',num1 / num2)
    
    # Bloco de potenciação
    elif opcao == '5':

        # São pedidos os dois números

        os.system('cls')
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))

        # Impressão do resultado da operação a partir dos valores recebidos

        os.system('cls')
        print(f'O resultado da potenciação entre {num1} e {num2} é: ',num1 ** num2)

    # Bloco para sair do sistema
    elif opcao == '6':
        break
    
    # Se a opção escolhida não estiver no menu, o sistema aguardará uma válida
    else:
        print('Opção inválida!\n')