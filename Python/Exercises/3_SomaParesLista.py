def sum_pairs(lst):
    result = 0 # 1 operation
    for i in range(0, len(lst), 2): # 2 operations
        result += lst[i] + lst[i + 1] # 4 operations
    print(result) # 1 operation
    return result # 1 operation

"""
Analysis

#1 Set variables
- lst: represents the list that will be used to calculate the sum of pairs.
- result: represents the sum of pairs.
-------------------------------------------------------------------------------

#2 Count operations
- We have a total of 8 operations.
    - 1 (result = 0) 
    - 2 (for loop) 
    - 4 (result += lst[i] + lst[i + 1]) 
    - 1 (print) 
    - 1 (return)
-------------------------------------------------------------------------------

#3 Mathematical expression
- T(n) = 1 + (4 * (n/2)) + 2
- T(n) = 1 + 2n + 2
-------------------------------------------------------------------------------

#4 Simplify expression
- T(n) = 2n + 3
-------------------------------------------------------------------------------

#5 Final result (complexity)
- O(n) Linear curve
-------------------------------------------------------------------------------

"""

sum_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
