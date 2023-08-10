"""

[753] Cracking the Safe


There is a safe protected by a password. The password is a sequence of n digits where each digit can be in the range [0, k - 1].

The safe has a peculiar way of checking the password. When you enter in a sequence, it checks the most recent n digits that were entered each time you type a digit.


	For example, the correct password is "345" and you enter in "012345":


		After typing 0, the most recent 3 digits is "0", which is incorrect.
		After typing 1, the most recent 3 digits is "01", which is incorrect.
		After typing 2, the most recent 3 digits is "012", which is incorrect.
		After typing 3, the most recent 3 digits is "123", which is incorrect.
		After typing 4, the most recent 3 digits is "234", which is incorrect.
		After typing 5, the most recent 3 digits is "345", which is correct and the safe unlocks.




Return any string of minimum length that will unlock the safe at some point of entering it.


Example 1:


Input: n = 1, k = 2
Output: "10"
Explanation: The password is a single digit, so enter each digit. "01" would also unlock the safe.


Example 2:


Input: n = 2, k = 2
Output: "01100"
Explanation: For each possible password:
- "00" is typed in starting from the 4th digit.
- "01" is typed in starting from the 1st digit.
- "10" is typed in starting from the 3rd digit.
- "11" is typed in starting from the 2nd digit.
Thus "01100" will unlock the safe. "01100", "10011", and "11001" would also unlock the safe.



Constraints:


	1 <= n <= 4
	1 <= k <= 10
	1 <= kn <= 4096

################################################################

# TODO
# tag: DFS, Graph, Eulerian Circuit

753. 破解保险箱

有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。

你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。

举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.

请返回一个能打开保险箱的最短字符串。



示例1:

输入: n = 1, k = 2
输出: "01"
说明: "10"也可以打开保险箱。


示例2:

输入: n = 2, k = 2
输出: "00110"
说明: "01100", "10011", "11001" 也能打开保险箱。


提示：

n 的范围是 [1, 4]。
k 的范围是 [1, 10]。
k^n 最大可能为 4096。


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


# https://leetcode.cn/problems/cracking-the-safe/solution/po-jie-bao-xian-xiang-by-leetcode-solution/


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        ans = list()
        highest = 10 ** (n - 1)

        def dfs(node: int):
            for x in range(k):
                nei = node * 10 + x
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei % highest)
                    ans.append(str(x))

        dfs(0)
        return "".join(ans) + "0" * (n - 1)


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
