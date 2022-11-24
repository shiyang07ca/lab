"""

[494] Target Sum


You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.


	For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".


Return the number of different expressions that you can build, which evaluates to target.


Example 1:


Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


Example 2:


Input: nums = [1], target = 1
Output: 1



Constraints:


	1 <= nums.length <= 20
	0 <= nums[i] <= 1000
	0 <= sum(nums[i]) <= 1000
	-1000 <= target <= 1000

################################################################

# tag: dp, DFS

494. 目标和

给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。



示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3


示例 2：

输入：nums = [1], target = 1
输出：1


提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

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
from functools import *

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
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        sums = [nums[-1]] * N
        for i in range(N - 2, -1, -1):
            sums[i] = nums[i] + sums[i + 1]
        #         print(sums)

        @cache
        def dfs(i, cur):
            if i == N:
                if cur == target:
                    return 1
                return 0

            if sums[i] + cur < target or cur - sums[i] > target:  # 剪枝
                return 0

            return dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])

        return dfs(0, 0)


"""

https://algo.itcharge.cn/Solutions/0400-0499/target-sum/

动态规划

假设数组中所有元素和为 sum，数组中所有符号为 + 的元素为 sum_x，符号为 - 的元素和
为 sum_y。则 target = sum_x - sum_y。

而 sum_x + sum_y = sum。根据两个式子可以求出 2 * sum_x = target + sum ，即 sum_x
= (target + sum) / 2。

那么这道题就变成了，如何在数组中找到一个集合，使集合中元素和为 (target + sum) /
2。这就变为了求容量为 (target + sum) / 2 的 01 背包问题。


1. 定义状态
定义状态 dp[i] 表示为：填满容量为 i 的背包，有 dp[i] 种方法。

2. 状态转移方程
填满容量为 i 的背包的方法数来源于：

* 不使用当前 num：只使用之前元素填满容量为 i 的背包的方法数。
* 使用当前 num：填满容量 i - num 的包的方法数，再填入 num 的方法数。则动态规划的
状态转移方程为：dp[i] = dp[i] + dp[i - num]。

3. 初始化
初始状态下，默认填满容量为 0 的背包有 1 种办法。即 dp[i] = 1。

4. 最终结果
根据状态定义，最后输出 dp[sise]（即填满容量为 size 的背包，有 dp[size] 种方法）
即可，其中 size 为数组 nums 的长度。


"""


class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > abs(s) or (target + s) % 2 == 1:
            return 0
        size = (target + s) // 2
        dp = [0 for _ in range(size + 1)]
        dp[0] = 1
        for num in nums:
            for i in range(size, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
        return dp[size]


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.sl = Solution()
        self.sl = Solution1()

    def test_sl(self):
        nums = [1, 1, 1, 1, 1]
        t = 3
        self.assertEqual(
            self.sl.findTargetSumWays(nums, t),
            5,
        )

        nums = [1]
        t = 1
        self.assertEqual(
            self.sl.findTargetSumWays(nums, t),
            1,
        )


if __name__ == "__main__":
    unittest.main()
