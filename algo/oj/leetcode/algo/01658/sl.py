"""

[1658] Minimum Operations to Reduce X to Zero


You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.


Example 1:


Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.


Example 2:


Input: nums = [5,6,7,8,9], x = 4
Output: -1


Example 3:


Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.



Constraints:


	1 <= nums.length <= 10⁵
	1 <= nums[i] <= 10⁴
	1 <= x <= 10⁹

################################################################

# tag: Sliding Window, Prefix Sum
# TODO

1658. 将 x 减到 0 的最小操作数

给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。

如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。



示例 1：

输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。


示例 2：

输入：nums = [5,6,7,8,9], x = 4
输出：-1


示例 3：

输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109



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


# 双指针
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # x = 5
        # 1, 1, 4, 2, 3
        # 返回sum(nums) - x 的最长长度
        t = sum(nums) - x
        if t < 0:
            return -1

        ans = -1
        tot = l = r = 0
        while r < len(nums):
            tot += nums[r]
            while tot > t:
                tot -= nums[l]
                l += 1
            if tot == t:
                ans = max(ans, r - l + 1)
            r += 1
        #         print(ans)
        #         print(t)
        return -1 if ans == -1 else len(nums) - ans


"""
https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/solution/by-lcbin-fnue/

方法一：哈希表 + 前缀和

我们可以将问题转换为求中间连续子数组的最大长度，使得子数组的和为 x = sum(nums) -
x


定义一个哈希表 vis，其中 vis[s] 表示前缀和为 s 的最小下标。

遍历数组 nums，对于每个元素 nums[i]，我们先将 nums[i] 加到前缀和 s 上，如果哈希
表中不存在 s，则将其加入哈希表，其值为当前下标 i。然后我们判断 s - x 是否在哈希
表中，如果存在，则说明存在一个下标 j，使得 nums[j + 1,..i] 的和为 x，此时我们更
新答案的最小值，即 ans = min(ans, n - (i - j))

遍历结束，如果找不到满足条件的子数组，返回 -1，否则返回 ans。
"""


class Solution1:
    def minOperations(self, nums: List[int], x: int) -> int:
        x = sum(nums) - x
        vis = {0: -1}
        ans = inf
        s, n = 0, len(nums)
        for i, v in enumerate(nums):
            s += v
            if s not in vis:
                vis[s] = i
            if s - x in vis:
                j = vis[s - x]
                ans = min(ans, n - (i - j))
        return -1 if ans == inf else ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.sl = Solution()
        self.sl = Solution1()

    def test_sl(self):
        ns = [1, 1, 4, 2, 3]
        x = 5
        self.assertEqual(
            self.sl.minOperations(ns, x),
            2,
        )

        ns = [5, 6, 7, 8, 9]
        x = 4
        self.assertEqual(
            self.sl.minOperations(ns, x),
            -1,
        )

        ns = [3, 2, 20, 1, 1, 3]
        x = 10
        self.assertEqual(
            self.sl.minOperations(ns, x),
            5,
        )


if __name__ == "__main__":
    unittest.main()
