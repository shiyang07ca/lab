"""

[1663] Smallest String With A Given Numeric Value


The numeric value of a lowercase character is defined as its position (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric value of b is 2, the numeric value of c is 3, and so on.

The numeric value of a string consisting of lowercase characters is defined as the sum of its characters' numeric values. For example, the numeric value of the string "abe" is equal to 1 + 2 + 5 = 8.

You are given two integers n and k. Return the lexicographically smallest string with length equal to n and numeric value equal to k.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.


Example 1:


Input: n = 3, k = 27
Output: "aay"
Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is the smallest string with such a value and length equal to 3.


Example 2:


Input: n = 5, k = 73
Output: "aaszz"



Constraints:


	1 <= n <= 10⁵
	n <= k <= 26 * n

################################################################

1663. 具有给定数值的最小字符串

小写字符 的 数值 是它在字母表中的位置（从 1 开始），因此 a 的数值为 1 ，b 的数值为 2 ，c 的数值为 3 ，以此类推。

字符串由若干小写字符组成，字符串的数值 为各字符的数值之和。例如，字符串 "abe" 的数值等于 1 + 2 + 5 = 8 。

给你两个整数 n 和 k 。返回 长度 等于 n 且 数值 等于 k 的 字典序最小 的字符串。

注意，如果字符串 x 在字典排序中位于 y 之前，就认为 x 字典序比 y 小，有以下两种情况：

x 是 y 的一个前缀；
如果 i 是 x[i] != y[i] 的第一个位置，且 x[i] 在字母表中的位置比 y[i] 靠前。


示例 1：

输入：n = 3, k = 27
输出："aay"
解释：字符串的数值为 1 + 1 + 25 = 27，它是数值满足要求且长度等于 3 字典序最小的字符串。
示例 2：

输入：n = 5, k = 73
输出："aaszz"


提示：

1 <= n <= 105
n <= k <= 26 * n


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
    def getSmallestString(self, n: int, k: int) -> str:
        if n < 1:
            return ""

        # ['a', 'b', ... 'z']
        char_arr = [chr(n) for n in range(ord("a"), ord("z") + 1)]
        ans = []
        for i in range(n):
            # 剩余位置全为 'z' 的和
            max_rest = (n - i - 1) * 26
            # 剩余目标小于所有位置都放 z 的情况
            if k <= max_rest:
                ans.append("a")
            else:
                ans.append(char_arr[k - max_rest - 1])
            k -= ord(ans[-1]) - ord("a") + 1

        return "".join(ans)


# 作者：zerotrac2
# 链接：https://leetcode.cn/problems/smallest-string-with-a-given-numeric-value/solution/ju-you-gei-ding-shu-zhi-de-zui-xiao-zi-fu-chuan-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = list()
        for rest in range(n, 0, -1):
            bound = k - 26 * (rest - 1)
            if bound > 0:
                ans.append(chr(bound + 96))
                k -= bound
            else:
                ans.append("a")
                k -= 1
        return "".join(ans)


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
