"""

[809] Expressive Words


Sometimes people repeat letters to represent extra feeling. For example:


	"hello" -> "heeellooo"
	"hi" -> "hiiii"


In these strings like "heeellooo", we have groups of adjacent letters that are all the same: "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words. A query word is stretchy if it can be made to be equal to s by any number of applications of the following extension operation: choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is three or more.


	For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", but we cannot get "helloo" since the group "oo" has a size less than three. Also, we could do another extension like "ll" -> "lllll" to get "helllllooo". If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = s.


Return the number of query strings that are stretchy.


Example 1:


Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.


Example 2:


Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3



Constraints:


	1 <= s.length, words.length <= 100
	1 <= words[i].length <= 100
	s and words[i] consist of lowercase letters.

################################################################

809. 情感丰富的文字
有时候人们会用重复写一些字母来表示额外的感受，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将相邻字母都相同的一串字符定义为相同字母组，例如："h", "eee", "ll", "ooo"。

对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。扩张操作定义如下：选择一个字母组（包含字母 c ），然后往其中添加相同的字母 c 使其长度达到 3 或以上。

例如，以 "hello" 为例，我们可以对字母组 "o" 扩张得到 "hellooo"，但是无法以同样的方法得到 "helloo" 因为字母组 "oo" 长度小于 3。此外，我们可以进行另一种扩张 "ll" -> "lllll" 以获得 "helllllooo"。如果 S = "helllllooo"，那么查询词 "hello" 是可扩张的，因为可以对它执行这两种扩张操作使得 query = "hello" -> "hellooo" -> "helllllooo" = S。

输入一组查询单词，输出其中可扩张的单词数量。



示例：

输入：
S = "heeellooo"
words = ["hello", "hi", "helo"]
输出：1
解释：
我们能通过扩张 "hello" 的 "e" 和 "o" 来得到 "heeellooo"。
我们不能通过扩张 "helo" 来得到 "heeellooo" 因为 "ll" 的长度小于 3 。

提示：

0 <= len(S) <= 100。
0 <= len(words) <= 100。
0 <= len(words[i]) <= 100。
S 和所有在 words 中的单词都只由小写字母组成。

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


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        if not s:
            return 0

        def check(w):
            wcount = get_count(w)
            if len(wcount) != len(count):
                return False

            for i, wc in enumerate(wcount):
                sc = count[i]
                if wc[0] != sc[0]:
                    return False
                elif wc[1] != sc[1] and (sc[1] < 3 or wc[1] > sc[1]):
                    return False
            return True

        def get_count(s):
            if not s:
                return []
            count = [[s[0], 1]]
            for c in s[1:]:
                if count[-1][0] == c:
                    count[-1] = [c, count[-1][1] + 1]
                else:
                    count.append([c, 1])
            return count

        count = get_count(s)
        ans = 0
        for w in words:
            if check(w):
                ans += 1

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
