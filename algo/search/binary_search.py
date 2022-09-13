"""

Binary Search

"""

import unittest


# 左笔右闭 [l, r]
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return None


# 左笔右开 [l, r)
def binary_search2(arr, target):
    l, r = 0, len(arr)
    while l < r:
        # [l, r]  mid
        # [2, 3]   2
        # [2, 4]   3
        # [2, 5]   3
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid

    return None


def binary_search_recur(array, low, high, val):
    """
    Worst-case Complexity: O(log(n))

    reference: https://en.wikipedia.org/wiki/Binary_search_algorithm
    """

    if low > high:  # error case
        return -1
    mid = (low + high) // 2
    if val < array[mid]:
        return binary_search_recur(array, low, mid - 1, val)
    if val > array[mid]:
        return binary_search_recur(array, mid + 1, high, val)
    return mid


class TestSuite(unittest.TestCase):
    def test_binary_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
        self.assertEqual(10, binary_search(array, 5))
        self.assertEqual(11, binary_search(array, 6))
        self.assertEqual(None, binary_search(array, 7))
        self.assertEqual(None, binary_search(array, -1))

        self.assertEqual(10, binary_search2(array, 5))
        self.assertEqual(11, binary_search2(array, 6))
        self.assertEqual(None, binary_search2(array, 7))
        self.assertEqual(None, binary_search2(array, -1))

        # Test binary_search_recur
        self.assertEqual(10, binary_search_recur(array, 0, 11, 5))
        self.assertEqual(11, binary_search_recur(array, 0, 11, 6))
        self.assertEqual(-1, binary_search_recur(array, 0, 11, 7))
        self.assertEqual(-1, binary_search_recur(array, 0, 11, -1))


if __name__ == "__main__":

    unittest.main()
