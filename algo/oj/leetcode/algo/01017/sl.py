"""

[1017] Convert to Base -2


Given an integer n, return a binary string representing its representation in base -2.

* * * * * * * * * * * * * * * * * * * * * * * * *

Note that the returned string should not have leading zeros unless the string is "0".


Example 1:


Input: n = 2
Output: "110"
Explantion: (-2)² + (-2)¹ = 2


Example 2:


Input: n = 3
Output: "111"
Explantion: (-2)² + (-2)¹ + (-2)⁰ = 3


Example 3:


Input: n = 4
Output: "100"
Explantion: (-2)² = 4



Constraints:
   0 <= n <= 10⁹


################################################################

1017. 负二进制转换

给你一个整数 n ，以二进制字符串的形式返回该整数的 负二进制（base -2）表示。

注意，除非字符串就是 "0"，否则返回的字符串中不能含有前导零。

示例 1：

输入：n = 2
输出："110"
解释：(-2)2 + (-2)1 = 2

示例 2：

输入：n = 3
输出："111"
解释：(-2)2 + (-2)1 + (-2)0 = 3

示例 3：

输入：n = 4
输出："100"
解释：(-2)2 = 4


提示：

0 <= n <= 109

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


# https://leetcode.cn/problems/convert-to-base-2/solutions/2210967/duan-chu-fa-pythonyi-xing-jin-shuang-bai-ch27/
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        if n == 1:
            return "1"
        if n & 1:
            return self.baseNeg2((n - 1) // -2) + "1"
        else:
            return self.baseNeg2(n // -2) + "0"


# 作者：ylb
# 链接：https://leetcode.cn/problems/convert-to-base-2/solutions/2210964/python3javacgotypescript-yi-ti-yi-jie-mo-5edi/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def baseNeg2(self, n: int) -> str:
        k = 1
        ans = []
        while n:
            if n % 2:
                ans.append("1")
                n -= k
            else:
                ans.append("0")
            n //= 2
            k *= -1
        return "".join(ans[::-1]) or "0"


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
