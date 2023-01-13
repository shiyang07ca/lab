"""

[17] Letter Combinations of a Phone Number


Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:


Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


Example 2:


Input: digits = ""
Output: []


Example 3:


Input: digits = "2"
Output: ["a","b","c"]



Constraints:


	0 <= digits.length <= 4
	digits[i] is a digit in the range ['2', '9'].

################################################################

17. 电话号码的字母组合

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。





示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]


示例 2：

输入：digits = ""
输出：[]


示例 3：

输入：digits = "2"
输出：["a","b","c"]


提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。

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


chr = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def dfs(i, cur):
            if i == len(digits):
                ans.append(cur)
                return

            for c in chr[int(digits[i])]:
                dfs(i + 1, cur + c)

        ans = []
        dfs(0, "")
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        digits = "23"
        self.assertEqual(
            self.sl.letterCombinations(digits),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )

        digits = ""
        self.assertEqual(
            self.sl.letterCombinations(digits),
            [],
        )

        digits = "2"
        self.assertEqual(
            self.sl.letterCombinations(digits),
            ["a", "b", "c"],
        )

        digits = "4563"

        self.assertEqual(
            self.sl.letterCombinations(digits),
            [
                "gjmd",
                "gjme",
                "gjmf",
                "gjnd",
                "gjne",
                "gjnf",
                "gjod",
                "gjoe",
                "gjof",
                "gkmd",
                "gkme",
                "gkmf",
                "gknd",
                "gkne",
                "gknf",
                "gkod",
                "gkoe",
                "gkof",
                "glmd",
                "glme",
                "glmf",
                "glnd",
                "glne",
                "glnf",
                "glod",
                "gloe",
                "glof",
                "hjmd",
                "hjme",
                "hjmf",
                "hjnd",
                "hjne",
                "hjnf",
                "hjod",
                "hjoe",
                "hjof",
                "hkmd",
                "hkme",
                "hkmf",
                "hknd",
                "hkne",
                "hknf",
                "hkod",
                "hkoe",
                "hkof",
                "hlmd",
                "hlme",
                "hlmf",
                "hlnd",
                "hlne",
                "hlnf",
                "hlod",
                "hloe",
                "hlof",
                "ijmd",
                "ijme",
                "ijmf",
                "ijnd",
                "ijne",
                "ijnf",
                "ijod",
                "ijoe",
                "ijof",
                "ikmd",
                "ikme",
                "ikmf",
                "iknd",
                "ikne",
                "iknf",
                "ikod",
                "ikoe",
                "ikof",
                "ilmd",
                "ilme",
                "ilmf",
                "ilnd",
                "ilne",
                "ilnf",
                "ilod",
                "iloe",
                "ilof",
            ],
        )


if __name__ == "__main__":
    unittest.main()
