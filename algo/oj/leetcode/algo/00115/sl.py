"""

[115] Distinct Subsequences


Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.


--------------------------------------------------

Example 1:


Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit


--------------------------------------------------

Example 2:


Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:


	1 <= s.length, t.length <= 1000
	s and t consist of English letters.


115. 不同的子序列
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。

字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。



示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。
babgbag
babgbag
babgbag
babgbag
babgbag


提示：

0 <= s.length, t.length <= 1000
s 和 t 由英文字母组成


"""

from copy import deepcopy


class Solution:
    def recur(self, s, t, i, strs=[]):
        pass

    from functools import cache

    # @cache
    def t1_r(self, s, t, i, res=""):
        if not t.startswith(res) or len(res) == len(t) or len(s) == i:
            self.all_res.append(res)
            return

        res_include = res[:]
        res_include += s[i]
        self.t1_r(s, t, i + 1, res_include)

        res_not_include = res[:]
        self.t1_r(s, t, i + 1, res_not_include)

    def numDistinct(self, s: str, t: str) -> int:
        # return self.recur(s, 0).count(t)

        ans = 0
        self.all_res = []
        self.t1_r(s, t, 0)
        for ss in self.all_res:
            # print(ss)
            if ss == t:
                # print(s, t, ss)
                ans += 1
        return ans


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = "rabbbit"
        t = "rabbit"
        self.assertEqual(self.sl.numDistinct(s, t), 3)

        s = "babgbag"
        t = "bag"
        self.assertEqual(self.sl.numDistinct(s, t), 5)

        s = "b"
        t = "a"
        self.assertEqual(self.sl.numDistinct(s, t), 0)

        s = "bccbcdcabadabddbccaddcbabbaaacdba"
        t = "bccbbdc"
        self.assertEqual(self.sl.numDistinct(s, t), 172)

        s = "dbaaadcddccdddcadacbadbadbabbbcad"
        t = "dadcccbaab"
        print(self.sl.numDistinct(s, t))

        # s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
        # t = "bddabdcae"
        # print(self.sl.numDistinct(s, t))


if __name__ == "__main__":
    unittest.main()
