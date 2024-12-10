import random

def selection_sort(jogadores):
    for i in range(len(jogadores)):
        menor = i
        for j in range(i+1, len(jogadores)):
            if jogadores[j]['pontuacao'] < jogadores[menor]['pontuacao']:
                menor = j
        jogadores[i], jogadores[menor] = jogadores[menor], jogadores[i]
    return jogadores

jogadores = [{'nome': f'Jogador {i}', 'pontuacao': random.randint(0, 100)} for i in range(10)]
jogadores_ordenados = selection_sort(jogadores)

for jogador in jogadores_ordenados:
    print(f'ex8: {jogador["nome"]}: {jogador["pontuacao"]}')
