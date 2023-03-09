"""

# template

# TODO
# tag: two pointer

2379. 得到 K 个黑块的最少涂色次数

给你一个长度为 n 下标从 0 开始的字符串 blocks ，blocks[i] 要么是 'W' 要么是 'B' ，表示第 i 块的颜色。字符 'W' 和 'B' 分别表示白色和黑色。

给你一个整数 k ，表示想要 连续 黑色块的数目。

每一次操作中，你可以选择一个白色块将它 涂成 黑色块。

请你返回至少出现 一次 连续 k 个黑色块的 最少 操作次数。



示例 1：

输入：blocks = "WBBWWBBWBW", k = 7
输出：3
解释：
一种得到 7 个连续黑色块的方法是把第 0 ，3 和 4 个块涂成黑色。
得到 blocks = "BBBBBBBWBW" 。
可以证明无法用少于 3 次操作得到 7 个连续的黑块。
所以我们返回 3 。


示例 2：

输入：blocks = "WBWBBBW", k = 2
输出：0
解释：
不需要任何操作，因为已经有 2 个连续的黑块。
所以我们返回 0 。


提示：

n == blocks.length
1 <= n <= 100
blocks[i] 要么是 'W' ，要么是 'B' 。
1 <= k <= n

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

https://leetcode.cn/problems/minimum-recolors-to-get-k-consecutive-black-blocks/solution/python3javacgotypescript-yi-ti-yi-jie-hu-dmdz/

目实际上求的是一个 k 大小的滑动窗口中白色块的最小数量。

因此，我们只需要遍历字符串 blocks，用一个变量 cnt 统计当前窗口中白色块的数量，然
后用一个变量 ans 维护最小值即可。


遍历结束后即可得到答案。

"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = cnt = blocks[:k].count("W")
        for i in range(k, len(blocks)):
            cnt += blocks[i] == "W"
            cnt -= blocks[i - k] == "W"
            ans = min(ans, cnt)
        return ans


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
