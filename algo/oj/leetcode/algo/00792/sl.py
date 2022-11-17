"""

[792] Number of Matching Subsequences


Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.


	For example, "ace" is a subsequence of "abcde".



Example 1:


Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".


Example 2:


Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

################################################################

# TODO

792. 匹配子序列的单词数
给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。

字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，
而不改变其余字符的相对顺序。

例如， “ace” 是 “abcde” 的子序列。

示例 1:

输入: s = "abcde", words = ["a","bb","acd","ace"]
输出: 3
解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。

示例 2:

输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
输出: 2


提示:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
words[i]和 s 都只由小写字母组成。

Constraints:


	1 <= s.length <= 5 * 10⁴
	1 <= words.length <= 5000
	1 <= words[i].length <= 50
	s and words[i] consist of only lowercase English letters.

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
from bisect import *


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
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(deque)
        for w in words:
            d[w[0]].append(w)
        ans = 0
        for c in s:
            # print(d)
            for _ in range(len(d[c])):
                w = d[c].popleft()
                if len(w) == 1:
                    ans += 1
                else:
                    d[w[1]].append(w[1:])
        return ans


# 作者：lcbin
# 链接：https://leetcode.cn/problems/number-of-matching-subsequences/solution/by-lcbin-gwyj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution2:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(deque)
        for i, w in enumerate(words):
            d[w[0]].append((i, 0))
        ans = 0
        for c in s:
            for _ in range(len(d[c])):
                i, j = d[c].popleft()
                j += 1
                if j == len(words[i]):
                    ans += 1
                else:
                    d[words[i][j]].append((i, j))
        return ans


"""

方法二：二分查找

我们还可以先用数组或哈希表 d 存放字符串 s 每个字符的下标，即 d[c] 为 s 中所有字
符 c 的下标组成的数组。

然后我们遍历 words 中的每个单词 w，我们通过二分查找的方法，判断 w 是否为 s 的子序列，是则答案加
1。判断逻辑如下：

定义指针 i 表示当前指向字符串 s 的第 i 个字符，初始化为 −1。
遍历字符串 w 中的每个字符 c，在 d[c] 中二分查找第一个大于 i 的位置 j，如果不存在，
则说明 w 不是 s 的子序列，直接跳出循环；否则，将 i 更新为 d[c][j]，继续遍历下一
个字符。
如果遍历完 w 中的所有字符，说明 w 是 s 的子序列。

"""


class Solution2:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def check(w):
            i = -1
            for c in w:
                j = bisect_right(d[c], i)
                print(c, d[c], i, j)
                if j == len(d[c]):
                    return False
                i = d[c][j]
            return True

        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        return sum(check(w) for w in words)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution2()

    def test_sl(self):
        s = "abcde"
        words = ["a", "bb", "acd", "ace"]
        self.assertEqual(
            self.sl.numMatchingSubseq(s, words),
            3,
        )

        s = "dsahjpjauf"
        words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
        self.assertEqual(
            self.sl.numMatchingSubseq(s, words),
            2,
        )


if __name__ == "__main__":
    unittest.main()
