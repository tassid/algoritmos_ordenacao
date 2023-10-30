import random
import os  # Adicione esta linha
import time

def main():
  print("Bem-vindo ao gerador e ordenador de arquivos!")

  while True:
      print("\nEscolha uma opção:")
      print("1 - Gerar todos os tipos para 500k, 750k e 1M registros")
      print("2 - Gerar arquivo ordenado")
      print("3 - Gerar arquivo invertido")
      print("4 - Gerar arquivo aleatório")
      print("5 - Ordenar arquivos usando diferentes algoritmos de ordenação")
      print("6 - Busca Binária")
      print("7 - Sair")

      opcao = input("Opção: ")

      if opcao == "1":
          tamanhos = [500000, 750000, 1000000]
          for tamanho in tamanhos:
              gerar_todos_tipos(tamanho)
      elif opcao in ["2", "3", "4"]:
          tamanho = int(input("Digite o tamanho da lista: "))
          tipo = ""
          if opcao == "2":
              tipo = "ordenado"
          elif opcao == "3":
              tipo = "invertido"
          elif opcao == "4":
              tipo = "aleatorio"

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

      elif opcao == "5":
            tamanhos = [500000, 750000, 1000000]
            tipos = ["ordenado", "invertido", "aleatorio"]
            algoritmos = {
                "Selection Sort": selection_sort,
                "Bubble Sort": bubble_sort,
                "QuickSort Hoare": quicksort_hoare,
                "QuickSort Lomuto": quicksort_lomuto,
                "Radix Sort": radix_sort,
                "Insertion Sort": insertion_sort,
                "Merge Sort": merge_sort,
                "Heapsort": heapsort
            }

            for tamanho in tamanhos:
                for tipo in tipos:
                    arquivo_entrada = f"arquivos/{tipo}_{tamanho}.txt"
                    if not os.path.exists(arquivo_entrada):
                        print(f"Arquivo {tipo}_{tamanho}.txt não encontrado. Voltando ao menu.")
                        continue
                    with open(arquivo_entrada, 'r') as arquivo:
                        lista = [int(line.strip()) for line in arquivo]
                    for nome_algoritmo, algoritmo in algoritmos.items():
                        lista_copia = lista.copy()
                        print(f"Iniciando {nome_algoritmo} para {tipo}_{tamanho}.txt...")
                        inicio = time.time()
                        algoritmo(lista_copia)
                        fim = time.time()
                        arquivo_saida = f"resultados/{tipo}_{nome_algoritmo}_{tamanho}.txt"
                        escrever_em_arquivo(lista_copia, arquivo_saida)
                        tempo_execucao = fim - inicio
                        print(f"Tempo de execução do {nome_algoritmo}: {tempo_execucao:.6f} segundos.")
                        print(f"Resultados salvos em {arquivo_saida}.")
      elif opcao == "6":
          tamanho = int(input("Digite o tamanho da lista: "))
          chave = int(input("Digite a chave de busca: "))
          tipo = input("Digite o tipo de lista (ordenado, invertido ou aleatorio): ")

          arquivo_entrada = f"arquivos/{tipo}_{tamanho}.txt"

          if not os.path.exists(arquivo_entrada):
              print(f"Arquivo {tipo}_{tamanho}.txt não encontrado. Voltando ao menu.")
              continue

          with open(arquivo_entrada, 'r') as arquivo:
              lista = [int(line.strip()) for line in arquivo]

          print(f"Iniciando busca binária para {tipo}_{tamanho}.txt...")
          inicio = time.time()
          resultado = busca_binaria(lista, chave)
          fim = time.time()

          if resultado != -1:
              print(f"Chave encontrada no índice {resultado}.")
          else:
              print("Chave não encontrada.")

          tempo_execucao = fim - inicio
          print(f"Tempo de execução: {tempo_execucao:.6f} segundos.")


      elif opcao == "7":
          print("Saindo do programa.")
          break
      else:
          print("Opção inválida. Por favor, escolha uma opção válida.")


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


if __name__ == "__main__":
  main()