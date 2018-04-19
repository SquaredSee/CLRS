#!/usr/bin/env python3


def insertion_sort(A):
    """ iterates through the array one item at a time, placing in the correct location """
    if type(A) is not list:
        raise TypeError('provided input is not a list')

    for j in range(1, len(A)):
        # key is the item currently being sorted
        key = A[j]
        i = j - 1

        # compare key with all items to the left
        while i >= 0 and A[i] > key:
            # move items right if they are greater than key
            A[i + 1] = A[i]
            # decrement i to move left through the list
            i = i - 1

        A[i + 1] = key


if __name__ == '__main__':
    import sys
    try:
        input_list = sys.argv[1]
    except IndexError:
        sys.exit('Usage: insertion_sort.py [1,2,3,4]')
    input_list = input_list.strip('[]').split(',')
    insertion_sort(input_list)
    print(input_list)
