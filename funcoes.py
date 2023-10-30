import random
import os
import time

# Função Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Função Selection Sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Função QuickSort Hoare
def quicksort_hoare(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    less, equal, greater = [], [], []
    for element in lista:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    return quicksort_hoare(less) + equal + quicksort_hoare(greater)

# Função QuickSort Lomuto
def quicksort_lomuto(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista.pop()
    lesser = [x for x in lista if x <= pivot]
    greater = [x for x in lista if x > pivot]
    return quicksort_lomuto(lesser) + [pivot] + quicksort_lomuto(greater)

# Função Radix Sort
def radix_sort(lista):
    if len(lista) == 0:
        return lista
    max_num = max(lista)
    exp = 1
    while max_num // exp > 0:
        counting_sort(lista, exp)
        exp *= 10

# Função Counting Sort (usada por Radix Sort)
def counting_sort(lista, exp):
    n = len(lista)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = lista[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = lista[i] // exp
        output[count[index % 10] - 1] = lista[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        lista[i] = output[i]

# Função Insertion Sort
def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key

# Função Merge Sort
def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        left_half = lista[:mid]
        right_half = lista[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lista[k] = left_half[i]
                i += 1
            else:
                lista[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            lista[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            lista[k] = right_half[j]
            j += 1
            k += 1

# Função Heapsort
def heapsort(lista):
    n = len(lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)

# Função para construir um heap máximo
def heapify(lista, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lista[left] > lista[largest]:
        largest = left
    if right < n and lista[right] > lista[largest]:
        largest = right
    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]
        heapify(lista, n, largest)

# Função para gerar uma lista ordenada de tamanho específico
def gerar_lista_ordenada(tamanho):
    return list(range(1, tamanho + 1))

# Função para gerar uma lista invertida de tamanho específico
def gerar_lista_invertida(tamanho):
    return list(range(tamanho, 0, -1))

# Função para gerar uma lista aleatória de tamanho específico
def gerar_lista_aleatoria(tamanho):
    return random.sample(range(1, tamanho + 1), tamanho)

# Função para escrever a lista em um arquivo
def escrever_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")


def gerar_todos_tipos(tamanho):
  tipos = ["ordenado", "invertido", "aleatorio"]
  for tipo in tipos:
      lista = None
      if tipo == "ordenado":
          lista = gerar_lista_ordenada(tamanho)
      elif tipo == "invertido":
          lista = gerar_lista_invertida(tamanho)
      elif tipo == "aleatorio":
          lista = gerar_lista_aleatoria(tamanho)

      if not os.path.exists("arquivos"):
          os.makedirs("arquivos")

      escrever_em_arquivo(lista, f"arquivos/{tipo}_{tamanho}.txt")
      print(f"Arquivo {tipo}_{tamanho}.txt gerado.")