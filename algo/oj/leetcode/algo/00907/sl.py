"""

[907] Sum of Subarray Minimums


Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 10⁹ + 7.


Example 1:


Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.


Example 2:


Input: arr = [11,81,94,43,3]
Output: 444



Constraints:


	1 <= arr.length <= 3 * 10⁴
	1 <= arr[i] <= 3 * 10⁴

################################################################

# TODO
# tag: monotone stack

907. 子数组的最小值之和

给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。

由于答案可能很大，因此 返回答案模 10^9 + 7 。



示例 1：

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。


示例 2：

输入：arr = [11,81,94,43,3]
输出：444


提示：

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4

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

https://leetcode.cn/problems/sum-of-subarray-minimums/solution/gong-xian-fa-dan-diao-zhan-san-chong-shi-gxa5/

思路

找到以每个元素为最小值的子树组个数，也就是找到比当前元素的小的左右边界，
计算子树组个数，乘以当前元素，就是对总和的贡献


i      0       1        2        3    4
a    [ 3       1        2        4 ]

    (-1, 1)   (-1, 4)  (1, 4)   (2, 4)

     1 * 1      2 * 3    1 * 2     1 * 1
     3 * 1 +   1 * 6  +  2 * 2 +  4 * 1  = 17

"""


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        pos = [[]] * len(arr)
        st = []
        N = len(arr)

        for i, n in enumerate(arr):
            while st and arr[st[-1]] >= n:
                index = st.pop()
                left = st[-1] if st else -1
                pos[index] = [left, i]
            st.append(i)

        while st:
            index = st.pop()
            left = st[-1] if st else -1
            pos[index] = [left, N]

        print(f"pos: {pos}")

        ans = 0
        for i, (l, r) in enumerate(pos):
            ans += (i - l) * (r - i) * arr[i]

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        arr = [3, 1, 2, 4]
        self.assertEqual(
            self.sl.sumSubarrayMins(arr),
            17,
        )

        arr = [11, 81, 94, 43, 3]
        self.assertEqual(
            self.sl.sumSubarrayMins(arr),
            444,
        )

        arr = [1, 2, 4, 2, 3, 1]
        self.sl.sumSubarrayMins(arr)


if __name__ == "__main__":
    unittest.main()
