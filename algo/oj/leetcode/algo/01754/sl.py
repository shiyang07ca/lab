"""

[1754] Largest Merge Of Two Strings


You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:


	If word1 is non-empty, append the first character in word1 to merge and delete it from word1.


		For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".


	If word2 is non-empty, append the first character in word2 to merge and delete it from word2.

		For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".




Return the lexicographically largest merge you can construct.

A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.


Example 1:


Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"
Explanation: One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.


Example 2:


Input: word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba"



Constraints:


	1 <= word1.length, word2.length <= 3000
	word1 and word2 consist only of lowercase English letters.

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
作者：lcbin
链接：https://leetcode.cn/problems/largest-merge-of-two-strings/solution/by-lcbin-t1mu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


贪心 + 双指针

我们用指针 i 和 j 分别指向字符串 word1 和 word2 的第一个字符。

然后循环，每次比较 word1[i:] 和 word2[j:] 的大小，如果 word1[i:] 比 word2[j:] 大，
那么我们就将 word1[i] 加入答案，否则我们就将 word2[j] 加入答案。循环，直至 i 到
达字符串 word1 的末尾，或者 j 到达字符串 word2 的末尾。

最后我们将剩余的字符串加入答案即可。

"""


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = j = 0
        ans = []
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
        ans.append(word1[i:])
        ans.append(word2[j:])
        return "".join(ans)


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
