def loopAninhado(n):
  for i in range(n):
    print(i)
    for j in range(n):
      print(j)
      print(i, j)

loopAninhado(3)