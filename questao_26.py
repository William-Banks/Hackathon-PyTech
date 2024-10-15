# Importação da biblioteca OS para facilitar a visualização dos prints
import os

# Recebimento da palavra digitada pelo usuário como um string
os.system('cls')
palavra = str(input('Digite uma palavra: '))

# Verifica-se se a quantidade de caracteres dentro da palavra é divisível por 2, imprimindo o resultado final
if len(palavra) % 2 == 0:
    print('A quantidade de letras existentes nessa palavra é par: ',len(palavra))
else:
    print('A quantidade de letras existentes nessa palavra é ímpar: ',len(palavra))