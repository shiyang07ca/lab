"""

[1759] Count Number of Homogenous Substrings


Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 10⁹ + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.


Example 1:


Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

Example 2:


Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".

Example 3:


Input: s = "zzzzz"
Output: 15



Constraints:


	1 <= s.length <= 10⁵
	s consists of lowercase letters.

################################################################

1759. 统计同构子字符串的数目

给你一个字符串 s ，返回 s 中 同构子字符串 的数目。由于答案可能很大，只需返回对 109 + 7 取余 后的结果。

同构字符串 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同构字符串。

子字符串 是字符串中的一个连续字符序列。



示例 1：

输入：s = "abbcccaa"
输出：13
解释：同构子字符串如下所列：
"a"   出现 3 次。
"aa"  出现 1 次。
"b"   出现 2 次。
"bb"  出现 1 次。
"c"   出现 3 次。
"cc"  出现 2 次。
"ccc" 出现 1 次。
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13


示例 2：

输入：s = "xy"
输出：2
解释：同构子字符串是 "x" 和 "y" 。


示例 3：

输入：s = "zzzzz"
输出：15


提示：

1 <= s.length <= 10^5
s 由小写字符串组成


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
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        # 1 + 2 + 3 + ... + i
        # (1 + i) * i // 2
        cnt = 1
        ans = 0
        for i, c in enumerate(s):
            if i + 1 == len(s) or c != s[i + 1]:
                ans += (1 + cnt) * cnt // 2
                cnt = 1
            else:
                cnt += 1
        return ans % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = "abbcccaa"
        self.assertEqual(
            self.sl.countHomogenous(s),
            13,
        )

        s = "xy"
        self.assertEqual(
            self.sl.countHomogenous(s),
            2,
        )

        s = "zzzzz"
        self.assertEqual(
            self.sl.countHomogenous(s),
            15,
        )


if __name__ == "__main__":
    unittest.main()
