def sum_pairs(lst):
    result = 0
    for i in range(0, len(lst), 2):
        result += lst[i] + lst[i + 1]
    print(result)
    return result

"""
Analysis

#1 Set variables

-------------------------------------------------------------------------------

#2 Count operations

-------------------------------------------------------------------------------

#3 Mathematical expression

-------------------------------------------------------------------------------

#4 Simplify expression

-------------------------------------------------------------------------------

#5 Final result (complexity)

-------------------------------------------------------------------------------

"""

sum_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
