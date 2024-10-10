def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 7
print(binary_search(lst, key))  # 6