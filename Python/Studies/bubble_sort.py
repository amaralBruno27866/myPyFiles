def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

# Lista de valores
my_list = [64, 34, 25, 12, 22, 11, 90]

# Chamada da função
print("Sorted list:", my_list)
print("Sorted list:", bubble_sort(my_list))