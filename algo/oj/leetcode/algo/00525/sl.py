"""

[525] Contiguous Array


Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


Example 1:


Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.


Example 2:


Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.



Constraints:


	1 <= nums.length <= 10⁵
	nums[i] is either 0 or 1.

################################################################

# tag: prefix sum

525. 连续数组

给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。


示例 1:

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。


示例 2:

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。


提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1

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
    def findMaxLength(self, nums: List[int]) -> int:
        a = list(accumulate([1 if n == 0 else -1 for n in nums], initial=0))
        cnt = {}
        ans = 0
        for i, c in enumerate(a):
            if c not in cnt:
                cnt[c] = i
            else:
                ans = max(ans, i - cnt[c])

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
