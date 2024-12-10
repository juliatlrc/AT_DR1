class Navegador:
    def __init__(self):
        self.pilha_voltar = []
        self.pilha_avancar = []

    def visitar_pagina(self, pagina):
        self.pilha_voltar.append(pagina)
        self.pilha_avancar.clear()

    def voltar(self):
        if self.pilha_voltar:
            pagina_atual = self.pilha_voltar.pop()
            self.pilha_avancar.append(pagina_atual)
            return f"Voltando para: {pagina_atual}"
        return "Não há páginas para voltar."

    def avancar(self):
        if self.pilha_avancar:
            pagina_atual = self.pilha_avancar.pop()
            self.pilha_voltar.append(pagina_atual)
            return f"Avançando para: {pagina_atual}"
        return "Não há páginas para avançar."

navegador = Navegador()

navegador.visitar_pagina('Página 1')
navegador.visitar_pagina('Página 2')
navegador.visitar_pagina('Página 3')

print(navegador.voltar())
print(navegador.voltar())
print(navegador.avancar())
print(navegador.voltar())
print(navegador.avancar())
