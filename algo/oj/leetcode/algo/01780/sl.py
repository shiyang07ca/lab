"""

[1780] Check if Number is a Sum of Powers of Three


Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.


Example 1:


Input: n = 12
Output: true
Explanation: 12 = 3¹ + 3²


Example 2:


Input: n = 91
Output: true
Explanation: 91 = 3⁰ + 3² + 3⁴


Example 3:


Input: n = 21
Output: false



Constraints:


	1 <= n <= 10⁷

################################################################

1780. 判断一个数字是否可以表示成三的幂的和

给你一个整数 n ，如果你可以将 n 表示成若干个不同的三的幂之和，请你返回 true ，否则请返回 false 。

对于一个整数 y ，如果存在整数 x 满足 y == 3x ，我们称这个整数 y 是三的幂。



示例 1：

输入：n = 12
输出：true
解释：12 = 31 + 32


示例 2：

输入：n = 91
输出：true
解释：91 = 30 + 32 + 34


示例 3：

输入：n = 21
输出：false


提示：

1 <= n <= 107

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
    def checkPowersOfThree(self, n: int) -> bool:
        i = 16
        while i >= 0:
            if 3**i <= n:
                n -= 3**i
                if n == 0:
                    return True

            i -= 1

        return False


"""

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/check-if-number-is-a-sum-of-powers-of-three/solution/pan-duan-yi-ge-shu-zi-shi-fou-ke-yi-biao-0j5k/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

我们可以将 n 转换成 3 进制。如果 n 的 3 进制表示中每一位均不为 2，那么答案为
True，否则为 False。

例如当 n=12 时，12=(110)3，满足要求；当 n=21 时，21 = (210)3 ，不满足要求。

"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n //= 3
        return True


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
