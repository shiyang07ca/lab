"""

[1824] Minimum Sideway Jumps


There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.

You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.


	For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.


The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.


	For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.


Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

* * * * * * * * * * * * * * * * * * * * * * * * *

Note: There will be no obstacles on points 0 and n.


Example 1:


Input: obstacles = [0,1,2,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps (red arrows).
Note that the frog can jump over obstacles only when making side jumps (as shown at point 2).


Example 2:


Input: obstacles = [0,1,1,3,3,0]
Output: 0
Explanation: There are no obstacles on lane 2. No side jumps are required.


Example 3:


Input: obstacles = [0,2,1,0,3,0]
Output: 2
Explanation: The optimal solution is shown by the arrows above. There are 2 side jumps.



Constraints:


	obstacles.length == n + 1
	1 <= n <= 5 * 10⁵
	0 <= obstacles[i] <= 3
	obstacles[0] == obstacles[n] == 0

################################################################

https://leetcode.cn/problems/minimum-sideway-jumps/
1824. 最少侧跳次数

给你一个长度为 n 的 3 跑道道路 ，它总共包含 n + 1 个 点 ，编号为 0 到 n 。一只青蛙从 0 号点第二条跑道 出发 ，它想要跳到点 n 处。然而道路上可能有一些障碍。

给你一个长度为 n + 1 的数组 obstacles ，其中 obstacles[i] （取值范围从 0 到 3）表示在点 i 处的 obstacles[i] 跑道上有一个障碍。如果 obstacles[i] == 0 ，那么点 i 处没有障碍。任何一个点的三条跑道中 最多有一个 障碍。

比方说，如果 obstacles[2] == 1 ，那么说明在点 2 处跑道 1 有障碍。
这只青蛙从点 i 跳到点 i + 1 且跑道不变的前提是点 i + 1 的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在 同一个 点处 侧跳 到 另外一条 跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。

比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。
这只青蛙从点 0 处跑道 2 出发，并想到达点 n 处的 任一跑道 ，请你返回 最少侧跳次数 。

注意：点 0 处和点 n 处的任一跑道都不会有障碍。



示例 1：

输入：obstacles = [0,1,2,3,0]
输出：2
解释：最优方案如上图箭头所示。总共有 2 次侧跳（红色箭头）。
注意，这只青蛙只有当侧跳时才可以跳过障碍（如上图点 2 处所示）。


示例 2：

输入：obstacles = [0,1,1,3,3,0]
输出：0
解释：跑道 2 没有任何障碍，所以不需要任何侧跳。


示例 3：

输入：obstacles = [0,2,1,0,3,0]
输出：2
解释：最优方案如上图所示。总共有 2 次侧跳。


提示：

obstacles.length == n + 1
1 <= n <= 5 * 105
0 <= obstacles[i] <= 3
obstacles[0] == obstacles[n] == 0

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
    def minSideJumps(self, obstacles: List[int]) -> int:
        # f[i][j] 表示到达 pos i 上 j 跑道的最小测跳次数
        # 如果为 0 表示该位置没有石头
        # inf 表示有石头

        N = len(obstacles)
        f = [[1, 0, 1]] + [[0, 0, 0] for _ in range(N - 1)]

        for i in range(1, N - 1):
            o = obstacles[i]
            for j in range(3):
                if j == o - 1:
                    f[i][o - 1] = inf
                else:
                    f[i][j] = f[i - 1][j]

            mi = min(f[i][0], f[i][1], f[i][2])
            for j in range(3):
                if j != o - 1:
                    f[i][j] = min(f[i][j], mi + 1)

        return min(f[N - 2])


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        d = [1, 0, 1]
        for i in range(1, len(obstacles)):
            minCnt = inf
            for j in range(3):
                if j == obstacles[i] - 1:
                    d[j] = inf
                else:
                    minCnt = min(minCnt, d[j])
            for j in range(3):
                if j != obstacles[i] - 1:
                    d[j] = min(d[j], minCnt + 1)
        return min(d)


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
