"""

[1653] Minimum Deletions to Make String Balanced

################################################################

# TODO
# tag: dp

1653. 使字符串平衡的最少删除次数

给你一个字符串 s ，它仅包含字符 'a' 和 'b'。

你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是 平衡 的。

请你返回使 s 平衡 的 最少 删除次数。



示例 1：

输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。


示例 2：

输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。


提示：

1 <= s.length <= 105
s[i] 要么是 'a' 要么是 'b'​ 。

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
https://leetcode.cn/problems/minimum-deletions-to-make-string-balanced/solution/qian-hou-zhui-fen-jie-yi-zhang-tu-miao-d-dor2/


TODO

前后缀分解


LC42. 接雨水 https://leetcode.cn/problems/trapping-rain-water/
LC238. 除自身以外数组的乘积 https://leetcode.cn/problems/product-of-array-except-self/
LC2256. 最小平均差 https://leetcode.cn/problems/minimum-average-difference/
LC2483. 商店的最少代价 https://leetcode.cn/problems/minimum-penalty-for-a-shop/
LC2420. 找到所有好下标 https://leetcode.cn/problems/find-all-good-indices/
LC2167. 移除所有载有违禁货物车厢所需的最少时间 https://leetcode.cn/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
LC2484. 统计回文子序列数目 https://leetcode.cn/problems/count-palindromic-subsequences/
LC2552. 统计上升四元组 https://leetcode.cn/problems/count-increasing-quadruplets/
LC2565. 最少得分子序列 https://leetcode.cn/problems/subsequence-with-the-minimum-score/

"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        # 考虑 s 的最后一个字母
        # a =>
        # 保留 cnt_b[i]
        # 删除 f[i-1] + 1
        # b => ans = f[i-1]

        f = cb = 0
        for c in s:
            if c == "b":
                cb += 1
            else:
                f = min(cb, f + 1)
        return f


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
