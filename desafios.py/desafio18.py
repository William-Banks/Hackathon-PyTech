import os
os.system('cls')
while True:
    # Pedir ao usuário que digite uma opção:
    os.system('cls')
    print(20*'=', 'VIAGEM', 20*'=')
    print('> Digite 1. Para selecionar o carro tipo A')
    print('> Digite 2. Para selecionar o carro tipo B')
    print('> Digite 3. Para selecionar o carro tipo C')
    print('> Digite 4. Para ver as informações sobres os carros')
    opcao = input('Digite alguma opção:')
    
    # Caso a opção seja 1
    if opcao == '1':
        os.system('cls')
        # Pedir ao usuário o tamanho do precurso e o valor da gasolina:
        percurso = float(input('digite o tamanho do percurso em KM: '))
        gaso = float(input('digite o valor da gasolina em R$:'))
        # Definir o calculo do combustível gasto pelo carro no percuro e o custo da viagem:
        gaso_gasta = percurso / 16
        vlr = gaso * gaso_gasta
        # Mostrar resultados:
        print(f'O combustível consumido pelo carro A é de: {gaso_gasta:.3f}L')
        print(f'O valor estimado em reais da viagem é de: {vlr:.3f}R$')
        break

    # Caso a opção seja 2
    elif opcao == '2':
         os.system('cls')
         # Pedir ao usuário o tamanho do precurso e o valor da gasolina:
         percurso = float(input('digite o tamanho do percurso em KM: '))
         gaso = float(input('digite o valor da gasolina em R$:'))
         # Definir o calculo do combustível gasto pelo carro no percuro e o custo da viagem:
         gaso_gasta = percurso / 16
         gaso_gasta = percurso / 12
         vlr = gaso * gaso_gasta
         # Mostrar resultados:
         print(f'O combustível consumido pelo carro A é de: {gaso_gasta:.3f}L')
         print(f'O valor estimado em reais da viagem é de: {vlr:.3f}R$')
         break
    
    # Caso a opção seja 3
    elif opcao == '3':
         os.system('cls')
         # Pedir ao usuário o tamanho do precurso e o valor da gasolina:
         percurso = float(input('digite o tamanho do percurso em KM: '))
         gaso = float(input('digite o valor da gasolina em R$:'))
         # Definir o calculo do combustível gasto pelo carro no percuro e o custo da viagem:
         gaso_gasta = percurso / 8
         vlr = gaso * gaso_gasta
         # Mostrar resultados:
         print(f'O combustível consumido pelo carro A é de: {gaso_gasta:.3f}L')
         print(f'O valor estimado em reais da viagem é de: {vlr:.3f}R$')
         break
    
    # Caso a opçao seja 4
    elif opcao == '4':
         os.system('cls')
         # Mostrar ao usuário as informações de cada carro:
         print('Carro A: 16 KM/l')
         print('Carro B: 12 KM/l')
         print('Carro C: 8 KM/l')
         print('> Aperte a tecla ENTER para voltar')
         opcao = input('Digite alguma opção:')

    # Caso o usuário digite uma opção inválida
    else: 
         os.system('cls')
         print('Digite alguma opção válida!!')
         break

# Encerrando o sistema :)
print('Encerrando...')
         


    
    
    
    

