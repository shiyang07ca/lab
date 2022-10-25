"""

[934] Shortest Bridge


You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.


Example 1:


Input: grid = [[0,1],[1,0]]
Output: 1


Example 2:


Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2


Example 3:


Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1



Constraints:


	n == grid.length == grid[i].length
	2 <= n <= 100
	grid[i][j] is either 0 or 1.
	There are exactly two islands in grid.

################################################################

934. 最短的桥
给你一个大小为 n x n 的二元矩阵 grid ，其中 1 表示陆地，0 表示水域。

岛 是由四面相连的 1 形成的一个最大组，即不会与非组内的任何其他 1 相连。grid 中 恰好存在两座岛 。

你可以将任意数量的 0 变为 1 ，以使两座岛连接起来，变成 一座岛 。

返回必须翻转的 0 的最小数目。



示例 1：

输入：grid = [[0,1],[1,0]]
输出：1


示例 2：

输入：grid = [[0,1,0],[0,0,0],[0,0,1]]
输出：2


示例 3：

输入：grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1


提示：

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] 为 0 或 1
grid 中恰有两个岛

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import deque

from typing import *

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

先通过 DFS 将其中一个岛屿的所有点找出来，放到一个队列 q 中。然后通过 BFS 一层层向外扩展，直至碰到另一个岛屿，此时将当前扩展的层数作为答案返回即可。

在 DFS 和 BFS 搜索的过程中，我们直接将已经访问过的点标记为 2，这样就不会重复访问。

作者：lcbin
链接：https://leetcode.cn/problems/shortest-bridge/solution/by-lcbin-j4i6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            q.append((i, j))
            grid[i][j] = 2
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                    dfs(x, y)

        n = len(grid)
        dirs = (-1, 0, 1, 0, -1)
        q = deque()
        i, j = next((i, j) for i in range(n) for j in range(n) if grid[i][j])
        dfs(i, j)
        ans = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return ans
                        if grid[x][y] == 0:
                            grid[x][y] = 2
                            q.append((x, y))
            ans += 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        grid = [[0, 1], [1, 0]]
        self.assertEqual(
            self.sl.shortestBridge(grid),
            1,
        )

        grid = [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 1],
        ]
        self.assertEqual(
            self.sl.shortestBridge(grid),
            2,
        )

        grid = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
        self.assertEqual(
            self.sl.shortestBridge(grid),
            1,
        )


if __name__ == "__main__":
    unittest.main()
