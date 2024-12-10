class Node:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave):
        if not self.raiz:
            self.raiz = Node(chave)
        else:
            self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, node, chave):
        if chave < node.chave:
            if node.esquerda:
                self._inserir_recursivo(node.esquerda, chave)
            else:
                node.esquerda = Node(chave)
        else:
            if node.direita:
                self._inserir_recursivo(node.direita, chave)
            else:
                node.direita = Node(chave)

    def encontrar_minimo(self):
        return self._encontrar_minimo(self.raiz)

    def _encontrar_minimo(self, node):
        while node.esquerda:
            node = node.esquerda
        return node.chave

    def encontrar_maximo(self):
        return self._encontrar_maximo(self.raiz)

    def _encontrar_maximo(self, node):
        while node.direita:
            node = node.direita
        return node.chave

notas = [85, 70, 95, 60, 75, 90, 100]

arvore = ArvoreBinariaDeBusca()

for nota in notas:
    arvore.inserir(nota)

minimo = arvore.encontrar_minimo()
maximo = arvore.encontrar_maximo()

print(f"ex15: A menor nota é: {minimo}")
print(f"ex15: A maior nota é: {maximo}")
