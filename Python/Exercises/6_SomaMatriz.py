def sum_matrix(matrix):
    result = 0
    for row in matrix:
        # print(row)
        for element in row:
            # print(element)
            result += element
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

sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 45
