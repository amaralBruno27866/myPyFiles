def hanoi_tower(n, origin, destine, auxiliar, count=0):
  if n == 1:
    return count + 1
  else:
    count = hanoi_tower(n - 1, origin, auxiliar, destine, count)
    count += 1
    count = hanoi_tower(n - 1, auxiliar, destine, origin, count)
    return count
  
# Chamada da função
total_moves = hanoi_tower(30, "A", "C", "B")
print("Total moves:", total_moves)