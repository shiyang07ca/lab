"""

[481] Magical String


A magical string s consists of only '1' and '2' and obeys the following rules:


	The string s is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string s itself.


The first few elements of s is s = "1221121221221121122……". If we group the consecutive 1's and 2's in s, it will be "1 22 11 2 1 22 1 22 11 2 11 22 ......" and the occurrences of 1's or 2's in each group are "1 2 2 1 1 2 1 2 2 1 2 2 ......". You can see that the occurrence sequence is s itself.

Given an integer n, return the number of 1's in the first n number in the magical string s.


Example 1:


Input: n = 6
Output: 3
Explanation: The first 6 elements of magical string s is "122112" and it contains three 1's, so return 3.


Example 2:


Input: n = 1
Output: 1



Constraints:


	1 <= n <= 10⁵

################################################################


神奇字符串 s 仅由 '1' 和 '2' 组成，并需要遵守下面的规则：

神奇字符串 s 的神奇之处在于，串联字符串中 '1' 和 '2' 的连续出现次数可以生成该字符串。
s 的前几个元素是 s = "1221121221221121122……" 。如果将 s 中连续的若干 1 和 2 进行分组，可以得到 "1 22 11 2 1 22 1 22 11 2 11 22 ......" 。每组中 1 或者 2 的出现次数分别是 "1 2 2 1 1 2 1 2 2 1 2 2 ......" 。上面的出现次数正是 s 自身。

给你一个整数 n ，返回在神奇字符串 s 的前 n 个数字中 1 的数目。



示例 1：

输入：n = 6
输出：3
解释：神奇字符串 s 的前 6 个元素是 “122112”，它包含三个 1，因此返回 3 。
示例 2：

输入：n = 1
输出：1


提示：

1 <= n <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/magical-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *

from typing import *

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

class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i = 2
        while len(s) < n:
            s += [s[-1] ^ 3] * s[i]  # 1^3=2, 2^3=1，这样就能在 1 和 2 之间转换
            i += 1
        return s[:n].count(1)

作者：endlesscheng
链接：https://leetcode.cn/problems/magical-string/solution/by-endlesscheng-z8o1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def magicalString(self, n: int) -> int:
        if n in (1, 2, 3):
            return 1

        s = [1, 2, 2]
        ans = 1
        i, j = 2, 2
        next_n = 1
        while j < n - 1:
            s.extend([next_n] * s[i])
            j += s[i]
            i += 1
            if next_n == 1:
                next_n = 2
            else:
                next_n = 1
        return s[:n].count(1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl.magicalString(6),
            3,
        )
        self.assertEqual(
            self.sl.magicalString(10),
            5,
        )
        self.assertEqual(
            self.sl.magicalString(5),
            3,
        )
        self.assertEqual(
            self.sl.magicalString(1),
            1,
        )


if __name__ == "__main__":
    unittest.main()
