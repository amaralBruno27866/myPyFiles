def loopSimples(n):
    for i in range(n): # 1 operation
        print(i) # 1 operation

"""
Analysis

#1 Set variables
- n: the amount of times that the loop must iterate
-------------------------------------------------------------------------------

#2 Count operations
- 2 operations (increment i and print i)
-------------------------------------------------------------------------------

#3 Mathematical expression
- T(n) = 1 + 1 * n
-------------------------------------------------------------------------------

#4 Simplify expression
- T(n) = 2n
-------------------------------------------------------------------------------

#5 Final result (complexity)
- O(n) Linear curve
-------------------------------------------------------------------------------

"""

loopSimples(100)
