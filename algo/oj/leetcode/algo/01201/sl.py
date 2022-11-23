"""

[1201] Ugly Number III


An ugly number is a positive integer that is divisible by a, b, or c.

Given four integers n, a, b, and c, return the nth ugly number.


Example 1:


Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.


Example 2:


Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.


Example 3:


Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.



Constraints:


	1 <= n, a, b, c <= 10⁹
	1 <= a * b * c <= 10¹⁸
	It is guaranteed that the result will be in range [1, 2 * 10⁹].

################################################################


1201. 丑数 III
给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。

丑数是可以被 a 或 b 或 c 整除的 正整数 。



示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。


示例 2：

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。


示例 3：

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。


示例 4：

输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984


提示：

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
本题结果在 [1, 2 * 10^9] 的范围内

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
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        m1 = lcm(a, b)
        m2 = lcm(b, c)
        m3 = lcm(a, c)
        m4 = lcm(a, b, c)

        def check():
            return (
                mid // a
                + mid // b
                + mid // c
                - mid // m1
                - mid // m2
                - mid // m3
                + mid // m4
            ) >= n

        l, r = min(a, b, c), min(a, b, c) * n
        while l < r:
            mid = (l + r) >> 1
            if check():
                r = mid
            else:
                l = mid + 1
        return l


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = """25
2
4
7
5
2
3
3
3
2
3
5
4
2
3
4
5
2
11
13"""

        ans = """44
8
4
6
10"""
        s = list(map(int, s.split("\n")))
        ans = list(map(int, ans.split("\n")))
        for i in range(0, len(s), 4):
            n, a, b, c = s[i : i + 4]
            print(n, a, b, c)

            self.assertEqual(
                self.sl.nthUglyNumber(n, a, b, c),
                ans[i // 4],
            )


if __name__ == "__main__":
    unittest.main()
