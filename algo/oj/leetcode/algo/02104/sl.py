"""

[2104] Sum of Subarray Ranges


You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:


Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

Example 2:


Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.


Example 3:


Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.



Constraints:


	1 <= nums.length <= 1000
	-10⁹ <= nums[i] <= 10⁹



Follow-up: Could you find a solution with O(n) time complexity?


################################################################


2104. 子数组范围和
给你一个整数数组 nums 。nums 中，子数组的 范围 是子数组中最大元素和最小元素的差值。

返回 nums 中 所有 子数组范围的 和 。

子数组是数组中一个连续 非空 的元素序列。


示例 1：

输入：nums = [1,2,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0
[2]，范围 = 2 - 2 = 0
[3]，范围 = 3 - 3 = 0
[1,2]，范围 = 2 - 1 = 1
[2,3]，范围 = 3 - 2 = 1
[1,2,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4


示例 2：

输入：nums = [1,3,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0
[3]，范围 = 3 - 3 = 0
[3]，范围 = 3 - 3 = 0
[1,3]，范围 = 3 - 1 = 2
[3,3]，范围 = 3 - 3 = 0
[1,3,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4


示例 3：

输入：nums = [4,-2,-3,4,1]
输出：59
解释：nums 中所有子数组范围的和是 59


提示：

1 <= nums.length <= 1000
-109 <= nums[i] <= 109


进阶：你可以设计一种时间复杂度为 O(n) 的解决方案吗？

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *
from copy import *
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # oj
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        N = len(nums)
        mist, mast = [], []
        mipos, mapos = [[]] * N, [[]] * N
        for i, n in enumerate(nums):
            while mist and nums[mist[-1]] > n:
                popi = mist.pop()
                l = mist[-1] if mist else -1
                mipos[popi] = [l, i]
            mist.append(i)

            while mast and nums[mast[-1]] < n:
                popi = mast.pop()
                l = mast[-1] if mast else -1
                mapos[popi] = [l, i]
            mast.append(i)

        while mist:
            popi = mist.pop()
            l = mist[-1] if mist else -1
            mipos[popi] = [l, N]

        while mast:
            popi = mast.pop()
            l = mast[-1] if mast else -1
            mapos[popi] = [l, N]
        # print(mipos, mapos)

        ans = 0
        for i in range(N):
            l, r = mipos[i]
            ans -= nums[i] * ((i - l - 1) * (r - i) + (r - i - 1))
            l, r = mapos[i]
            ans += nums[i] * ((i - l - 1) * (r - i) + (r - i - 1))

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 2, 3]
        self.assertEqual(
            self.sl.subArrayRanges(nums),
            4,
        )

        nums = [1, 3, 3]
        self.assertEqual(
            self.sl.subArrayRanges(nums),
            4,
        )

        nums = [4, -2, -3, 4, 1]
        # self.sl.subArrayRanges(nums)
        self.assertEqual(
            self.sl.subArrayRanges(nums),
            59,
        )


if __name__ == "__main__":
    unittest.main()
