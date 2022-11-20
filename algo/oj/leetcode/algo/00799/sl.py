"""

[799] Champagne Tower


We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  (A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full.  After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.



Now after pouring some non-negative integer cups of champagne, return how full the jth glass in the ith row is (both i and j are 0-indexed.)


Example 1:


Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
Explanation: We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.


Example 2:


Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
Explanation: We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.


Example 3:


Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000



Constraints:


	0 <= poured <= 10⁹
	0 <= query_glass <= query_row < 100

################################################################

# TODO
# tag: dp


799. 香槟塔
我们把玻璃杯摆成金字塔的形状，其中 第一层 有 1 个玻璃杯， 第二层 有 2 个，依次类
推到第 100 层，每个玻璃杯 (250ml) 将盛有香槟。


从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等
流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左右两边
的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）


例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯
各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。
在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之
一的香槟，如下图所示。


现在当倾倒了非负整数杯香槟后，返回第 i 行 j 个玻璃杯所盛放的香槟占玻璃杯容积的比
例（ i 和 j 都从0开始）。


示例 1:
输入: poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
输出: 0.00000
解释: 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。



示例 2:
输入: poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
输出: 0.50000
解释: 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟。

示例 3:

输入: poured = 100000009, query_row = 33, query_glass = 17
输出: 1.00000


提示:

0 <= poured <= 109
0 <= query_glass <= query_row < 100


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


"""

作者：lcbin
链接：https://leetcode.cn/problems/champagne-tower/solution/by-lcbin-9en4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


我们直接模拟倒香槟的过程。

定义一个二维数组 f，其中 f[i][j] 表示第 i 层第 j 个玻璃杯中的香槟量。初始时 f[0][0] = pouredf。
对于每一层，如果当前杯子的香槟量 f[i][j] 大于 1，香槟会流向下一层的两个杯子，流入的量为 ( f[i][j]−1 ) / 2
，即当前杯子的香槟量减去 11 后除以 22，然后当前杯子的香槟量更新为 11。
模拟结束，返回 f[query_row][query_glass] 即可。

"""


class Solution:
    def champagneTower(self, p: int, row: int, col: int) -> float:
        f = [[0] * 101 for _ in range(101)]
        f[0][0] = p
        for i in range(row + 1):
            for j in range(i + 1):
                if f[i][j] > 1:
                    half = (f[i][j] - 1) / 2
                    f[i][j] = 1
                    f[i + 1][j] += half
                    f[i + 1][j + 1] += half
        return f[row][col]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        p = 1
        r = 1
        c = 1
        self.assertEqual(
            self.sl.champagneTower(p, r, c),
            0.00000,
        )

        p = 2
        r = 1
        c = 1
        self.assertEqual(
            self.sl.champagneTower(p, r, c),
            0.50000,
        )

        p = 100000009
        r = 33
        c = 17
        self.assertEqual(
            self.sl.champagneTower(p, r, c),
            1.00000,
        )


if __name__ == "__main__":
    unittest.main()
