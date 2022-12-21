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


"""
基于贪心思想拿石子，每次从剩余数目前两名的堆中拿，
每次拿的数目应该等于 第二堆 - 最小堆的数目
（这样可以使得第二堆和最小堆的石子数量一样）
"""


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        h = [-a, -b, -c]
        heapify(h)
        ans = 0
        while True:
            ma = -heappop(h)
            med = -heappop(h)
            mi = -h[0]
            if med == 0:
                return ans

            t = max(med - mi, 1)
            ans += t
            heappush(h, -(ma - t))
            heappush(h, -(med - t))


"""
作者：lcbin
链接：https://leetcode.cn/problems/maximum-score-from-removing-stones/solution/by-lcbin-01wp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

每次贪心地从最大的两堆石子中取石头，直到至少有两堆石子为空。
时间复杂度 O(n)，其中 n 为石子总数。
"""


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        s = sorted([a, b, c])
        ans = 0
        while s[1]:
            ans += 1
            s[1] -= 1
            s[2] -= 1
            s.sort()
        return ans


"""
我们不妨设 a ≤ b ≤ c，那么：

- 当 a + b ≤ c 时，我们可以先从 a, c 两堆中取石头，得到分数 a；再从 b, c 两堆中
取石头，得到分数 b，总分数为 a + b；

- 当 a + b >c 时，这时我们每次会从 c 以及 a 和 b 中较大的那一堆中取石头，最终将
c 取空。此时 a 和 b 的大小差最多为 1。我们再从 a, b 两堆中取石头，直到不能取为止，
总分数为 floor((a + b + c) / 2)

时间复杂度 O(1)。
"""


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if a + b < c:
            return a + b
        return (a + b + c) >> 1


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
