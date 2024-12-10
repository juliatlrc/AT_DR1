class SistemaAtendimento:
    def __init__(self):
        self.fila_chamados = []

    def adicionar_chamado(self, chamado):
        self.fila_chamados.append(chamado)

    def atender_chamado(self):
        if self.fila_chamados:
            chamado_atendido = self.fila_chamados.pop(0)
            return f"Chamado atendido: {chamado_atendido}"
        return "Nenhum chamado para atender."

sistema = SistemaAtendimento()

sistema.adicionar_chamado('Chamado 1: Falha no sistema')
sistema.adicionar_chamado('Chamado 2: Erro 404')
sistema.adicionar_chamado('Chamado 3: Dúvida sobre a site')

print(f'ex11:{sistema.atender_chamado()}')
print(f'ex11:{sistema.atender_chamado()}')
print(f'ex11:{sistema.atender_chamado()}')
