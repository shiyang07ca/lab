"""

[22] Generate Parentheses


Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


--------------------------------------------------

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
--------------------------------------------------

Example 2:
Input: n = 1
Output: ["()"]


Constraints:


	1 <= n <= 8


################################################################

22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]


提示：

1 <= n <= 8

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *


class Solution:
    def process(self, pre, leftCount, n):

        if n == 0:
            self.ans.append(pre)
            return

        if leftCount == n:
            self.process(pre + ")", leftCount - 1, n - 1)
            return
        elif leftCount == 0:
            self.process(pre + "(", leftCount + 1, n)
            return

        self.process(pre + ")", leftCount - 1, n - 1)
        self.process(pre + "(", leftCount + 1, n)

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.process("(", 1, n)
        return self.ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            set(self.sl.generateParenthesis(3)),
            set(["((()))", "(()())", "(())()", "()(())", "()()()"]),
        )

    def test_sl2(self):
        self.assertEqual(
            set(self.sl.generateParenthesis(1)),
            set(["()"]),
        )


if __name__ == "__main__":
    unittest.main()
