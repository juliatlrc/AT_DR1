def localizar_contato(agenda, chave_nome):
    for registro in agenda:
        if registro["nome"] == chave_nome:
            return registro["celular"]
    return "Número não encontrado"

agenda_telefonica = [
    {"nome": "p1", "celular": "912345678"},
    {"nome": "p2", "celular": "923456789"},
    {"nome": "p3", "celular": "934567890"},
    {"nome": "3", "celular": "945678901"}
]

nome_procurado = "p3"

numero = localizar_contato(agenda_telefonica, nome_procurado)

if numero != "Número não encontrado":
    print(f"ex3: {nome_procurado} está com o número {numero}.")
else:
    print(f"ex3: O contato {nome_procurado} não foi localizado na agenda.")
