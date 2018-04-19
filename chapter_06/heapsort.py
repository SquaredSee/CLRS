#!/usr/bin/env python3

from math import floor


class Heap:
    def __init__(self):
        self._a = []

    def __str__(self):
        return str(self._a)

    def size(self):
        return len(self._a)

    def _parent_i(self, i):
        if i != 0:
            return floor(i / 2)
        else:
            return None

    def _left_i(self, i):
        result = 2 * i
        if result < self.size() - 1:
            return result
        else:
            return None

    def _right_i(self, i):
        result = 2 * i + 1
        if result < self.size() - 1:
            return result
        else:
            return None

    def parent(self, i):
        return self._a[self._parent_i(i)]

    def left(self, i):
        return self._a[self._left_i(i)]

    def right(self, i):
        return self._a[self._right_i(i)]

    def _max_heapify(self, i):
        l = self._left_i(i)
        r = self._right_i(i)

        # find the largest item of the subtree (root, left, and right)
        if l <= self.size() - 1 and self._a[l] > self._a[i]:
            largest = l
        else:
            largest = i
        if r <= self.size() - 1 and self._a[r] > self._a[largest]:
            largest = r

        # swap the largest index with the current index if not equal and recursively heapify the swapped index
        if largest != i:
            self._a[i], self._a[largest] = self._a[largest], self._a[i]
            self._max_heapify(largest)

    def add_item(self, item):
        self._a.append(item)
        if self.size() == 1:
            # initial item, no need to heapify
            return
        p_index = self._parent_i(self.size() - 1)
        cur_index = self.size() - 1
        while cur_index != 0 and self._a[p_index] < self._a[cur_index]:
            self._a[p_index], self._a[cur_index] = self._a[cur_index], self._a[p_index]
            cur_index = p_index
            p_index = self._parent_i(cur_index)
