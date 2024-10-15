# Importação da biblioteca OS para facilitar a visualização dos prints
import os

# Criação de uma lista contendo todas as vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# É pedido ao usuário que ele digite uma letra
os.system('cls')
letra = input('Digite uma letra: ')

# O input sofre uma verificação, caso esteja na lista é vogal, caso contrário consoante
if letra in vogais:
    print('A letra digitada é uma vogal.')
else:
    print('A letra digitada é uma consoante')