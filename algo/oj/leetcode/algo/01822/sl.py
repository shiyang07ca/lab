"""

[1822] Sign of the Product of an Array


There is a function signFunc(x) that returns:


	1 if x is positive.
	-1 if x is negative.
	0 if x is equal to 0.


You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).


Example 1:


Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1


Example 2:


Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0


Example 3:


Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1



Constraints:


	1 <= nums.length <= 1000
	-100 <= nums[i] <= 100

################################################################


1822. 数组元素积的符号

已知函数 signFunc(x) 将会根据 x 的正负返回特定值：

如果 x 是正数，返回 1 。
如果 x 是负数，返回 -1 。
如果 x 是等于 0 ，返回 0 。
给你一个整数数组 nums 。令 product 为数组 nums 中所有元素值的乘积。

返回 signFunc(product) 。


示例 1：

输入：nums = [-1,-2,-3,-4,3,2,1]
输出：1
解释：数组中所有值的乘积是 144 ，且 signFunc(144) = 1


示例 2：

输入：nums = [1,5,0,2,-3]
输出：0
解释：数组中所有值的乘积是 0 ，且 signFunc(0) = 0


示例 3：

输入：nums = [-1,1,-1,1,-1]
输出：-1
解释：数组中所有值的乘积是 -1 ，且 signFunc(-1) = -1


提示：

1 <= nums.length <= 1000
-100 <= nums[i] <= 100


"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *

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
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                ans *= -1
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 5, 0, 2, -3]
        self.assertEqual(
            self.sl.arraySign(nums),
            0,
        )

        nums = [-1, -2, -3, -4, 3, 2, 1]
        self.assertEqual(
            self.sl.arraySign(nums),
            1,
        )

        nums = [-1, 1, -1, 1, -1]
        self.assertEqual(
            self.sl.arraySign(nums),
            -1,
        )
        nums = [
            56,
            32,
            76,
            92,
            78,
            91,
            -100,
            -82,
            -40,
            -63,
            -48,
            -55,
            -59,
            -81,
            -35,
            -59,
            -29,
        ]
        self.assertEqual(
            self.sl.arraySign(nums),
            -1,
        )


if __name__ == "__main__":
    unittest.main()
