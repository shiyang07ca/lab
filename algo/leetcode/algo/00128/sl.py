"""

# TODO

[128] Longest Consecutive Sequence


Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


--------------------------------------------------

Example 1:


Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


--------------------------------------------------

Example 2:


Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9



Constraints:


	0 <= nums.length <= 10⁵
	-10⁹ <= nums[i] <= 10⁹

################################################################

128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。


示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109

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


from algo.tree.builder import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nmap = set(nums)
        ans = 0

        for n in nmap:
            # 如果 n - 1 不再 map 中，说明 n 是左边界
            if n - 1 not in nmap:
                l = 0
                # 如果 n 在 map 中，更新长度
                while n in nmap:
                    n += 1
                    l += 1

                if l > ans:
                    ans = l

        return ans

    def longestConsecutive2(self, nums: List[int]) -> int:

        lmap = {}
        ans = 0
        for n in nums:
            if n not in lmap:
                # 左右两边的 value 分别表示两边的值的长度
                left = lmap.get(n - 1, 0)
                right = lmap.get(n + 1, 0)

                cur_length = left + 1 + right
                if cur_length > ans:
                    ans = cur_length

                # 更新最左和最右边界的值
                lmap[n] = lmap[n - left] = lmap[n + right] = cur_length

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [100, 4, 200, 1, 3, 2]
        self.assertEqual(
            self.sl.longestConsecutive(nums),
            4,
        )

    def test_sl2(self):
        nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
        self.assertEqual(
            self.sl.longestConsecutive(nums),
            9,
        )


if __name__ == "__main__":
    unittest.main()
