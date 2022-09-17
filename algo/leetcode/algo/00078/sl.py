"""

# TODO

# tag: 回溯 backtrack

78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

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


"""

def subsets(nums):
    '''
    O(2**n)
    '''

    def backtrack(res, nums, stack, pos):
        if pos == len(nums):
            res.append(list(stack))
        else:
            # take nums[pos]
            stack.append(nums[pos])
            backtrack(res, nums, stack, pos + 1)
            stack.pop()
            # dont take nums[pos]
            backtrack(res, nums, stack, pos + 1)

    res = []
    backtrack(res, nums, [], 0)
    return res

################################################################

simplified backtrack

def backtrack(res, nums, cur, pos):
    if pos >= len(nums):
        res.append(cur)
    else:
        backtrack(res, nums, cur+[nums[pos]], pos+1)
        backtrack(res, nums, cur, pos+1)
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            ans += [arr + [n] for arr in ans]
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 2, 3]
        ans = sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
        self.assertEqual(
            sorted(self.sl.subsets(nums)),
            ans,
        )

        nums = [0]
        ans = sorted([[], [0]])
        self.assertEqual(
            sorted(self.sl.subsets(nums)),
            ans,
        )


if __name__ == "__main__":
    unittest.main()
