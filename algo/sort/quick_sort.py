def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    p = arr.pop()
    greater = []
    lesser = []
    for e in arr:
        if e > p:
            greater.append(e)
        else:
            lesser.append(e)
    return quick_sort(lesser) + [p] + quick_sort(greater)


import random


def quick_sort2(arr):
    def partition(arr, lo, hi):
        pivot = arr[lo]
        i = lo + 1
        for j in range(lo + 1, hi):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
        arr[lo], arr[i - 1] = arr[i - 1], arr[lo]
        return i - 1

    def qs(arr, lo, hi):
        # print(lo, hi)
        if lo < hi:
            pivot = random.randint(lo, hi - 1)
            arr[pivot], arr[lo] = arr[lo], arr[pivot]
            pivot_index = partition(arr, lo, hi)
            qs(arr, lo, pivot_index)
            qs(arr, pivot_index + 1, hi)

    qs(arr, 0, len(arr))
    # print(arr)
    return arr


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.s = quick_sort
        self.s = quick_sort2
        # self.s = quick_sort_random

    def test1(self):
        self.assertEqual(self.s([0, 5, 3, 2, 2]), [0, 2, 2, 3, 5])

        self.assertEqual(self.s([-2, 5, 0, -45]), [-45, -2, 0, 5])

        self.assertEqual(self.s([]), [])


if __name__ == "__main__":
    unittest.main()
