"""

[503] Next Greater Element II


Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.


Example 1:


Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.


Example 2:


Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]



Constraints:


	1 <= nums.length <= 10⁴
	-10⁹ <= nums[i] <= 10⁹

################################################################

# template
# tag: monotone stack

503. 下一个更大元素 II

给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。

数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1 。



示例 1:

输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数；
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。


示例 2:

输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]


提示:

1 <= nums.length <= 104
-109 <= nums[i] <= 109

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


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        N = len(nums)
        ans = [-1] * N
        nums = nums + nums
        for i, n in enumerate(nums):
            while st and nums[st[-1]] < n:
                cur = st.pop()
                ans[cur % N] = n
            st.append(i)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 2, 1]
        self.assertEqual(
            self.sl.nextGreaterElements(nums),
            [2, -1, 2],
        )

        nums = [1, 2, 3, 4, 3]
        self.assertEqual(
            self.sl.nextGreaterElements(nums),
            [2, 3, 4, -1, 4],
        )


if __name__ == "__main__":
    unittest.main()
