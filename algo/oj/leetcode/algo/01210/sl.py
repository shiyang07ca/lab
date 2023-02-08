"""

[1210] Minimum Moves to Reach Target with Rotations


In an n*n grid, there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1). The grid has empty cells represented by zeros and blocked cells represented by ones. The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:


	Move one cell to the right if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
	Move down one cell if there are no blocked cells there. This move keeps the horizontal/vertical position of the snake as it is.
	Rotate clockwise if it's in a horizontal position and the two cells under it are both empty. In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).

	Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty. In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).



Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.


Example 1:




Input: grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
Output: 11
Explanation:
One possible solution is [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].


Example 2:


Input: grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
Output: 9



Constraints:


	2 <= n <= 100
	0 <= grid[i][j] <= 1
	It is guaranteed that the snake starts at empty cells.

################################################################

# TODO
# tag: BFS

1210. 穿过迷宫的最少移动次数

你还记得那条风靡全球的贪吃蛇吗？

我们在一个 n*n 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（(0, 0) 和 (0, 1)）开始移动。我们用 0 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（(n-1, n-2) 和 (n-1, n-1)）。

每次移动，蛇可以这样走：

如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（(r, c)、(r, c+1)）移动到 （(r, c)、(r+1, c)）。

如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（(r, c)、(r+1, c)）移动到（(r, c)、(r, c+1)）。

返回蛇抵达目的地所需的最少移动次数。

如果无法到达目的地，请返回 -1。

示例 1：

输入：grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
输出：11
解释：
一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。


示例 2：

输入：grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
输出：9


提示：

2 <= n <= 100
0 <= grid[i][j] <= 1
蛇保证从空单元格开始出发。


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

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/solution/huan-zai-if-elseyi-ge-xun-huan-chu-li-li-tw8b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def minimumMoves(self, g: List[List[int]]) -> int:
        step, n = 1, len(g)
        vis = {(0, 0, 0)}
        q = [(0, 0, 0)]  # 初始位置
        while q:
            tmp = q
            q = []
            for X, Y, S in tmp:
                for t in (X + 1, Y, S), (X, Y + 1, S), (X, Y, S ^ 1):  # 直接把移动后的位置算出来
                    x, y, s = t  # 移动后的蛇尾
                    x2, y2 = x + s, y + (s ^ 1)  # 移动后的蛇头
                    if (
                        x2 < n
                        and y2 < n
                        and t not in vis
                        and g[x][y] == 0
                        and g[x2][y2] == 0
                        and (s == S or g[x + 1][y + 1] == 0)
                    ):
                        if x == n - 1 and y == n - 2:  # 此时蛇头一定在 (n-1, n-1)
                            return step
                        vis.add(t)
                        q.append(t)
            step += 1
        return -1


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
