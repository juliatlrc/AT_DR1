import random

livros = sorted(random.randint(1000000000, 9999999999) for _ in range(100000))
isbn_procurado = random.choice(livros)

def busca_binaria(livros, isbn):
    esquerda, direita = 0, len(livros) - 1
    iteracoes = 0
    while esquerda <= direita:
        iteracoes += 1
        meio = (esquerda + direita) // 2
        if livros[meio] == isbn:
            return iteracoes
        elif livros[meio] < isbn:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return iteracoes

def busca_linear(livros, isbn):
    iteracoes = 0
    for livro in livros:
        iteracoes += 1
        if livro == isbn:
            return iteracoes
    return iteracoes

iteracoes_binaria = busca_binaria(livros, isbn_procurado)
iteracoes_linear = busca_linear(livros, isbn_procurado)

print(f"ex4: Busca Binária - Iterações: {iteracoes_binaria}")
print(f"ex4: Busca Linear - Iterações: {iteracoes_linear}")
