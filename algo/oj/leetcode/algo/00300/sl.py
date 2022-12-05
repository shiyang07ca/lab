"""

# TODO

300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。


示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4


示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1


提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


进阶：

你能将算法的时间复杂度降低到 O(n log(n)) 吗?

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


def get_near_great(arr):
    ans = [None] * len(arr)
    stack = []

    for i, e in enumerate(arr):
        # 如果破坏了栈单调性
        while stack and arr[stack[-1][0]] < e:
            pop_indexs = stack.pop()
            # 取位于下面位置列表中，最晚加入的那个
            # left = stack[-1][-1] if stack else -1
            for p_i in pop_indexs:
                ans[p_i] = i

        if stack and arr[stack[-1][0]] == e:
            stack[-1].append(i)
        else:
            stack.append([i])

    while stack:
        pop_indexs = stack.pop()
        # 取位于下面位置列表中，最晚加入的那个
        # left = stack[-1][-1] if stack else -1
        for p_i in pop_indexs:
            ans[p_i] = -1

    return ans


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """"""

        # stack = get_near_great(nums)
        # print(stack)
        # checked = set()
        # ans = 0
        # for i, n in enumerate(nums):
        #     # if n not in checked:
        #         # checked.add(n)

        #     tmp = 1
        #     nexti = i
        #     while stack[nexti] != -1:
        #         print(n, nums[nexti], nexti, ans)
        #         if nexti in checked:
        #             break
        #         checked.add(nexti)
        #         nexti = stack[nexti]
        #         tmp += 1
        #     if tmp > ans:
        #         ans = tmp

        # return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    # def test_sl(self):
    #     nums = [10, 9, 2, 5, 3, 7, 101, 18]
    #     self.assertEqual(
    #         self.sl.lengthOfLIS(nums),
    #         4,
    #     )

    def test_sl2(self):
        nums = [0, 1, 0, 3, 2, 3]
        print(nums)
        self.assertEqual(
            self.sl.lengthOfLIS(nums),
            4,
        )

    # def test_sl3(self):
    #     nums = [7, 7, 7, 7, 7, 7, 7]
    #     self.assertEqual(
    #         self.sl.lengthOfLIS(nums),
    #         1,
    #     )


if __name__ == "__main__":
    unittest.main()
