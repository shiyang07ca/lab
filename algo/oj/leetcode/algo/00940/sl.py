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

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)

from functools import lru_cache as cache

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/distinct-subsequences-ii/solution/xi-fen-wen-ti-fu-za-du-you-hua-pythonjav-1ihu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

定义 f[i][j] 表示用 s 的前 i 个字符组成以 j 结尾的不同非空子序列的个数，根据上述
思路，得
    f[i][s[i]] = 1 + f[i-1][j]   (j = [0, 25])
初始值f[0][s[0]] = 1, 答案为 f[n-1][j] (j = [0, 25])
"""


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        f = [[0] * 26 for _ in range(len(s) + 1)]
        for i, c in enumerate(s, 1):
            c = ord(c) - ord("a")
            f[i] = f[i - 1][:]
            f[i][c] = (1 + sum(f[i - 1])) % MOD

        return sum(f[-1]) % MOD


"""
由于状态转移只发生在 i 和 i−1 之间，因此可以只用一个长为 26 的数组表示上述状态转
移过程。由于除了 f[s[i]] 以外，其余值都不变，因此只需要更新 f[s[i]] 的值。
"""


class Solution1:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        f = [0] * 26
        for c in s:
            f[ord(c) - ord("a")] = (1 + sum(f)) % MOD
        return sum(f) % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.sl = Solution()
        self.sl = Solution1()

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
