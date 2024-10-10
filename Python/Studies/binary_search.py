def binarySearch(list, key):
  low = 0 # 1 operação =
  high = len(list) - 1 # 3 operações =, len(), -1

  while low <= high: # 1 operação <=

    mid = (low + high) // 2 # 3 operações //, +

    if list[mid] == key: # 1 operação ==
      return mid # 1 operação return  
    elif list[mid] < key: # 1 operação <
      low = mid + 1 # 2 operações =, +
    else:
      high = mid - 1 # 2 operações =, -

  return -1 # 1 operação return

# Anilise da função binarySearch(list, key)
# Variables
# - list: lista de valores
# - key: valor a ser buscado
# - low: valor inicial da lista
# - high: valor final da lista
# - mid: valor do meio da lista
# Count the operations
# - Inicialização: 4 operações
# - While: 1 operação
#   - Inicialização de mid: 3 operações
#   - low <= high and list[mid] == key: 2 operações
#   - low <= high and list[mid] != key and list[mid] < key: 3 operações 
#   - low <= high and list[mid] != key and list[mid] > key: 3 operações
#   - low > high: 1 operação
# Mathematica expression
# - Inicialização: T(n) = 4
# - Inicialização + low <= high + inicialização and list[mid] == key: T(n) = 10
# - Inicialização + low <= high + inicialização and list[mid] != key and list[mid] < key: T(n) = 12
# - Inicialização + low <= high + inicialização and list[mid] != key and list[mid] > key: T(n) = 12
# - Inicialização + low > high: T(n) = 6
