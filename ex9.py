class Usuario:
    def __init__(self, nome_usuario, nome_completo, idade, email):
        self.nome_usuario = nome_usuario
        self.nome_completo = nome_completo
        self.idade = idade
        self.email = email

class SistemaRedeSocial:
    def __init__(self):
        self.hashtable = {}

    def adicionar_usuario(self, usuario):
        self.hashtable[usuario.nome_usuario] = usuario

    def recuperar_perfil(self, nome_usuario):
        return self.hashtable.get(nome_usuario, "Usuário não encontrado")

usuarios = [
    Usuario('pessoa1', 'Pessoa Um', 28, 'pessoa1@email.com'),
    Usuario('pessoa2', 'Pessoa Dois', 24, 'pessoa2@email.com'),
    Usuario('pessoa3', 'Pessoa Três', 30, 'pessoa3@email.com')
]

sistema = SistemaRedeSocial()
for usuario in usuarios:
    sistema.adicionar_usuario(usuario)

perfil_pessoa1 = sistema.recuperar_perfil('pessoa1')
perfil_pessoa3 = sistema.recuperar_perfil('pessoa3')
perfil_inexistente = sistema.recuperar_perfil('pessoa4')

print(f"ex9: Perfil de Pessoa 1: {vars(perfil_pessoa1)}")
print(f"ex9: Perfil de Pessoa 3: {vars(perfil_pessoa3)}")
print(f"ex9: Perfil inexistente: {perfil_inexistente}")
