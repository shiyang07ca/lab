"""

[1147] Longest Chunked Palindrome Decomposition


You are given a string text. You should split it to k substrings (subtext₁, subtext₂, ..., subtextk) such that:


	subtexti is a non-empty string.
	The concatenation of all the substrings is equal to text (i.e., subtext₁ + subtext₂ + ... + subtextk == text).
	subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).


Return the largest possible value of k.


Example 1:


Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".


Example 2:


Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".


Example 3:


Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".



Constraints:


	1 <= text.length <= 1000
	text consists only of lowercase English characters.


################################################################

# TODO
# tag: greedy

1147. 段式回文

你会得到一个字符串 text 。你应该把它分成 k 个子字符串 (subtext1, subtext2，…， subtextk) ，要求满足:

subtexti 是 非空 字符串
所有子字符串的连接等于 text ( 即subtext1 + subtext2 + ... + subtextk == text )
对于所有 i 的有效值( 即 1 <= i <= k ) ，subtexti == subtextk - i + 1 均成立
返回k可能最大值。



示例 1：

输入：text = "ghiabcdefhelloadamhelloabcdefghi"
输出：7
解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。


示例 2：

输入：text = "merchant"
输出：1
解释：我们可以把字符串拆分成 "(merchant)"。


示例 3：

输入：text = "antaprezatepzapreanta"
输出：11
解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。


提示：

1 <= text.length <= 1000
text 仅由小写英文字符组成

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

"""
作者：灵茶山艾府
链接：https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/solutions/2221544/tu-jie-tan-xin-zuo-fa-yi-tu-miao-dong-py-huik/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# 递归写法
class Solution:
    def longestDecomposition(self, s: str) -> int:
        if s == "":
            return 0
        for i in range(1, len(s) // 2 + 1):  # 枚举前后缀长度
            if s[:i] == s[-i:]:  # 立刻分割
                return 2 + self.longestDecomposition(s[i:-i])
        return 1  # 无法分割


# 迭代写法
class Solution:
    def longestDecomposition(self, s: str) -> int:
        ans = 0
        while s:
            i = 1
            while i <= len(s) // 2 and s[:i] != s[-i:]:  # 枚举前后缀
                i += 1
            if i > len(s) // 2:  # 无法分割
                ans += 1
                break
            ans += 2  # 分割出 s[:i] 和 s[-i:]
            s = s[i:-i]
        return ans


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
