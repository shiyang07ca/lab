"""

300. Longest Increasing Subsequence
Given an integer array nums, return the length of the longest strictly increasing subsequence.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

################################################################

# TODO
# tag: dp, LIS, binary search

300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。


示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。


示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4


示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1


提示：

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


进阶：

你能将算法的时间复杂度降低到 O(n log(n)) 吗?

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def get_left_less(arr):
            left = [-1] * len(arr)
            st = []
            for i, e in enumerate(arr):
                # 如果破坏了栈单调性
                while st and arr[st[-1]] >= e:
                    st.pop()

                left[i] = st[-1] if st else -1
                st.append(i)

            return left

        stack = get_left_less(nums)
        N = len(nums)
        f = [1] * (N + 1)
        for i, n in enumerate(nums):

            if stack[i] != -1:
                t = 0
                for j in range(0, stack[i] + 1):
                    if nums[j] < n and f[j] > t:
                        t = f[j]
                f[i] = t + 1

        return max(f)


"""
作者：coldme-2
链接：https://leetcode.cn/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


动态规划 + 二分查找
很具小巧思。新建数组 cell，用于保存最长上升子序列。

对原序列进行遍历，将每位元素二分插入 f 中。

如果 f 中元素都比它小，将它插到最后
否则，用它覆盖掉比大于等于它的元素中最小的那个(bisect_left)。
总之，思想就是让 f 中存储比较小的元素。这样，f 未必是真实的最长上升子序列，但长度是对的。

"""


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return N
        f = [nums[0]]
        for n in nums[1:]:
            if n > f[-1]:
                f.append(n)
            else:
                l, r = 0, len(f) - 1
                while l < r:
                    mid = l + (r - l) // 2
                    if f[mid] >= n:
                        r = mid
                    else:
                        l = mid + 1
                f[l] = n
        return len(f)


"""
定义 f[i] 表示考虑前 i 个数字，以第 i 个数字结尾的最长递增子序列长度
     f[i] = max(f[j]) + 1  j < i 且 nums[j] < nums[i]
答案为 max(f)
"""


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.sl = Solution()
        self.sl = Solution1()

    def test_sl(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(
            self.sl.lengthOfLIS(nums),
            4,
        )

    def test_sl2(self):
        nums = [0, 1, 0, 3, 2, 3]
        print(nums)
        self.assertEqual(
            self.sl.lengthOfLIS(nums),
            4,
        )

    def test_sl3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(
            self.sl.lengthOfLIS(nums),
            1,
        )


if __name__ == "__main__":
    unittest.main()
