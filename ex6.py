import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

precos_1000 = [random.uniform(1, 1000) for _ in range(1000)]
precos_10000 = [random.uniform(1, 1000) for _ in range(10000)]

inicio_1000 = time.time()
bubble_sort(precos_1000)
fim_1000 = time.time()

inicio_10000 = time.time()
bubble_sort(precos_10000)
fim_10000 = time.time()

print(f"ex06: Tempo de execução para 1000 elementos: {fim_1000 - inicio_1000:.6f} segundos")
print(f"ex06: Tempo de execução para 10000 elementos: {fim_10000 - inicio_10000:.6f} segundos")
