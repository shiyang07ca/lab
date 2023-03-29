"""

[1641] Count Sorted Vowel Strings


Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.


Example 1:


Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].


Example 2:


Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.


Example 3:


Input: n = 33
Output: 66045



Constraints:


	1 <= n <= 50

################################################################

# TODO

1641. 统计字典序元音字符串的数目

中等

亚马逊

给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。

字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。

示例 1：

输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]


示例 2：

输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后


示例 3：

输入：n = 33
输出：66045


提示：

1 <= n <= 50

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

作者：ylb
链接：https://leetcode.cn/problems/count-sorted-vowel-strings/solutions/2196576/python3javacgo-yi-ti-shuang-jie-ji-yi-hu-vh2j/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


我们设计一个函数 dfs(i,j)，表示当前已经选了 i 个元音字母，且最后一个元音字母是 j
的方案数。那么答案就是 dfs(0,0)。

函数 dfs(i,j) 的计算过程如下：

如果 i≥n，说明已经选了 n 个元音字母，返回 1。
否则，枚举 j 后面的元音字母，即 k∈[j,4]，并将 dfs(i+1,k) 的结果累加，即
dfs(i,j)=∑k=j~4 dfs(i+1,k)。

"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def dfs(i, j):
            return 1 if i >= n else sum(dfs(i + 1, k) for k in range(j, 5))

        return dfs(0, 0)


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
