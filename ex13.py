def knapsack_programacao_dinamica(capacidade, pesos, valores, n):
    tabela = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                tabela[i][w] = max(valores[i - 1] + tabela[i - 1][w - pesos[i - 1]], tabela[i - 1][w])
            else:
                tabela[i][w] = tabela[i - 1][w]

    return tabela[n][capacidade]


pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
n = len(pesos)

print(f'ex13: {knapsack_programacao_dinamica(capacidade, pesos, valores, n)}')
