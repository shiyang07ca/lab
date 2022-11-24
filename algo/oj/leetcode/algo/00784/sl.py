"""

[784] Letter Case Permutation


Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.


Example 1:


Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]


Example 2:


Input: s = "3z4"
Output: ["3z4","3Z4"]



Constraints:


	1 <= s.length <= 12
	s consists of lowercase English letters, uppercase English letters, and digits.

################################################################

# template
# TODO
# tag: DFS
# LC46

784. 字母大小写全排列

给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。

返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。


示例 1：

输入：s = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]


示例 2:

输入: s = "3z4"
输出: ["3z4","3Z4"]


提示:

1 <= s.length <= 12
s 由小写英文字母、大写英文字母和数字组成

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


from algo.tree.builder import *


class Solution:
    def letterCasePermutation(self, st: str) -> List[str]:
        ans = []

        def dfs(s, i):
            if i == len(s):
                ans.append("".join(deepcopy(s)))
                return

            # print(s[i])
            dfs(s, i + 1)
            if not s[i].isdigit():
                if s[i].isupper():
                    s[i] = s[i].lower()
                    dfs(s, i + 1)
                elif s[i].islower():
                    s[i] = s[i].upper()
                    dfs(s, i + 1)

        dfs(list(st), 0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = "a1b2"
        self.assertEqual(
            sorted(self.sl.letterCasePermutation(s)),
            sorted(["a1b2", "a1B2", "A1b2", "A1B2"]),
        )

        s = "3z4"
        self.assertEqual(
            sorted(self.sl.letterCasePermutation(s)),
            sorted(["3z4", "3Z4"]),
        )


if __name__ == "__main__":
    unittest.main()
