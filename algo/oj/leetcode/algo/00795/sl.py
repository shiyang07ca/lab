"""

[795] Number of Subarrays with Bounded Maximum


Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.


Example 1:


Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].


Example 2:


Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7



Constraints:


	1 <= nums.length <= 10⁵
	0 <= nums[i] <= 10⁹
	0 <= left <= right <= 10⁹


################################################################

# TODO
# tag: monotonic stack
# 贡献法


795. 区间子数组个数
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最
大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。


生成的测试用例保证结果符合 32-bit 整数范围。


示例 1：

输入：nums = [2,1,4,3], left = 2, right = 3
输出：3
解释：满足条件的三个子数组：[2], [2, 1], [3]


示例 2：

输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7


提示：

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9


"""

import sys
import inspect
import os
import unittest

from itertools import *
from collections import *
from copy import *
from typing import *
from math import *

from os.path import abspath, join, dirname

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
    def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int) -> int:
        N = len(nums)
        left = [-1] * N  # left[i] 为左侧严格大于 nums[i] 的最近元素位置（不存在时为-1）
        right = [N] * N  # left[i] 为右侧大于等于 nums[i] 的最近元素位置（不存在时为 N）
        st = []
        for i, n in enumerate(nums):
            while st and nums[st[-1]] <= n:
                popi = st.pop()
                right[popi] = i
            left[i] = st[-1] if st else -1
            st.append(i)

        ans = 0
        for i, n in enumerate(nums):
            if l <= n <= r:
                print(left[i], i, right[i], n, (i - left[i]) * (right[i] - i))
                ans += (i - left[i]) * (right[i] - i)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [2, 1, 4, 3]
        left = 2
        right = 3
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            3,
        )

        nums = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
        left = 32
        right = 69
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            22,
        )

        nums = [2, 9, 2, 5, 6]
        left = 2
        right = 8
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            7,
        )

        nums = [4]
        left = 5
        right = 6
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            0,
        )

        nums = [4]
        left = 1
        right = 2
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            0,
        )


if __name__ == "__main__":
    unittest.main()
