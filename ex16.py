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

    def remover(self, chave):
        self.raiz = self._remover_recursivo(self.raiz, chave)

    def _remover_recursivo(self, node, chave):
        if node is None:
            return node
        if chave < node.chave:
            node.esquerda = self._remover_recursivo(node.esquerda, chave)
        elif chave > node.chave:
            node.direita = self._remover_recursivo(node.direita, chave)
        else:
            if node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            temp = self._minimo(node.direita)
            node.chave = temp.chave
            node.direita = self._remover_recursivo(node.direita, temp.chave)
        return node

    def _minimo(self, node):
        while node.esquerda:
            node = node.esquerda
        return node

    def em_ordem(self):
        return self._em_ordem_recursivo(self.raiz)

    def _em_ordem_recursivo(self, node):
        if node is None:
            return []
        return self._em_ordem_recursivo(node.esquerda) + [node.chave] + self._em_ordem_recursivo(node.direita)

codigos = [45, 25, 65, 20, 30, 60, 70]

arvore = ArvoreBinariaDeBusca()

for codigo in codigos:
    arvore.inserir(codigo)

print("ex16: Árvore em ordem:", arvore.em_ordem())

arvore.remover(20)
print("ex16: Árvore após remover 20:", arvore.em_ordem())

arvore.remover(25)
print("ex16: Árvore após remover 25:", arvore.em_ordem())

arvore.remover(45)
print("ex16: Árvore após remover 45:", arvore.em_ordem())
