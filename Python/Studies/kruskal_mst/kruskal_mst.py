class DisjointSet: # Classe que implementa o conjunto disjunto
    def __init__(self, vertices): # Inicializa o conjunto disjunto
        self.parent = {v: v for v in vertices} # Inicializa o pai de cada vértice como ele mesmo
        self.rank = {v: 0 for v in vertices} # Inicializa a altura de cada vértice como 0

    def find(self, item): # Encontra o representante do conjunto de item
        if self.parent[item] != item: # Se o pai de item não é ele mesmo
            self.parent[item] = self.find(self.parent[item])  # Atualiza o pai de item para o pai do pai de item
        return self.parent[item] # Retorna o pai de item

    def union(self, set1, set2): # Une os conjuntos de set1 e set2
        root1 = self.find(set1) # Encontra o representante de set1
        root2 = self.find(set2) # Encontra o representante de set2

        if root1 != root2: # Se os representantes são diferentes
            if self.rank[root1] > self.rank[root2]: # Se a altura de root1 é maior que a altura de root2
                self.parent[root2] = root1 # O pai de root2 é atualizado para root1
            elif self.rank[root1] < self.rank[root2]: # Se a altura de root1 é menor que a altura de root2
                self.parent[root1] = root2 # O pai de root1 é atualizado para root2
            else: # Se as alturas são iguais
                self.parent[root2] = root1 # O pai de root2 é atualizado para root1
                self.rank[root1] += 1 # A altura de root1 é incrementada

class Graph: # Classe que implementa o grafo
    def __init__(self, vertices): # Inicializa o grafo
        self.vertices = vertices # Inicializa os vértices
        self.edges = [] # Inicializa as arestas

    def add_edge(self, u, v, weight): # Adiciona uma aresta ao grafo
        self.edges.append((weight, u, v)) # Adiciona a aresta (u, v, peso)

    def kruskal_mst(self): # Encontra a Árvore de Abrangência Mínima (MST) do grafo
        self.edges.sort() # Ordena as arestas por peso
        
        disjoint_set = DisjointSet(self.vertices) # Inicializa o conjunto disjunto
        mst = [] # Inicializa a MST
        
        for weight, u, v in self.edges: # Para cada aresta (u, v, peso) em ordem crescente de peso
            if disjoint_set.find(u) != disjoint_set.find(v): # Se u e v não estão no mesmo conjunto
                disjoint_set.union(u, v) # Une os conjuntos de u e v
                mst.append((u, v, weight)) # Adiciona a aresta (u, v, peso) à MST
        
        return mst # Retorna a MST

# Exemplo de uso:
vertices = ['A', 'B', 'C', 'D', 'E'] # Vértices do grafo
graph = Graph(vertices) # Inicializando o grafo

# Adicionando as arestas (u, v, peso)
graph.add_edge('A', 'B', 7) # Adiciona a aresta (A, B, 7)
graph.add_edge('A', 'E', 3) # Adiciona a aresta (A, E, 3)
graph.add_edge('B', 'E', 1) # Adiciona a aresta (B, E, 1)
graph.add_edge('B', 'C', 6) # Adiciona a aresta (B, C, 6)
graph.add_edge('E', 'D', 2) # Adiciona a aresta (E, D, 2)
graph.add_edge('D', 'C', 4) # Adiciona a aresta (D, C, 4)

# Encontrando a MST
mst = graph.kruskal_mst() # Encontra a MST
print("Arestas da Árvore de Abrangência Mínima (MST):") # Imprime as arestas da MST
for u, v, weight in mst: # Para cada aresta (u, v, peso) na MST
    print(f"{u} -- {v} com peso {weight}") # Imprime a aresta (u, v, peso)
