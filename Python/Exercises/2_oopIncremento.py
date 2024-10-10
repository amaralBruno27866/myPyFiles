def loop_incremento(n):
  for i in range(0, n, 2): # 1 operations
    print(i) # 1 operation

"""
Analysis

#1 Set variables
- n: the amount of times that the loop must iterate
-------------------------------------------------------------------------------

#2 Count operations
- For each iteration inside the loop we have 1 operations
  - 1 operation (increment i)
  - 1 operation (print i)
-------------------------------------------------------------------------------

#3 Mathematical expression
- T(n) = 2 * (n/2)
-------------------------------------------------------------------------------

#4 Simplify expression
- T(n) = n
-------------------------------------------------------------------------------

#5 Final result (complexity)
- O(n) Linear curve
-------------------------------------------------------------------------------

"""

loop_incremento(10)
