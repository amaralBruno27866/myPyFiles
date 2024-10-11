def search(lst, key):
    for i in range(len(lst)): # 2 operations
        if lst[i] == key: # 2 operation
            return i # 1 operation
    return -1 # 1 operation

"""
Analysis

#1 Set variables
- lst: represents the list that will be used to search for the key.
- key: represents the element that will be searched in the list.
-------------------------------------------------------------------------------

#2 Count operations
- We have a total of 9 operations
    - For Loop: 2 operations
        - print(i): 1 operation
        - If return treu: 2 operations
            - print(f"Element {key} found at index {i}"): 1 operation
            - return i: 1 operation
                - Total 4 operations inside the loop
        - If return false: 2 operations
            - print(f"Element {key} not found"): 1 operation
            - return -1: 1 operation
                - Total 4 operations inside the loop
-------------------------------------------------------------------------------

#3 Mathematical expression
- lst[i] == key: T(n) = 2n + 2
- lst[i] != key: T(n) = 2n + 2
-------------------------------------------------------------------------------

#4 Simplify expression
- lst[i] == key: T(n) = 7
- lst[i] != key: T(n) = 5n +2
-------------------------------------------------------------------------------

#5 Final result (complexity)
- O(n) Linear curve
-------------------------------------------------------------------------------

"""

search([1, 2, 3, 4, 5], 6)

