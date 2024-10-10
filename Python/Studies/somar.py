def sum1(n):
  sum = 0
  for i in range(n + 1):
    if i == 0:
      print(" ",i)
    else:
      print("+", i)
    sum += i
  return print("Total sum: ", sum)

print("Call sum1")
sum1(5)

print("-------------------")

def sum2(n):
  if n == 0:
    return 0
  if n == 5:
    print(" ", n)
  else:
    print("+", n)
  return n + sum2(n - 1)

print("Call sum2")
result = sum2(5)
print("Total: ",result)