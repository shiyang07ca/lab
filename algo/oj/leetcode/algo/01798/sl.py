"""

[1798] Maximum Number of Consecutive Values You Can Make


You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. You can make some value x if you can choose some of your n coins such that their values sum up to x.

Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.

Note that you may have multiple coins of the same value.


Example 1:


Input: coins = [1,3]
Output: 2
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.

Example 2:


Input: coins = [1,1,1,4]
Output: 8
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.

Example 3:


Input: nums = [1,4,10,3,1]
Output: 20


Constraints:


	coins.length == n
	1 <= n <= 4 * 10⁴
	1 <= coins[i] <= 4 * 10⁴

################################################################

# TODO

1798. 你能构造出连续值的最大数目

给你一个长度为 n 的整数数组 coins ，它代表你拥有的 n 个硬币。第 i 个硬币的值为 coins[i] 。如果你从这些硬币中选出一部分硬币，它们的和为 x ，那么称，你可以 构造 出 x 。

请返回从 0 开始（包括 0 ），你最多能 构造 出多少个连续整数。

你可能有多个相同值的硬币。


示例 1：

输入：coins = [1,3]
输出：2
解释：你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
从 0 开始，你可以构造出 2 个连续整数。


示例 2：

输入：coins = [1,1,1,4]
输出：8
解释：你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
- 2：取 [1,1]
- 3：取 [1,1,1]
- 4：取 [4]
- 5：取 [4,1]
- 6：取 [4,1,1]
- 7：取 [4,1,1,1]
从 0 开始，你可以构造出 8 个连续整数。


示例 3：

输入：nums = [1,4,10,3,1]
输出：20


提示：

coins.length == n
1 <= n <= 4 * 104
1 <= coins[i] <= 4 * 104

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

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/maximum-number-of-consecutive-values-you-can-make/solution/mei-xiang-ming-bai-yi-zhang-tu-miao-dong-7xlx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        m = 0  # 一开始只能构造出 0
        coins.sort()
        for c in coins:
            if c > m + 1:  # coins 已排序，后面没有比 c 更小的数了
                break  # 无法构造出 m+1，继续循环没有意义
            m += c  # 可以构造出区间 [0,m+c] 中的所有整数
        return m + 1  # [0,m] 中一共有 m+1 个整数


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
