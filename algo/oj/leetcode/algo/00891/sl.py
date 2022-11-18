"""

[891] Sum of Subsequence Widths


The width of a sequence is the difference between the maximum and minimum elements in the sequence.

Given an array of integers nums, return the sum of the widths of all the non-empty subsequences of nums. Since the answer may be very large, return it modulo 10⁹ + 7.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


Example 1:


Input: nums = [2,1,3]
Output: 6
Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.


Example 2:


Input: nums = [2]
Output: 0



Constraints:


	1 <= nums.length <= 10⁵
	1 <= nums[i] <= 10⁵

################################################################

# TODO

891. 子序列宽度之和

一个序列的 宽度 定义为该序列中最大元素和最小元素的差值。

给你一个整数数组 nums ，返回 nums 的所有非空 子序列 的 宽度之和 。由于答案可能非常大，请返回对 10^9 + 7 取余 后的结果。

子序列 定义为从一个数组里删除一些（或者不删除）元素，但不改变剩下元素的顺序得到的数组。例如，[3,6,2,7] 就是数组 [0,3,1,6,2,2,7] 的一个子序列。



示例 1：

输入：nums = [2,1,3]
输出：6
解释：子序列为 [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3] 。
相应的宽度是 0, 0, 0, 1, 1, 2, 2 。
宽度之和是 6 。


示例 2：

输入：nums = [2]
输出：0


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105


"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *
from copy import *
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

作者：endlesscheng
链接：https://leetcode.cn/problems/sum-of-subsequence-widths/solution/by-endlesscheng-upd1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



子序列（不要求连续）
                     => 顺序不重要，排序
只关注最大、最小


从每个元素对答案的贡献角度考虑：

考虑每个元素成为最大，最小的情况
[1, 2, 3, 4, 5, 6]
已 4 为例，有多少子序列的最大值是 4 ？=> 比 4 小的选择或不选择，4必须选，比 4 大的不能选
因此子序列的个数：2 * 2 * 2 * 1 * 1 * 1 = 2^3 = 8

结论：
设 x 在排序后的数组中下标为 i（从 0 开始）
x 作为最大值的子序列的个数为 2^i
x 作为最小值的子序列的个数为 2^(n-1-i)
x 对答案的贡献为 (2^i - 2^(n-1-i)) * x
累加每个元素的贡献，得到答案

答疑
问：对于数组中有重复元素的情况，这种做法不会重复统计吗？

答：不会。例如计算最大值时，如果有多个相同元素 x，那么每个 x 都只会考虑在它左侧
的元素，而不会计入在它右侧的元素，所以不会有重复统计发生。


问：为什么 x 作为最小值的子序列的个数为 n−1−i ？

答：因为排序后，x 右侧有 n−1−i 个元素，每个元素都可以选或不选，这有 n−1−i 种方案，
也就对应着 n−1−i 个子序列。


"""


class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        N = len(nums)
        nums.sort()

        pow2 = [1] + [None] * (N - 1)
        for i in range(1, N):
            pow2[i] = pow2[i - 1] * 2 % MOD  # 预处理 2 的幂次

        return sum((pow2[i] - pow2[N - 1 - i]) * x for i, x in enumerate(nums)) % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [2, 1, 3]
        self.assertEqual(
            self.sl.sumSubseqWidths(nums),
            6,
        )

        nums = [2]
        self.assertEqual(
            self.sl.sumSubseqWidths(nums),
            0,
        )


if __name__ == "__main__":
    unittest.main()
