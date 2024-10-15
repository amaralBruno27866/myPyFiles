def loopAninhado(n):
  for i in range(n): # 1 operation n times
    for j in range(n): # 1 operation n times
      print(i, j) # 1 operation n times

"""
Analysis

#1 Set variables
- n = number of iterations
-------------------------------------------------------------------------------

#2 Count operations
- 3 operations n times
-------------------------------------------------------------------------------

#3 Mathematical expression
- T(n) = n + n² + n²
-------------------------------------------------------------------------------

#4 Simplify expression
T(n) = n + 2n²
-------------------------------------------------------------------------------

#5 Final result (complexity)
T(n) = 2n² + n Complexity: O(n²)
-------------------------------------------------------------------------------

"""

loopAninhado(3)
