"""

[754] Reach a Number


You are standing at position 0 on an infinite number line. There is a destination at position target.

You can make some number of moves numMoves so that:


	On each move, you can either go left or right.
	During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.


Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.


Example 1:


Input: target = 2
Output: 3
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to -1 (2 steps).
On the 3rd move, we step from -1 to 2 (3 steps).


Example 2:


Input: target = 3
Output: 2
Explanation:
On the 1st move, we step from 0 to 1 (1 step).
On the 2nd move, we step from 1 to 3 (2 steps).



Constraints:


	-10⁹ <= target <= 10⁹
	target != 0

################################################################

# TODO
# tag:

754. 到达终点数字
在一根无限长的数轴上，你站在0的位置。终点在target的位置。

你可以做一些数量的移动 numMoves :

每次你可以选择向左或向右移动。
第 i 次移动（从  i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。
给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。



示例 1:

输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。


示例 2:

输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。


提示:

 -10^9 <= target <= 10^9
 target != 0

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *

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


作者：endlesscheng
链接：https://leetcode.cn/problems/reach-a-number/solution/fen-lei-tao-lun-xiang-xi-zheng-ming-jian-sqj2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        s = n = 0
        while s < target or (s - target) % 2:  # 没有到达（越过）终点，或者相距奇数
            n += 1
            s += n
        return n


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
