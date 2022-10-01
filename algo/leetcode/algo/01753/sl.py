"""

[1753] Maximum Score From Removing Stones

################################################################

# TODO
# tag: greedy, priority queue

1753. 移除石子的最大得分


你正在玩一个单人游戏，面前放置着大小分别为 a​​​​​​、b 和 c​​​​​​ 的 三堆 石子。

每回合你都要从两个 不同的非空堆 中取出一颗石子，并在得分上加 1 分。当存在 两个或更多 的空堆时，游戏停止。

给你三个整数 a 、b 和 c ，返回可以得到的 最大分数 。


示例 1：

输入：a = 2, b = 4, c = 6
输出：6
解释：石子起始状态是 (2, 4, 6) ，最优的一组操作是：
- 从第一和第三堆取，石子状态现在是 (1, 4, 5)
- 从第一和第三堆取，石子状态现在是 (0, 4, 4)
- 从第二和第三堆取，石子状态现在是 (0, 3, 3)
- 从第二和第三堆取，石子状态现在是 (0, 2, 2)
- 从第二和第三堆取，石子状态现在是 (0, 1, 1)
- 从第二和第三堆取，石子状态现在是 (0, 0, 0)
总分：6 分 。


示例 2：

输入：a = 4, b = 4, c = 6
输出：7
解释：石子起始状态是 (4, 4, 6) ，最优的一组操作是：
- 从第一和第二堆取，石子状态现在是 (3, 3, 6)
- 从第一和第三堆取，石子状态现在是 (2, 3, 5)
- 从第一和第三堆取，石子状态现在是 (1, 3, 4)
- 从第一和第三堆取，石子状态现在是 (0, 3, 3)
- 从第二和第三堆取，石子状态现在是 (0, 2, 2)
- 从第二和第三堆取，石子状态现在是 (0, 1, 1)
- 从第二和第三堆取，石子状态现在是 (0, 0, 0)
总分：7 分 。


示例 3：

输入：a = 1, b = 8, c = 8
输出：8
解释：最优的一组操作是连续从第二和第三堆取 8 回合，直到将它们取空。
注意，由于第二和第三堆已经空了，游戏结束，不能继续从第一堆中取石子。


提示：

1 <= a, b, c <= 105

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

from heapq import *

from algo.tree.builder import *


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        arr = [-a, -b, -c]
        heapify(arr)
        ans = 0
        while True:

            """
            基于贪心思想拿石子，每次从剩余数目前两名的堆中拿，
            每次拿的数目应该等于 第二堆-最小堆的数目（这样可以使得第二堆和最小堆的石子数量一样）
            """
            max_ = -heappop(arr)
            medium = -heappop(arr)
            min_ = -arr[0]
            if medium == 0:
                return ans

            tmp = max(medium - min_, 1)
            max_ -= tmp
            medium -= tmp
            heappush(arr, -max_)
            heappush(arr, -medium)
            ans += tmp


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl.maximumScore(2, 4, 6),
            6,
        )
        self.assertEqual(
            self.sl.maximumScore(4, 4, 6),
            7,
        )
        self.assertEqual(
            self.sl.maximumScore(6, 2, 1),
            3,
        )

        self.assertEqual(
            self.sl.maximumScore(1, 8, 8),
            8,
        )


if __name__ == "__main__":
    unittest.main()
