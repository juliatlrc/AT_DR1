def verificar_duplicatas(lista):
    vistos = {}
    for item in lista:
        if item in vistos:
            return True
        vistos[item] = True
    return False

lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]
resultado = verificar_duplicatas(lista_teste)

if resultado:
    print("ex7: A lista contém duplicatas.")
else:
    print("ex7: A lista não contém duplicatas.")
