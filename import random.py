import random
import time

def bubble_sort(v):
    fim = len(v)
    trocas = 0  # Variável para contar as trocas
    comparacoes = 0  # Variável para contar as comparações

    while fim > 0:
        i = 0
        while i < fim - 1:
            comparacoes += 1  # Incrementa a contagem de comparações
            if v[i] > v[i + 1]:
                temp = v[i]
                v[i] = v[i + 1]
                v[i + 1] = temp
                trocas += 1
            i += 1
        fim -= 1

    return trocas, comparacoes  # Retorna o número de trocas e comparações

vetor = list(range(0, 101))
random.shuffle(vetor)

antes = time.time()
trocas, comparacoes = bubble_sort(vetor)
depois = time.time()

total = (depois - antes) * 1000

print("Vetor original:", vetor)
print("Vetor ordenado:", vetor)
print("Número de números alterados:", trocas)
print("Número total de comparações:", comparacoes)
print("Esse processo demorou: %0.2f ms" % total)
