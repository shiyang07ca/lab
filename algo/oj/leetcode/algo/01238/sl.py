"""

[1238] Circular Permutation in Binary Representation


Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :


	p[0] = start
	p[i] and p[i+1] differ by only one bit in their binary representation.
	p[0] and p[2^n -1] must also differ by only one bit in their binary representation.



Example 1:


Input: n = 2, start = 3
Output: [3,2,0,1]
Explanation: The binary representation of the permutation is (11,10,00,01).
All the adjacent element differ by one bit. Another valid permutation is [3,1,0,2]


Example 2:


Input: n = 3, start = 2
Output: [2,6,7,5,4,0,1,3]
Explanation: The binary representation of the permutation is (010,110,111,101,100,000,001,011).



Constraints:


	1 <= n <= 16
	0 <= start < 2 ^ n

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

# 作者：lcbin
# 链接：https://leetcode.cn/problems/circular-permutation-in-binary-representation/solution/python3javacgotypescript-yi-ti-shuang-ji-zhm7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 方法一：二进制码转格雷码


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        g = [i ^ (i >> 1) for i in range(1 << n)]
        j = g.index(start)
        return g[j:] + g[:j]


# 方法二：转换优化


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [i ^ (i >> 1) ^ start for i in range(1 << n)]


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
