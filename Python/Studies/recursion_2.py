def rec(myString, a, b):
  if a >= b:
    return True
  else:
    if myString[a] != myString[b]:
      return False
    else:
      return rec(myString, a+1, b-1)
    
def fun(myString):
  return rec(myString, 0, len(myString) - 1)

# Analise da função fun(myString)
# def fun(myString):
#   return rec(myString, 0, len(myString) - 1) # Total de 3 operações
# Nessa função temos apenas um return que faz a chamada recursiva de rec(myString, 0, len(myString) - 1)
# T(n) = 3

# Analise da função rec(myString, a b)
# def rec(myString, a, b):
#   if a >= b: # 1 operação >=
#     return True # 1 operação return
#   else:
#     if myString[a] != myString[b]: # 1 operação !=
#       return False # 1 operação return
#     else:
#       return rec(myString, a+1, b-1) # 1 operação +, 1 operação -, 1 operação rec
# Set variables
# - myString: representa a string que será analisada
# - a: representa o inicio da string
# - b: representa o final da string
# Count the operations
# - Caso base a >= b: 2 operações
# - Caso base a < b e myString[a] != myString[b]: 3 operações
# - Caso base a < b e myString[a] == myString[b]: 5 operações
# Mathematica expression
# - Caso base a >= b: T(n) = 2
# - Caso base a < b e myString[a] != myString[b]: T(n) = 3
# - Caso base a < b e myString[a] == myString[b]: T(n) = 5 + T(n-2)
# Simplyfy the equation
# - Considerando que temos T(n) = 5 + T(n -2) e T(0) = 0 e T(1) = 0, quando temos n > 1 nós teriomamos o seguinte:
#   - T(n) = 5 + T(n-2)
#   - T(n-2) = 5 + 5 + (T(n-4))
#   - T(n-4) = 5 + 5 + 5 + (T(n-6))
#   - ...
# - Isso demonstra que a cada iteração o valor de n é incrementado em 5 e o valor de n-2 é decrementado em 2, isso é feito ate que n = 0 ou 1, no final teriamos o seguinte:
# - T(n) = 5n/2 + 2 onde 5n é o total de operações, /2 são as reduções realizadas a cada iteração e - +2 são as duas ultimas operações realizadas quando chegamos ao caso base.
# Final Result
#  - Como a função fun(myString) apenas uma vez e essa tem 3 operações, nós adicionamos o total de operações da função rec(myString, a, b) que é 5n/2 + 2, logo temos:
#  - T(n) = (5 * (n / 2)) + 5, onde 5n é o total de operações da função rec(myString, a, b) quanto n > 1, /2 é a redução que fazermos a cada iteração e + 5 é o total de operações que temos quando somamos o caso base de n = 0 com as 3 operações da chamada da função fun().
