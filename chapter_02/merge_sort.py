#!/usr/bin/env python3

from math import floor


def merge(A, l, m, r):
    # l is the beginning of the first sub array
    # m is the end of the first sub array, m+1 is the beginning of the second
    # r is the end of the second sub array
    # n = r - l + 1 where n is the total number of items in the sub array

    # copy into left and right sub arrays
    # python string slicing has the first number included, last number excluded
    L = A[l:m + 1]
    R = A[m + 1:r + 1]

    i = 0
    j = 0
    k = l
    while i < len(L) and j < len(R):
        # iterate over left and right sub arrays, adding the smallest to the next index
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # copy remaining items over, only one of the below cases will occur per merge
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1


def merge_sort(A, l, r):
    # recursively go to smaller sub arrays until they are one item in length
    if l < r:
        m = floor((l + r) / 2)
        merge_sort(A, l, m)
        merge_sort(A, m + 1, r)
        merge(A, l, m, r)


if __name__ == '__main__':
    import sys
    try:
        input_list = sys.argv[1]
    except IndexError:
        sys.exit('Usage: insertion_sort.py [1,2,3,4]')
    input_list = input_list.strip('[]').split(',')
    merge_sort(input_list, 0, len(input_list) - 1)
    print(input_list)
