def insertion_sort(my_list):
  for i in range(1, len(my_list)):
    curr = my_list[i]
    j = i
    while j > 0 and my_list[j - 1] > curr:
      my_list[j] = my_list[j - 1]
      j -= 1
    my_list[j] = curr
  return my_list

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print (my_list)
print (insertion_sort(my_list))