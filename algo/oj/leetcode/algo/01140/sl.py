"""

[1140] Stone Game II


Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.


Example 1:


Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.


Example 2:


Input: piles = [1,2,3,4,5,100]
Output: 104



Constraints:


	1 <= piles.length <= 100
	1 <= piles[i] <= 10⁴

################################################################

# TODO
# tag: dp

1140. 石子游戏 II

爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 排成一行，每堆都有正整数颗石子 piles[i]。游戏以谁手中的石子最多来决出胜负。

爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初，M = 1。

在每个玩家的回合中，该玩家可以拿走剩下的 前 X 堆的所有石子，其中 1 <= X <= 2M。然后，令 M = max(M, X)。

游戏一直持续到所有石子都被拿走。

假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。



示例 1：

输入：piles = [2,7,9,4,4]
输出：10
解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。


示例 2:

输入：piles = [1,2,3,4,5,100]
输出：104


提示：

1 <= piles.length <= 100
1 <= piles[i] <= 104



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
https://leetcode.cn/problems/stone-game-ii/solution/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-jjax/

"""


# 尚未优化，会超时
class Solution:
    def stoneGameII(self, s: List[int]) -> int:
        n = len(s)
        for i in range(n - 2, -1, -1):
            s[i] += s[i + 1]  # 后缀和

        def dfs(i: int, m: int) -> int:
            if i + m * 2 >= n:  # 能全拿
                return s[i]
            return s[i] - min(dfs(i + x, max(m, x)) for x in range(1, m * 2 + 1))

        return dfs(0, 1)


# 记忆化搜索
class Solution:
    def stoneGameII(self, s: List[int]) -> int:
        n = len(s)
        for i in range(n - 2, -1, -1):
            s[i] += s[i + 1]  # 后缀和

        @cache
        def dfs(i: int, m: int) -> int:
            if i + m * 2 >= n:  # 能全拿
                return s[i]
            return s[i] - min(dfs(i + x, max(m, x)) for x in range(1, m * 2 + 1))

        return dfs(0, 1)


# 1 比 1 翻译成递推
"""
* dfs 改成 f 数组；
* 递归改成循环（每个参数都对应一层循环）；
* 递归边界改成 f 数组的初始值。由于本题的边界比较复杂，直接在递推中计算。
"""


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        s, n = 0, len(piles)
        f = [[0] * (n + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            s += piles[i]
            for m in range(1, i // 2 + 2):
                if i + m * 2 >= n:
                    f[i][m] = s
                else:
                    f[i][m] = s - min(f[i + x][max(m, x)] for x in range(1, m * 2 + 1))
        return f[0][1]


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
