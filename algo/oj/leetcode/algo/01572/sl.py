"""

[1572] Matrix Diagonal Sum


Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.


Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.


Example 2:


Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8


Example 3:


Input: mat = [[5]]
Output: 5



Constraints:


	n == mat.length == mat[i].length
	1 <= n <= 100
	1 <= mat[i][j] <= 100

################################################################

1752. 检查数组是否经排序和轮转得到
给你一个数组 nums 。nums 的源数组中，所有元素与 nums 相同，但按非递减顺序排列。

如果 nums 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 true ；否则，返回 false 。

源数组中可能存在 重复项 。

注意：我们称数组 A 在轮转 x 个位置后得到长度相同的数组 B ，当它们满足 A[i] == B[(i+x) % A.length] ，其中 % 为取余运算。



示例 1：

输入：nums = [3,4,5,1,2]
输出：true
解释：[1,2,3,4,5] 为有序的源数组。
可以轮转 x = 3 个位置，使新数组从值为 3 的元素开始：[3,4,5,1,2] 。

示例 2：

输入：nums = [2,1,3,4]
输出：false
解释：源数组无法经轮转得到 nums 。

示例 3：

输入：nums = [1,2,3]
输出：true
解释：[1,2,3] 为有序的源数组。
可以轮转 x = 0 个位置（即不轮转）得到 nums 。


提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100


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
    def check(self, nums: List[int]) -> bool:
        fi = pre = nums[0]
        flag = False
        #         print('=======')
        for i in range(1, len(nums)):
            #             print(pre, nums[i], flag)
            if not flag and nums[i] < pre:
                if fi < nums[i]:
                    return False
                flag = True
            elif flag:
                if nums[i] < pre or fi < nums[i]:
                    return False
            pre = nums[i]
        return True


# 作者：lcbin
# 链接：https://leetcode.cn/problems/check-if-array-is-sorted-and-rotated/solution/by-lcbin-qm10/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution1:
    def check(self, nums: List[int]) -> bool:
        return sum(v > nums[(i + 1) % len(nums)] for i, v in enumerate(nums)) <= 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution1()

    def test_sl(self):
        nums = [1, 3, 2]
        self.assertEqual(
            self.sl.check(nums),
            False,
        )

        nums = [8, 5, 4, 5, 1, 4, 5, 2, 2]
        self.assertEqual(
            self.sl.check(nums),
            False,
        )

        nums = [3, 4, 5, 1, 2]
        self.assertEqual(
            self.sl.check(nums),
            True,
        )

        nums = [2, 1, 3, 4]
        self.assertEqual(
            self.sl.check(nums),
            False,
        )

        nums = [1, 2, 3]
        self.assertEqual(
            self.sl.check(nums),
            True,
        )


if __name__ == "__main__":
    unittest.main()
