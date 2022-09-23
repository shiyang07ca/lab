"""

[75] Sort Colors


Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


--------------------------------------------------

Example 1:


Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


--------------------------------------------------

Example 2:


Input: nums = [2,0,1]
Output: [0,1,2]



Constraints:


	n == nums.length
	1 <= n <= 300
	nums[i] is either 0, 1, or 2.



Follow up: Could you come up with a one-pass algorithm using only constant extra space?


################################################################


75. 颜色分类


给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库的sort函数的情况下解决这个问题。



示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]


示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]


提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2


进阶：

你可以不使用代码库中的排序函数来解决这道题吗？
你能想出一个仅使用常数空间的一趟扫描算法吗？



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
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0, c1, c2 = 0, 0, 0
        for n in nums:
            if n == 0:
                c0 += 1
            elif n == 1:
                c1 += 1
            elif n == 2:
                c2 += 1

        for i in range(len(nums)):
            if c0:
                nums[i] = 0
                c0 -= 1
            elif c1:
                nums[i] = 1
                c1 -= 1
            elif c2:
                nums[i] = 2
                c2 -= 1


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
