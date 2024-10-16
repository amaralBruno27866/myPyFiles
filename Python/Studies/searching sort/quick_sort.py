def quick_sort(mylist):
    recursive_quick_sort(mylist, 0, len(mylist) - 1)  # call recursive quicksort

def recursive_quick_sort(mylist, left, right, THRESHOLD=32):
    if right - left <= THRESHOLD:
        insertion_sort(mylist, left, right)
    else:
        pivot_position = partition(mylist, left, right)
        recursive_quick_sort(mylist, left, pivot_position - 1)
        recursive_quick_sort(mylist, pivot_position + 1, right)

def insertion_sort(mylist, left, right):
    for i in range(left + 1, right + 1):
        curr = mylist[i]  # store the first number in the unsorted part of
                          # of array into curr
        j = i
        # this loop shifts value within sorted part of array to open a spot for curr
        while j > left and mylist[j - 1] > curr:
            mylist[j] = mylist[j - 1]
            j = j - 1
        mylist[j] = curr

import random

def partition(mylist, left, right):
    # choose a random index between left and right inclusive
    pivot_location = random.randint(left, right)

    # get the pivot
    pivot = mylist[pivot_location]

    # move the pivot out of the way by swapping with
    # last value of partition.  This step is crucial as pivot will
    # end up "moving" if we don't get it out of the way which will
    # lead to inconsistent results.
    mylist[pivot_location] = mylist[right]
    mylist[right] = pivot

    end_of_smaller = left - 1

    # note the loop below does not look at pivot which is in mylist[right]
    for j in range(left, right):
        if mylist[j] <= pivot:
            end_of_smaller += 1
            mylist[end_of_smaller], mylist[j] = mylist[j], mylist[end_of_smaller]

    # restore the pivot
    mylist[end_of_smaller + 1], mylist[right] = mylist[right], mylist[end_of_smaller + 1]

    # and return its location
    return end_of_smaller + 1