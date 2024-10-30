import heapq

# Função para o Algoritmo de Prim
def prim_mst(graph):
    # Inicializa a MST e uma lista para verificar quais vértices foram visitados
    mst = []  # Lista que irá armazenar as arestas da MST
    visited = set()  # Conjunto de vértices que já estão na MST
    
    # Seleciona um vértice inicial (usaremos o vértice 0 neste exemplo)
    start_vertex = 0 # Vértice inicial
    visited.add(start_vertex) # Adiciona o vértice inicial ao conjunto de visitados

    # Heap (fila de prioridade) que conterá as arestas possíveis para MST
    edges = [(weight, start_vertex, dest) for dest, weight in graph[start_vertex]] # Lista de arestas possíveis
    heapq.heapify(edges)  # Converte a lista em um MinHeap baseado no peso

    while edges: # Enquanto houver arestas na heap
        # Pega a aresta de menor peso
        weight, src, dest = heapq.heappop(edges)

        # Se o destino já foi visitado, ignore esta aresta
        if dest in visited: # Se o destino já está na MST
            continue # Ignora a aresta

        # Caso contrário, essa é uma aresta válida para a MST
        mst.append((src, dest, weight)) # Adiciona a aresta à MST
        visited.add(dest) # Adiciona o destino ao conjunto de visitados

        # Adiciona as arestas que partem do vértice recém-adicionado
        for next_dest, next_weight in graph[dest]: # Para cada aresta (destino, peso) partindo do vértice recém-adicionado
            if next_dest not in visited: # Se o destino não está na MST
                heapq.heappush(edges, (next_weight, dest, next_dest)) # Adiciona a aresta à heap

    return mst # Retorna a MST

# Exemplo de grafo representado como um dicionário
graph = {
    0: [(1, 2), (2, 3)],
    1: [(0, 2), (2, 4), (3, 5)],
    2: [(0, 3), (1, 4), (3, 1)],
    3: [(1, 5), (2, 1), (4, 2)],
    4: [(3, 2), (5, 4)],
    5: [(4, 4)]
}

# Executa o algoritmo e imprime o resultado
mst = prim_mst(graph)
print("Arestas da MST e seus pesos:")
for src, dest, weight in mst:
    print(f"{src} -- {weight} -- {dest}")
