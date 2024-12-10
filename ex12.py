import os

def listar_arquivos(diretorio):
    for item in os.listdir(diretorio):
        caminho_completo = os.path.join(diretorio, item)
        if os.path.isdir(caminho_completo):
            listar_arquivos(caminho_completo)
        else:
            print(f'ex12: {caminho_completo}')

listar_arquivos('diretorios_aninhados')
