"""

[795] Number of Subarrays with Bounded Maximum


Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.


Example 1:


Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].


Example 2:


Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7



Constraints:


	1 <= nums.length <= 10⁵
	0 <= nums[i] <= 10⁹
	0 <= left <= right <= 10⁹


################################################################

# TODO
# tag: monotonic stack
# 贡献法


795. 区间子数组个数
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最
大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。


生成的测试用例保证结果符合 32-bit 整数范围。


示例 1：

输入：nums = [2,1,4,3], left = 2, right = 3
输出：3
解释：满足条件的三个子数组：[2], [2, 1], [3]


示例 2：

输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7


提示：

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9


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
    def numSubarrayBoundedMax(self, nums: List[int], l: int, r: int) -> int:
        N = len(nums)
        left = [-1] * N  # left[i] 为左侧严格大于 nums[i] 的最近元素位置（不存在时为-1）
        right = [N] * N  # left[i] 为右侧大于等于 nums[i] 的最近元素位置（不存在时为 N）
        st = []
        for i, n in enumerate(nums):
            while st and nums[st[-1]] <= n:
                popi = st.pop()
                right[popi] = i
            left[i] = st[-1] if st else -1
            st.append(i)

        ans = 0
        for i, n in enumerate(nums):
            if l <= n <= r:
                print(left[i], i, right[i], n, (i - left[i]) * (right[i] - i))
                ans += (i - left[i]) * (right[i] - i)

        return ans


"""
作者：lcbin
链接：https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/solution/by-lcbin-0l6h/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

区间计数

题目要我们统计数组 nums 中，最大值在区间 [left, right] 范围内的子数组个数。

对于区间 [left,..right] 问题，我们可以考虑将其转换为 [0,..right] 然后再减去
[0,..left−1] 的问题。也就是说，所有最大元素不超过 right 的子数组个数，减去所有最
大元素不超过 left-1 的子数组个数，剩下的就是最大元素在区间 [left,..right] 范围内
的子数组个数，即题目要求的结果。

对于本题，我们只需要设计一个函数 f(x)，表示数组 nums 中，最大值不超过 x 的子数组
个数。那么答案为 f(right) - f(left-1)。函数 f(x) 的执行逻辑如下：

* 用变量 cnt 记录最大值不超过 x 的子数组的个数，用 t 记录当前子数组的长度。

* 遍历数组 nums，对于每个元素 nums[i]，如果 nums[i]≤x，则当前子数组的长度加一，即
t=t+1，否则当前子数组的长度重置为 0，即 t=0。然后将当前子数组的长度加到 cnt 中，
即 cnt = cnt + t

* 遍历结束，将 cnt 返回即可。

"""


class Solution1:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def f(x):
            cnt = t = 0
            for v in nums:
                t = 0 if v > x else t + 1
                cnt += t
            return cnt

        return f(right) - f(left - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()
        # self.sl = Solution1()

    def test_sl(self):
        nums = [2, 1, 4, 3]
        left = 2
        right = 3
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            3,
        )

        nums = [73, 55, 36, 5, 55, 14, 9, 7, 72, 52]
        left = 32
        right = 69
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            22,
        )

        nums = [2, 9, 2, 5, 6]
        left = 2
        right = 8
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            7,
        )

        nums = [4]
        left = 5
        right = 6
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            0,
        )

        nums = [4]
        left = 1
        right = 2
        self.assertEqual(
            self.sl.numSubarrayBoundedMax(nums, left, right),
            0,
        )


if __name__ == "__main__":
    unittest.main()
