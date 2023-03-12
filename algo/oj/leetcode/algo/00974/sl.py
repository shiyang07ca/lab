"""

[974] Subarray Sums Divisible by K


Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.


Example 1:


Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Example 2:


Input: nums = [5], k = 9
Output: 0



Constraints:


	1 <= nums.length <= 3 * 10⁴
	-10⁴ <= nums[i] <= 10⁴
	2 <= k <= 10⁴

################################################################

# tag: prefix sum

974. 和可被 K 整除的子数组

给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。

子数组 是数组的 连续 部分。



示例 1：

输入：nums = [4,5,0,-2,-3,1], k = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 k = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

示例 2:

输入: nums = [5], k = 9
输出: 0


提示:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104


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

# 同余定理


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        a = list(accumulate(nums, initial=0))
        cnt = defaultdict(int)
        ans = 0
        for p in a:
            ans += cnt[p % k]
            cnt[p % k] += 1

        return ans


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        a = list(accumulate(nums, initial=0))
        cnt = defaultdict(int)
        ans = 0
        for p in a:
            ans += cnt[p % k]
            cnt[p % k] += 1

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl,
            None,
        )


if __name__ == "__main__":
    unittest.main()
