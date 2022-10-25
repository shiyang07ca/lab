"""

[34] Find First and Last Position of Element in Sorted Array


Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


--------------------------------------------------

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
--------------------------------------------------

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
--------------------------------------------------

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]


Constraints:


	0 <= nums.length <= 10⁵
	-10⁹ <= nums[i] <= 10⁹
	nums is a non-decreasing array.
	-10⁹ <= target <= 10⁹


################################################################

# TODO
# tag: binary search
# template

34. 在排序数组中查找元素的第一个和最后一个位置

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。


示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]


示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]


示例 3：

输入：nums = [], target = 0
输出：[-1,-1]


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109


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
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if len(nums) == 0:
            return ans

        l, r = 0, len(nums) - 1
        # 找左边界
        # [l, mid], [mid + 1, l]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            ans[0] = l
        else:
            return ans

        l, r = 0, len(nums) - 1
        # 找右边界
        # [l, mid - 1], [mid, r]
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        ans[1] = l

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):

        nums = [5, 7, 7, 8, 8, 10]
        t = 8
        self.assertEqual(
            self.sl.searchRange(nums, t),
            [3, 4],
        )

        nums = []
        t = 0
        self.assertEqual(
            self.sl.searchRange(nums, t),
            [-1, -1],
        )


if __name__ == "__main__":
    unittest.main()
