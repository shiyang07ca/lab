"""

[1043] Partition Array for Maximum Sum


Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.


Example 1:


Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]


Example 2:


Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83


Example 3:


Input: arr = [1], k = 1
Output: 1



Constraints:


	1 <= arr.length <= 500
	0 <= arr[i] <= 10⁹
	1 <= k <= arr.length

################################################################

# TODO
# tag: dp

1043. 分隔数组以得到最大和

给你一个整数数组 arr，请你将该数组分隔为长度 最多 为 k 的一些（连续）子数组。分
隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。

返回将数组分隔变换后能够得到的元素最大和。本题所用到的测试用例会确保答案是一个
32 位整数。


示例 1：

输入：arr = [1,15,7,9,2,5,10], k = 3
输出：84
解释：数组变为 [15,15,15,9,10,10,10]


示例 2：

输入：arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
输出：83


示例 3：

输入：arr = [1], k = 1
输出：1


提示：

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length

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
作者：灵茶山艾府
链接：
https://leetcode.cn/problems/partition-array-for-maximum-sum/solutions/2234242/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-rq5i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            # i=-1 时不会进入循环
            res = mx = 0
            for j in range(i, max(i - k, -1), -1):
                mx = max(mx, arr[j])  # 一边枚举 j，一边计算子数组的最大值
                res = max(res, dfs(j - 1) + (i - j + 1) * mx)
            return res

        return dfs(len(arr) - 1)


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
