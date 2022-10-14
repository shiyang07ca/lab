"""

# TODO
# tag: dp

940. 不同的子序列 II

给定一个字符串 s，计算 s 的 不同非空子序列 的个数。因为结果可能很大，所以返回答案需要对 10^9 + 7 取余 。

字符串的 子序列 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。

例如，"ace" 是 "abcde" 的一个子序列，但 "aec" 不是。

示例 1：

输入：s = "abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。

示例 2：

输入：s = "aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。


示例 3：

输入：s = "aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。


提示：

1 <= s.length <= 2000
s 仅由小写英文字母组成


"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)

from algo.tree.builder import *

from functools import lru_cache as cache


class Solution:

    def distinctSubseqII(self, s: str) -> int:
        t = set()
        # t = []

        @cache(maxsize=1000000000)
        def search(i, last_i, last):
            if i == last_i:
                t.add(last)
                return

            cur = s[i] + last
            # print(f"{pre}, {s[i]}")
            # if cur not in t:
            #     t.add(cur)
            #     search(i + 1, cur)
            # t.remove(cur)

            t.add(cur)
            search(i + 1, last_i, cur)
            search(i + 1, last_i, last)

        for i in range(len(s)):
            search(0, i, s[i])

        # print(t)
        return len(t) % (10**9 + 7)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = "abc"
        self.assertEqual(
            self.sl.distinctSubseqII(s),
            7,
        )

        s = "aba"
        self.assertEqual(
            self.sl.distinctSubseqII(s),
            6,
        )

        s = "aaa"
        self.assertEqual(
            self.sl.distinctSubseqII(s),
            3,
        )

        # s = "pcrdhwdxmqdznbenhwjs"
        # print(self.sl.distinctSubseqII(s))

        s = "pcrdhwdxmqdznbenhwjsenjhvulyve"
        print(self.sl.distinctSubseqII(s))


if __name__ == "__main__":
    unittest.main()
