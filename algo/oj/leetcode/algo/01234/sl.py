"""

[1234] Replace the Substring for Balanced String


You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.


Example 1:


Input: s = "QWER"
Output: 0
Explanation: s is already balanced.


Example 2:


Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.


Example 3:


Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER".



Constraints:


	n == s.length
	4 <= n <= 10⁵
	n is a multiple of 4.
	s contains only 'Q', 'W', 'E', and 'R'.

################################################################

# TODO

# tag: two pointer; sliding window; 双指针; 同向双指针; 滑动窗口;


1234. 替换子串得到平衡字符串

有一个只含有 'Q', 'W', 'E', 'R' 四种字符，且长度为 n 的字符串。

假如在该字符串中，这四个字符都恰好出现 n/4 次，那么它就是一个「平衡字符串」。



给你一个这样的字符串 s，请通过「替换一个子串」的方式，使原字符串 s 变成一个「平衡字符串」。

你可以用和「待替换子串」长度相同的 任何 其他字符串来完成替换。

请返回待替换子串的最小可能长度。

如果原字符串自身就是一个平衡字符串，则返回 0。



示例 1：

输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。
示例 2：

输入：s = "QQWE"
输出：1
解释：我们需要把一个 'Q' 替换成 'R'，这样得到的 "RQWE" (或 "QRWE") 是平衡的。
示例 3：

输入：s = "QQQW"
输出：2
解释：我们可以把前面的 "QQ" 替换成 "ER"。
示例 4：

输入：s = "QQQQ"
输出：3
解释：我们可以替换后 3 个 'Q'，使 s = "QWER"。


提示：

1 <= s.length <= 10^5
s.length 是 4 的倍数
s 中只含有 'Q', 'W', 'E', 'R' 四种字符


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
作者：endlesscheng
链接：https://leetcode.cn/problems/replace-the-substring-for-balanced-string/solution/tong-xiang-shuang-zhi-zhen-hua-dong-chua-z7tu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


根据题意，如果在待替换子串之外的任意字符的出现次数都超过 m= n / 4 ，那么无论怎么
替换，都无法使这个字符的出现次数等于 m。

反过来说，如果在待替换子串之外的任意字符的出现次数都不超过m，那么可以通过替换，
使 s 为平衡字符串，即每个字符的出现次数均为 m。

这可以用同向双指针（长度不固定的滑动窗口）实现，对于本题，设子串的左右端点为
left 和 right，枚举 right，如果子串外的任意字符的出现次数都不超过 m，则说明从
left 到 right 的这段子串可以是待替换子串，用其长度 right − left + 1 更新答案的最
小值，并向右移动 left，缩小子串长度。



相似题目

LC3. 无重复字符的最长子串 https://leetcode.cn/problems/longest-substring-without-repeating-characters/

LC209. 长度最小的子数组 https://leetcode.cn/problems/minimum-size-subarray-sum/

LC713. 乘积小于 K 的子数组 https://leetcode.cn/problems/subarray-product-less-than-k/


"""


class Solution:
    def balancedString(self, s: str) -> int:
        cnt, m = Counter(s), len(s) // 4
        if all(cnt[x] == m for x in "QWER"):  # 已经符合要求啦
            return 0
        ans, left = inf, 0
        for right, c in enumerate(s):  # 枚举子串右端点
            cnt[c] -= 1
            while all(cnt[x] <= m for x in "QWER"):
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1  # 缩小子串
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
