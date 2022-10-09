"""

[493] Reverse Pairs


Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:


	0 <= i < j < nums.length and
	nums[i] > 2 * nums[j].



--------------------------------------------------

Example 1:


Input: nums = [1,3,2,3,1]
Output: 2
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1


--------------------------------------------------

Example 2:


Input: nums = [2,4,3,5,1]
Output: 3
Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1



Constraints:


	1 <= nums.length <= 5 * 10⁴
	-2³¹ <= nums[i] <= 2³¹ - 1

################################################################

# TODO
# tag: merge sort, BIT
# template

493. 翻转对

给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

示例 1:

输入: [1,3,2,3,1]
输出: 2
示例 2:

输入: [2,4,3,5,1]
输出: 3
注意:

给定数组的长度不会超过50000。
输入数组中的所有数字都在32位整数的表示范围内。

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0

        def merge(left, right, merged):
            # compute reverse pairs
            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] > 2 * right[r]:
                    self.ans += len(left) - l
                    r += 1
                else:
                    l += 1

            l, r = 0, 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged[l + r] = left[l]
                    l += 1
                else:
                    merged[l + r] = right[r]
                    r += 1

            for l in range(l, len(left)):
                merged[l + r] = left[l]

            for r in range(r, len(right)):
                merged[l + r] = right[r]

        def merge_count(arr):
            N = len(arr)
            if N <= 1:
                return arr

            mid = N // 2
            left, right = merge_count(arr[:mid]), merge_count(arr[mid:])

            merge(left, right, arr)
            return arr

        merge_count(nums)

        return self.ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n = [1, 3, 2, 3, 1]
        ans = 2
        self.assertEqual(
            self.sl.reversePairs(n),
            ans,
        )

        n = [2, 4, 3, 5, 1]
        ans = 3
        self.assertEqual(
            self.sl.reversePairs(n),
            ans,
        )


if __name__ == "__main__":
    unittest.main()
