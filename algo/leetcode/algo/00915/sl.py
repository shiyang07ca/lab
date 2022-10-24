"""

[915] Partition Array into Disjoint Intervals


Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:


	Every element in left is less than or equal to every element in right.
	left and right are non-empty.
	left has the smallest possible size.


Return the length of left after such a partitioning.

Test cases are generated such that partitioning exists.


Example 1:


Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]


Example 2:


Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]



Constraints:


	2 <= nums.length <= 10⁵
	0 <= nums[i] <= 10⁶
	There is at least one valid answer for the given input.

################################################################

915. 分割数组


给定一个数组 nums ，将其划分为两个连续子数组 left 和 right， 使得：

left 中的每个元素都小于或等于 right 中的每个元素。
left 和 right 都是非空的。
left 的长度要尽可能小。
在完成这样的分组后返回 left 的 长度 。

用例可以保证存在这样的划分方法。

示例 1：

输入：nums = [5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]


示例 2：

输入：nums = [1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]

提示：

2 <= nums.length <= 105
0 <= nums[i] <= 106
可以保证至少有一种方法能够按题目所描述的那样对 nums 进行划分。


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

from bisect import *


from algo.tree.builder import *


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # n1[i] 表示 0 ~ i 的最大值
        # n2[i] 表示 -1 ~ i 的最小值
        N = len(nums)
        n1, n2 = [nums[0]] * N, [nums[-1]] * N
        for i in range(1, N):
            n1[i] = max(nums[i], n1[i - 1])

        for i in range(N - 2, -1, -1):
            n2[i] = min(nums[i], n2[i + 1])

        # print(n1, n2)
        for i in range(N):
            if n1[i] <= n2[i + 1]:
                return i + 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [5, 0, 3, 8, 6]
        self.assertEqual(
            self.sl.partitionDisjoint(nums),
            3,
        )

        nums = [1, 1, 1, 0, 6, 12]
        self.assertEqual(
            self.sl.partitionDisjoint(nums),
            4,
        )

        nums = [1, 1]
        self.assertEqual(
            self.sl.partitionDisjoint(nums),
            1,
        )

        nums = [90, 47, 69, 10, 43, 92, 31, 73, 61, 97]
        self.assertEqual(
            self.sl.partitionDisjoint(nums),
            9,
        )

        nums = [26, 51, 40, 58, 42, 76, 30, 48, 79, 91]
        self.assertEqual(
            self.sl.partitionDisjoint(nums),
            1,
        )


if __name__ == "__main__":
    unittest.main()
