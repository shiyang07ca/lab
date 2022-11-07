"""

[816] Ambiguous Coordinates


We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces and ended up with the string s.


	For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".


Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit occurring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.)


Example 1:


Input: s = "(123)"
Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]


Example 2:


Input: s = "(0123)"
Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
Explanation: 0.0, 00, 0001 or 00.01 are not allowed.


Example 3:


Input: s = "(00011)"
Output: ["(0, 0.011)","(0.001, 1)"]



Constraints:


	4 <= s.length <= 12
	s[0] == '(' and s[s.length - 1] == ')'.
	The rest of s are digits.

################################################################

816. 模糊坐标
我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表中。

原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。

最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。



示例 1:
输入: "(123)"
输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]


示例 2:
输入: "(00011)"
输出:  ["(0.001, 1)", "(0, 0.011)"]
解释:
0.0, 00, 0001 或 00.01 是不被允许的。


示例 3:
输入: "(0123)"
输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
示例 4:
输入: "(100)"
输出: [(10, 0)]
解释:
1.0 是不被允许的。


提示:

4 <= S.length <= 12.
S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。


"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *

from typing import *

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
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]

        def find(s):
            if len(s) == 1:
                return [s]

            ans = []
            if s[0] == "0":
                if s[-1] == "0":
                    return []
                else:
                    return [f"0.{s[1:]}"]
            elif s[-1] != "0":
                for i in range(len(s) - 1):
                    ans.append(f"{s[:i+1]}.{s[i+1:]}")
            ans.append(s)
            return ans

        ans = []
        for i in range(len(s) - 1):
            pre, suf = s[: i + 1], s[i + 1 :]
            pa, sa = find(pre), find(suf)
            if pa and sa:
                for pw in pa:
                    for sw in sa:
                        ans.append(f"({pw}, {sw})")
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = "(0010)"
        self.assertEqual(
            self.sl.ambiguousCoordinates(s),
            ["(0.01, 0)"],
        )

        s = "(00011)"
        self.assertEqual(
            self.sl.ambiguousCoordinates(s),
            ["(0, 0.011)", "(0.001, 1)"],
        )
        s = "(123)"
        self.assertEqual(
            self.sl.ambiguousCoordinates(s),
            ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"],
        )
        s = "(0123)"
        self.assertEqual(
            self.sl.ambiguousCoordinates(s),
            [
                "(0, 1.23)",
                "(0, 12.3)",
                "(0, 123)",
                "(0.1, 2.3)",
                "(0.1, 23)",
                "(0.12, 3)",
            ],
        )
        s = "(100)"
        self.assertEqual(
            self.sl.ambiguousCoordinates(s),
            ["(10, 0)"],
        )


if __name__ == "__main__":
    unittest.main()
