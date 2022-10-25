"""

# TODO
# template
# tag: dp


322. 零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：

输入：coins = [2], amount = 3
输出：-1


示例 3：

输入：coins = [1], amount = 0
输出：0


提示：

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

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
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [-1] * amount
        for v in coins:
            # 完全背包模版
            # dp[i] 表示兑换 i 金额的最小硬币数
            for i in range(v, amount + 1):
                if dp[i - v] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i - v] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - v] + 1)

        return dp[amount]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(
            self.sl.coinChange(coins, amount),
            3,  # 11 = 5 + 5 + 1
        )

        coins = [2]
        amount = 3
        self.assertEqual(self.sl.coinChange(coins, amount), -1)

        coins = [1]
        amount = 0
        self.assertEqual(self.sl.coinChange(coins, amount), 0)


if __name__ == "__main__":
    unittest.main()
