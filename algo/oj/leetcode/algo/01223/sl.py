"""

[1223] Dice Roll Simulation


A die simulator generates a random number from 1 to 6 for each roll. You introduced a constraint to the generator such that it cannot roll the number i more than rollMax[i] (1-indexed) consecutive times.

Given an array of integers rollMax and an integer n, return the number of distinct sequences that can be obtained with exact n rolls. Since the answer may be too large, return it modulo 10⁹ + 7.

Two sequences are considered different if at least one element differs from each other.


Example 1:


Input: n = 2, rollMax = [1,1,2,2,2,3]
Output: 34
Explanation: There will be 2 rolls of die, if there are no constraints on the die, there are 6 * 6 = 36 possible combinations. In this case, looking at rollMax array, the numbers 1 and 2 appear at most once consecutively, therefore sequences (1,1) and (2,2) cannot occur, so the final answer is 36-2 = 34.


Example 2:


Input: n = 2, rollMax = [1,1,1,1,1,1]
Output: 30


Example 3:


Input: n = 3, rollMax = [1,1,1,2,2,3]
Output: 181



Constraints:


	1 <= n <= 5000
	rollMax.length == 6
	1 <= rollMax[i] <= 15

################################################################

# TODO
# tag: dp

1223. 掷骰子模拟

有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。

不过我们在使用它时有个约束，就是使得投掷骰子时，连续 掷出数字 i 的次数不能超过 rollMax[i]（i 从 1 开始编号）。

现在，给你一个整数数组 rollMax 和一个整数 n，请你来计算掷 n 次骰子可得到的不同点数序列的数量。

假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 模 10^9 + 7 之后的结果。



示例 1：

输入：n = 2, rollMax = [1,1,2,2,2,3]
输出：34
解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。


示例 2：

输入：n = 2, rollMax = [1,1,1,1,1,1]
输出：30


示例 3：

输入：n = 3, rollMax = [1,1,1,2,2,3]
输出：181


提示：

1 <= n <= 5000
rollMax.length == 6
1 <= rollMax[i] <= 15


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

"""

作者：endlesscheng
链接：https://leetcode.cn/problems/dice-roll-simulation/solution/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-sje6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dfs(i: int, last: int, left: int) -> int:
            if i == 0:
                return 1
            res = 0
            for j, mx in enumerate(rollMax):
                if j != last:
                    res += dfs(i - 1, j, mx - 1)
                elif left:
                    res += dfs(i - 1, j, left - 1)
            return res % MOD

        return sum(dfs(n - 1, j, mx - 1) for j, mx in enumerate(rollMax)) % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl,
            None,
        )


if __name__ == "__main__":
    unittest.main()
