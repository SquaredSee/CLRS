#!/usr/bin/env python3

from math import floor


def max_crossing_subarray(A, l, m, h):
    """ find the max contiguous sub array that crosses the midpoint """
    l_sum = 0
    s = 0
    max_left = m
    for i in range(m, l, -1):
        # move backward from m to l
        s += A[i]
        if s > l_sum:
            # if the running total is greater than the current sum, set current sum and max
            l_sum = s
            max_left = i
    r_sum = 0
    s = 0
    max_right = m + 1
    for j in range(m + 1, h):
        # move forward from m+1 to h
        s = s + A[j]
        if s > r_sum:
            # if the running total is greater than the current sum, set current sum and max
            r_sum = s
            max_right = j
    return max_left, max_right, l_sum + r_sum


def max_subarray(A, l, h):
    """
    recursively find the left and right max contiguous subarray
    returns either the left, right, or crossing subarray with the highest sum
    """
    if l == h:
        # base case when subarray is one item in length
        return l, h, A[l]

    m = floor((l + h) / 2)

    # recursively find maximum subarrays within the defined subarrays
    l_low, l_high, l_sum = max_subarray(A, l, m)
    r_low, r_high, r_sum = max_subarray(A, m + 1, h)
    c_low, c_high, c_sum = max_crossing_subarray(A, l, m, h)

    if l_sum >= r_sum and l_sum >= c_sum:
        return l_low, l_high, l_sum
    elif r_sum >= l_sum and r_sum >= c_sum:
        return r_low, r_high, r_sum
    else:
        return c_low, c_high, c_sum


if __name__ == '__main__':
    import sys
    try:
        input_list = sys.argv[1]
    except IndexError:
        sys.exit('Usage: max_subarray.py [1,2,3,4]')
    input_list = [float(x) for x in input_list.strip('[]').split(',')]
    low, high, s = max_subarray(input_list, 0, len(input_list) - 1)
    print(input_list[low:high + 1])
