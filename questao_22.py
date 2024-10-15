# Importação da biblioteca OS para facilitar a visualização dos prints
import os
os.system('cls')

# É pedido um número ao usuário de 1 a 7, assim como é criada uma lista contendo cada dia da semana
num = int(input("Digite um número de 1 a 7: "))
dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

# Aqui acontece a verificação do número recebido, cujo será usado para buscar o dia correspondente na lista caso válido
if 0 < num < 8:
    os.system('cls')
    print(f'O número {num} corresponde ao dia da semana: {dias_semana[num - 1]}')
else:
    os.system('cls')
    print('Não existe dia da semana com esse número.')