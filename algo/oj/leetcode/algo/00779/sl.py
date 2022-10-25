"""

779. 第K个语法符号
我们构建了一个包含 n 行( 索引从 1  开始 )的表。首先在第一行我们写上一个 0。接下来的每一行，将前一行中的0替换为01，1替换为10。

例如，对于 n = 3 ，第 1 行是 0 ，第 2 行是 01 ，第3行是 0110 。
给定行数 n 和序数 k，返回第 n 行中第 k 个字符。（ k 从索引 1 开始）


示例 1:

输入: n = 1, k = 1
输出: 0
解释: 第一行：0


示例 2:

输入: n = 2, k = 1
输出: 0
解释:
第一行: 0
第二行: 01


示例 3:

输入: n = 2, k = 2
输出: 1
解释:
第一行: 0
第二行: 01


提示:

1 <= n <= 30
1 <= k <= 2n - 1




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


from algo.tree.builder import *

from math import log, floor


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        if self.kthGrammar(n - 1, (k + 1) // 2) == 0:
            return [1, 0][k % 2]
        else:
            return [0, 1][k % 2]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
                0
            0          1
         0    1      1      0
        0 1  1 0    1 0    0 1

        """
        n = 3
        k = 3
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            1,
        )

        n = 1
        k = 1
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            0,
        )

        n = 2
        k = 1
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            0,
        )

        n = 2
        k = 2
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            1,
        )

        n = 4
        k = 3
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            1,
        )

        n = 4
        k = 4
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            0,
        )

        n = 4
        k = 5
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            1,
        )

        n = 4
        k = 6
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            0,
        )

        n = 4
        k = 7
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            0,
        )

        n = 4
        k = 1
        self.assertEqual(
            self.sl.kthGrammar(n, k),
            0,
        )


if __name__ == "__main__":
    unittest.main()
