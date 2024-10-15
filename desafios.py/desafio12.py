import os
# Definir as conversões:
os.system('cls')
print(10*'=', 'CONVERSÕES', 10*'=')
pes = int(input('Digite o valor em pés:'))
polegada = 12 * pes
jarda = 3 * pes
milha = 1760 * jarda
os.system('cls')

#mostrar os resultados
print(10*'=', 'RESULTADO', 10*'=')
print(f'O valor em polegadas é: {polegada}.')
print(f'O valor em jardas é: {jarda}.')
print(f'O valor em milhas é: {milha}.')