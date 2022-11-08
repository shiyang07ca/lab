"""

[47] Permutations II


Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


Example 1:


Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]


Example 2:


Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



Constraints:


	1 <= nums.length <= 8
	-10 <= nums[i] <= 10

################################################################


47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。



示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10


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
    def process(self, nums, i, ans):
        if i == len(nums):
            ans.append(deepcopy(nums))

        # nums[..i) 是已经排好的范围
        # nums[i...] 是需要继续排列的范围
        visit = [False] * 10
        for j in range(i, len(nums)):
            if not visit[nums[j]]:
                visit[nums[j]] = True

                nums[i], nums[j] = nums[j], nums[i]
                self.process(nums, i + 1, ans)
                nums[i], nums[j] = nums[j], nums[i]

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.process(nums, 0, ans)
        return sorted(ans)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 1, 2]
        self.assertEqual(self.sl.permuteUnique(nums), [[1, 1, 2], [1, 2, 1], [2, 1, 1]])

        nums = [1, 2, 3]
        self.assertEqual(
            self.sl.permuteUnique(nums),
            [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
        )


if __name__ == "__main__":
    unittest.main()
