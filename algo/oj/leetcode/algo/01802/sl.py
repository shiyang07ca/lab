"""

[1802] Maximum Value at a Given Index in a Bounded Array


You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:


	nums.length == n
	nums[i] is a positive integer where 0 <= i < n.
	abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
	The sum of all the elements of nums does not exceed maxSum.
	nums[index] is maximized.


Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.


Example 1:


Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].


Example 2:


Input: n = 6, index = 1,  maxSum = 10
Output: 3



Constraints:


	1 <= n <= maxSum <= 10⁹
	0 <= index < n

################################################################

# TODO
tag: bianry search

1802. 有界数组中指定下标处的最大值

给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。



示例 1：

输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
示例 2：

输入：n = 6, index = 1,  maxSum = 10
输出：3


提示：

1 <= n <= maxSum <= 109
0 <= index < n

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
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        #      nums[index-i]  index    nums[index+i]
        # 1 .... target-i ... target ... target-i .... 1

        def check(target):
            tot = 0
            r = n - index - 1
            if target <= index:
                tot += index - target + 1
                tot += (1 + target) * target // 2
            else:
                tot += (target - index + target) * (index + 1) // 2

            if r < target:
                tot += (target + target - r) * (r + 1) // 2
            else:
                tot += (1 + target) * target // 2
                tot += r - target + 1

            #             print(tot)
            return tot - target <= maxSum

        l, r = 1, maxSum
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1

        return l


# 作者：lcbin
# 链接：https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/solution/by-lcbin-4vp4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def sum(x, cnt):
            return (
                (x + x - cnt + 1) * cnt // 2 if x >= cnt else (x + 1) * x // 2 + cnt - x
            )

        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) >> 1
            if sum(mid - 1, index) + sum(mid, n - index) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n = 9
        i = 5
        m = 24
        self.assertEqual(
            self.sl.maxValue(n, i, m),
            4,
        )

        n = 4
        i = 0
        m = 6
        self.assertEqual(
            self.sl.maxValue(n, i, m),
            2,
        )

        n = 4
        i = 2
        m = 6
        self.assertEqual(
            self.sl.maxValue(n, i, m),
            2,
        )

        n = 6
        i = 1
        m = 10
        self.assertEqual(
            self.sl.maxValue(n, i, m),
            3,
        )


if __name__ == "__main__":
    unittest.main()
