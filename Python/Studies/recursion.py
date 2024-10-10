for _ in range(5):
  print("recursion with a for loop")

def recursion():
  print("recursion in infinite loop")

  return recursion()

def recursion_2(i, n):
  print("recursion with limit: ", i)
  i += 1
  if i == n:
    return
  else:
    recursion_2(i, n)

recursion_2(0, 100)