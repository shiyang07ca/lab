"""

[1814] Count Nice Pairs in an Array


You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:


	0 <= i < j < nums.length
	nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])


Return the number of nice pairs of indices. Since that number can be too large, return it modulo 10⁹ + 7.


Example 1:


Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.


Example 2:


Input: nums = [13,10,35,24,76]
Output: 4



Constraints:


	1 <= nums.length <= 10⁵
	0 <= nums[i] <= 10⁹

################################################################

# TODO

1814. 统计一个数组中好对子的数目

给你一个数组 nums ，数组中只包含非负整数。定义 rev(x) 的值为将整数 x 各个数字位反转得到的结果。比方说 rev(123) = 321 ， rev(120) = 21 。我们称满足下面条件的下标对 (i, j) 是 好的 ：

- 0 <= i < j < nums.length
- nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])


请你返回好下标对的数目。由于结果可能会很大，请将结果对 109 + 7 取余 后返回。


示例 1：

输入：nums = [42,11,1,97]
输出：2
解释：两个坐标对为：
 - (0,3)：42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121 。
 - (1,2)：11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12 。



示例 2：

输入：nums = [13,10,35,24,76]
输出：4


提示：

1 <= nums.length <= 105
0 <= nums[i] <= 109

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
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        for i, n in enumerate(nums):
            t = 0
            while n:
                t = t * 10 + n % 10
                n //= 10
            nums[i] = nums[i] - t

        ans = 0
        cnt = defaultdict(int)
        for n in nums:
            if cnt[n]:
                ans = (ans + cnt[n]) % MOD
            cnt[n] += 1

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
