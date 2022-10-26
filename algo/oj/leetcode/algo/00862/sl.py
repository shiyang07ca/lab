"""

[862] Shortest Subarray with Sum at Least K


Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.


Example 1:
Input: nums = [1], k = 1
Output: 1
Example 2:
Input: nums = [1,2], k = 4
Output: -1
Example 3:
Input: nums = [2,-1,2], k = 3
Output: 3


Constraints:


	1 <= nums.length <= 10⁵
	-10⁵ <= nums[i] <= 10⁵
	1 <= k <= 10⁹

################################################################

# TODO
# tag: 前缀和

862. 和至少为 K 的最短子数组
给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的
最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。

子数组 是数组中 连续 的一部分。


示例 1：

输入：nums = [1], k = 1
输出：1


示例 2：

输入：nums = [1,2], k = 4
输出：-1


示例 3：

输入：nums = [2,-1,2], k = 3
输出：3


提示：

1 <= nums.length <= 10^5
-105 <= nums[i] <= 10^5
1 <= k <= 109


"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import deque

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

from math import inf

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solution/liang-zhang-tu-miao-dong-dan-diao-dui-li-9fvh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = inf
        s = list(accumulate(nums, initial=0))  # 计算前缀和
        print(s)
        q = deque()
        for i, cur_s in enumerate(s):
            while q and cur_s - s[q[0]] >= k:
                ans = min(ans, i - q.popleft())  # 优化一
            while q and s[q[-1]] >= cur_s:
                q.pop()  # 优化二
            q.append(i)
        return ans if ans < inf else -1


# 前缀和数组 TLE
class Solution1:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + n)
        # print(nums)
        # print(pre)
        ans = inf
        N = len(nums)
        flags = [True] * N
        for i in range(N):
            if not flags[i]:
                break
            for j in range(i + 1, N + 1):
                # print(f"{i}~{j}", pre[j] - pre[i])
                if pre[i] >= pre[j]:
                    flags[i] = False
                    break
                elif pre[j] - pre[i] >= k:
                    ans = min(ans, j - i)
                    flags[i] = False
                    break

        return -1 if ans is inf else ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1]
        k = 1
        self.assertEqual(
            self.sl.shortestSubarray(nums, k),
            1,
        )
        nums = [2]
        k = 1
        self.assertEqual(
            self.sl.shortestSubarray(nums, k),
            1,
        )

        nums = [1, 2]
        k = 4
        self.assertEqual(
            self.sl.shortestSubarray(nums, k),
            -1,
        )

        nums = [2, -1, 2]
        k = 3
        self.assertEqual(
            self.sl.shortestSubarray(nums, k),
            3,
        )

        nums = [4, -1, 2, 2]
        k = 3
        self.assertEqual(
            self.sl.shortestSubarray(nums, k),
            1,
        )

        nums = [48, 99, 37, 4, -31]
        k = 140
        self.assertEqual(
            self.sl.shortestSubarray(nums, k),
            2,
        )


if __name__ == "__main__":
    unittest.main()
