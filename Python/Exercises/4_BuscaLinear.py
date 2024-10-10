def search(lst, key):
    for i in range(len(lst)):
        print (i)
        if lst[i] == key:
            print(f"Element {key} found at index {i}")
            return i
    print(f"Element {key} not found")
    return -1

search([1, 2, 3, 4, 5], 1)
