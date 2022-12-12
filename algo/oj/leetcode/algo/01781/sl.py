"""

[1781] Sum of Beauty of All Substrings


The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.


	For example, the beauty of "abaacc" is 3 - 1 = 2.


Given a string s, return the sum of beauty of all of its substrings.


Example 1:


Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

Example 2:


Input: s = "aabcbaa"
Output: 17



Constraints:


	1 <= s.length <= 500
	s consists of only lowercase English letters.

################################################################

1781. 所有子字符串美丽值之和
一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。

比方说，"abaacc" 的美丽值为 3 - 1 = 2 。
给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。



示例 1：

输入：s = "aabcb"
输出：5
解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。
示例 2：

输入：s = "aabcbaa"
输出：17


提示：

1 <= s.length <= 500
s 只包含小写英文字母。

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
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            cnt = defaultdict(int)
            cnt[s[i]] = 1
            for j in range(i + 1, len(s)):
                cnt[s[j]] += 1
                vs = cnt.values()
                ans += max(vs) - min(vs)
            # print(cnt)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = "aabcb"
        self.assertEqual(
            self.sl.beautySum(s),
            5,
        )
        s = "aabcbaa"
        self.assertEqual(
            self.sl.beautySum(s),
            17,
        )


if __name__ == "__main__":
    unittest.main()
