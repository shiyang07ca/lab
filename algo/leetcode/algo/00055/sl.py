"""

# TODO
# tag: dp, greedy

[55] Jump Game


You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


--------------------------------------------------

Example 1:


Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


--------------------------------------------------

Example 2:


Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.



Constraints:


	1 <= nums.length <= 10⁴
	0 <= nums[i] <= 10⁵


################################################################


55. 跳跃游戏

给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。



示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。


提示：

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105

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

    # 超时
    from functools import cache

    @cache
    def recur(self, i):
        if i == (len(self.nums) - 1):
            return True

        if self.nums[i] == 0:
            return False

        for next_index in range(i + 1, i + self.nums[i] + 1):
            if next_index < len(self.nums):
                if self.recur(next_index):
                    return True

        return False

    # https://leetcode.cn/problems/jump-game/solution/tiao-yue-you-xi-by-leetcode-solution/
    def canJump(self, nums: List[int]) -> bool:
        # self.nums = nums
        # return self.recur(0)

        rightMost = 0
        for i, n in enumerate(nums):
            if i <= rightMost:
                rightMost = max(rightMost, i + n)

            if rightMost >= len(nums) - 1:
                return True

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        # 可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
        nums = [2, 3, 1, 1, 4]
        self.assertEqual(
            self.sl.canJump(nums),
            True,
        )

    def test_sl2(self):
        # 无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
        nums = [3, 2, 1, 0, 4]
        self.assertEqual(
            self.sl.canJump(nums),
            False,
        )


if __name__ == "__main__":
    unittest.main()
