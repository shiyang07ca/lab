"""

[474] Ones and Zeroes


You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.


Example 1:


Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.


Example 2:


Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.



Constraints:


	1 <= strs.length <= 600
	1 <= strs[i].length <= 100
	strs[i] consists only of digits '0' and '1'.
	1 <= m, n <= 100


################################################################


474. 一和零

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。



示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。


示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。


提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100

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


import unittest


class Solution:

    from functools import cache

    @cache
    def recur(self, m, n, strs, ans):
        if not strs:
            return ans

        c_0 = strs[0].count("0")
        c_1 = strs[0].count("1")
        if c_0 <= m and c_1 <= n:
            return max(
                self.recur(m, n, strs[1:], ans),
                self.recur(m - c_0, n - c_1, strs[1:], ans + 1),
            )
        else:
            return self.recur(m, n, strs[1:], ans)

    def dp(self, m, n, strs):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            c0 = s.count("0")
            c1 = s.count("1")
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i - c0][j - c1] + 1, dp[i][j])

        return dp[m][n]

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.recur(m, n, tuple(strs), 0)
        # return self.dp(m, n, strs)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = ["10", "0001", "111001", "1", "0"]
        m = 5
        n = 3
        ans = 4
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)

        s = ["10", "0", "1"]
        m = 1
        n = 1
        ans = 2
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)

        s = ["10", "0001", "111001", "1", "0"]
        m = 4
        n = 3
        ans = 3
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)

        s = ["111", "1000", "1000", "1000"]
        m = 9
        n = 3
        ans = 3
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)

        s = [
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
        ]
        m = 30
        n = 30
        ans = 47
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)


if __name__ == "__main__":
    unittest.main()
