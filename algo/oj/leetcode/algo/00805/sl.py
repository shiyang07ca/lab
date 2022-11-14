"""

[805] Split Array With Same Average


You are given an integer array nums.

You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).

Return true if it is possible to achieve that and false otherwise.

* * * * * * * * * * * * * * * * * * * * * * * * *

Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.


Example 1:


Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.


Example 2:


Input: nums = [3,1]
Output: false



Constraints:


	1 <= nums.length <= 30
	0 <= nums[i] <= 10⁴

################################################################


805. 数组的均值分割
给定你一个整数数组 nums

我们要将 nums 数组中的每个元素移动到 A 数组 或者 B 数组中，使得 A 数组和 B 数组不为空，并且 average(A) == average(B) 。

如果可以完成则返回true ， 否则返回 false  。

注意：对于数组 arr ,  average(arr) 是 arr 的所有元素的和除以 arr 长度。


示例 1:

输入: nums = [1,2,3,4,5,6,7,8]
输出: true
解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。


示例 2:

输入: nums = [3,1]
输出: false


提示:

1 <= nums.length <= 30
0 <= nums[i] <= 104
通过次数17,329提交次数40,771

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
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(
            self.sl.splitArraySameAverage(nums),
            True,
        )

        nums = [3, 1]
        self.assertEqual(
            self.sl.splitArraySameAverage(nums),
            False,
        )


if __name__ == "__main__":
    unittest.main()
