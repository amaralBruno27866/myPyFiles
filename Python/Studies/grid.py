def overflow(grid, the_queue):
    # Percorre cada linha da grade
    for row in grid:
        # Adiciona a linha à fila se não estiver vazia
        if any(value != 0 for value in row):  # Verifica se há elementos não nulos
            the_queue.append(row)  # Adiciona a linha à fila
    
    return the_queue  # Retorna a fila após adicionar as linhas

# Grade original
grid = [
    [-2, 1, -3, -3, 0],
    [2, 0, 3, 2, 0],
    [0, 0, -3, 0, 0],
    [0, 0, 1, 0, 0]
]

# Fila inicial (vazia)
the_queue = []

# Chamada da função
result_queue = overflow(grid, the_queue)

# Exibindo a fila resultante
print("Elements added to the queue:")
for idx, item in enumerate(result_queue, start=1):
    print(f"{idx}: {item}")

# Exibir o valor de retorno (a fila)
print("\nReturn value (queue):", result_queue)
