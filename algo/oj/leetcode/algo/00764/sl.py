"""

764. Largest Plus Sign
You are given an integer n. You have an n x n binary grid grid with all values
initially 1's except for some indices given in the array mines. The ith element
of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid.
If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1
along with four arms of length k - 1 going up, down, left, and right, and made
of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign,
only the relevant area of the plus sign is checked for 1's.


Example 1:

Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2.
One of them is shown.

Example 2:


Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.


Constraints:

1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
All the pairs (xi, yi) are unique.

################################################################

764. 最大加号标志
在一个 n x n 的矩阵 grid 中，除了在数组 mines 中给出的元素为 0，其他每个元素都为
1。mines[i] = [xi, yi]表示 grid[xi][yi] == 0

返回  grid 中包含 1 的最大的 轴对齐 加号标志的阶数 。如果未找到加号标志，则返回
0 。

一个 k 阶由 1 组成的 “轴对称”加号标志 具有中心网格 grid[r][c] == 1 ，以及4个从中
心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。注意，只有加号标志的所
有网格要求为 1 ，别的网格可能为 0 也可能为 1 。



示例 1：

输入: n = 5, mines = [[4, 2]]
输出: 2
解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。


示例 2：


输入: n = 1, mines = [[0, 0]]
输出: 0
解释: 没有加号标志，返回 0 。


提示：

1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
每一对 (xi, yi) 都 不重复

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *
from copy import *
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


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n = 5
        mines = [[4, 2]]
        self.assertEqual(
            self.sl.orderOfLargestPlusSign(n, mines),
            2,
        )

        n = 1
        mines = [[0, 0]]
        self.assertEqual(
            self.sl.orderOfLargestPlusSign(n, mines),
            0,
        )


if __name__ == "__main__":
    unittest.main()
