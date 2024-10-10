def sum_matrix(matrix):
    result = 0
    for row in matrix:
        # print(row)
        for element in row:
            # print(element)
            result += element
            print(result)
    return result

sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 45