import random

pratos = {
    'Farofa de Cuscuz': 2,
    'Refrigerante': 2,
    'Ovo Mexido': 2,
    'Pão de Sal & Queijo': 2,
    'Pão de Sal & Presunto': 2,
    'Café': 2,
    'Salgados': 2,
    'Suco': 2,
    'Banana da Terra': 2,
    'Aipim Cozido': 2,
    'Calabresa Frita': 2,
    'Iogurte e Café': 2,
    'Bolo': 2,
    'Chocolate Quente': 2,
    'Torta Salgada': 2,
    'Cachorro Quente': 2,
    'Pipoca': 1
}

lista_final = {}

while True:
    nome = input('Digite seu nome (ou "000" para encerrar): ').strip().title()
    if nome == '000':
        break

    pratos_disponiveis = [prato for prato, qtd in pratos.items() if qtd > 0]

    if not pratos_disponiveis:
        print('Todos os pratos já foram escolhidos 2 vezes.')
        break

    prato_escolhido = random.choice(pratos_disponiveis)
    pratos[prato_escolhido] -= 1
    lista_final[nome] = prato_escolhido

    print(f'{nome}, você deve trazer: {prato_escolhido}')

print('\nLista final de participantes e seus pratos:')
for pessoa, prato in lista_final.items():
    print(f'{pessoa}: {prato}')
