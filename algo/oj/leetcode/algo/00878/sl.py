"""

[878] Nth Magical Number


A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 10⁹ + 7.


Example 1:


Input: n = 1, a = 2, b = 3
Output: 2


Example 2:


Input: n = 4, a = 2, b = 3
Output: 6



Constraints:


	1 <= n <= 10⁹
	2 <= a, b <= 4 * 10⁴

################################################################

# TODO
# tag: binary search


878. 第 N 个神奇数字
一个正整数如果能被 a 或 b 整除，那么它是神奇的。

给定三个整数 n , a , b ，返回第 n 个神奇的数字。因为答案可能很大，所以返回答案 对 109 + 7 取模 后的值。



示例 1：

输入：n = 1, a = 2, b = 3
输出：2
示例 2：

输入：n = 4, a = 2, b = 3
输出：6


提示：

 1 <= n <= 10^9
 2 <= a, b <= 4 * 10^4


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

from math import *

from algo.tree.builder import *


"""

作者：endlesscheng
链接：https://leetcode.cn/problems/nth-magical-number/solution/er-fen-da-an-rong-chi-yuan-li-by-endless-9j34/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


问：为什么二分循环结束时，得到的一定是一个神奇数字？

答：设答案为 x，循环结束时，≤x 的神奇数字有 n 个，而 ≤x−1 的神奇数字不足 n 个。
只有当 x 是一个神奇数字时，才会出现这种情况。

这也同时说明，在二分循环中，我们不能在计算结果恰好等于 n 的时候，直接返回答案，而是要继续二分。

问：最小公倍数是怎么算的？

答：利用最小公倍数与最大公约数的关系 lcm(a,b)=  a⋅b / gcd(a,b)。计算 gcd(a,b) 可
以用辗转相除法。


"""


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        m = lcm(a, b)
        l, r = min(a, b), min(a, b) * n
        while l < r:
            mid = (l + r) >> 1
            if (mid // a + mid // b - mid // m) >= n:
                r = mid
            else:
                l = mid + 1
        return l % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n = 1
        a = 2
        b = 3
        self.assertEqual(
            self.sl.nthMagicalNumber(n, a, b),
            2,
        )

        n = 4
        a = 2
        b = 3
        self.assertEqual(
            self.sl.nthMagicalNumber(n, a, b),
            6,
        )


if __name__ == "__main__":
    unittest.main()
