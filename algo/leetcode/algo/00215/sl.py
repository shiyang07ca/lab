"""

[215] Kth Largest Element in an Array


Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.


--------------------------------------------------

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
--------------------------------------------------

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:


	1 <= k <= nums.length <= 10⁵
	-10⁴ <= nums[i] <= 10⁴


################################################################

215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5


示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4


提示：

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104


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

from heapq import *


import math
from functools import total_ordering


@total_ordering
class Wrapper:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        wrapper_heap = list(map(lambda item: Wrapper(item), nums))
        heapify(wrapper_heap)
        ans = Wrapper(math.inf)
        while k:
            n = heappop(wrapper_heap)
            # print(n.val, ans.val, k)
            if n >= ans:
                k -= 1
                ans = n

        return ans.val


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        self.assertEqual(
            self.sl.findKthLargest(nums, k),
            5,
        )

        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        self.assertEqual(
            self.sl.findKthLargest(nums, k),
            4,
        )


if __name__ == "__main__":
    unittest.main()
