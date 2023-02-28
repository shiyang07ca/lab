"""

[767] Reorganize String


Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.


Example 1:
Input: s = "aab"
Output: "aba"
Example 2:
Input: s = "aaab"
Output: ""


Constraints:


	1 <= s.length <= 500
	s consists of lowercase English letters.

################################################################

# tag: greedy, heap

767. 重构字符串

给定一个字符串 s ，检查是否能重新排布其中的字母，使得两相邻的字符不同。

返回 s 的任意可能的重新排列。若不可行，返回空字符串 "" 。



示例 1:

输入: s = "aab"
输出: "aba"


示例 2:

输入: s = "aaab"
输出: ""


提示:

1 <= s.length <= 500
s 只包含小写字母

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

from heapq import *


class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        h = []
        for c, v in cnt.items():
            heappush(h, (-v, c))

        ans = []
        while True:
            v1, c1 = heappop(h)
            v1 = -v1
            if not h and v1 >= 2:
                return ""
            elif not h:
                ans.append(c1)
                return "".join(ans)

            v2, c2 = heappop(h)
            v2 = -v2
            ans.append(c1)
            ans.append(c2)
            if v2 - 1 > 0:
                heappush(h, (-v2 + 1, c2))
            if v1 - 1 > 0:
                heappush(h, (-v1 + 1, c1))
            if not h:
                return "".join(ans)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = "aab"
        self.assertEqual(
            self.sl.reorganizeString(s),
            "aba",
        )

        s = "aaab"
        self.assertEqual(
            self.sl.reorganizeString(s),
            "",
        )

        s = "aaabc"
        self.assertEqual(
            self.sl.reorganizeString(s),
            "abaca",
        )

        s = "aaabcd"
        self.assertEqual(
            self.sl.reorganizeString(s),
            "abacad",
        )


if __name__ == "__main__":
    unittest.main()
