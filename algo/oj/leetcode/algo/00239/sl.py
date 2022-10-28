"""

[239] Sliding Window Maximum


You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Example 1:


Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Example 2:


Input: nums = [1], k = 1
Output: [1]



Constraints:


	1 <= nums.length <= 10⁵
	-10⁴ <= nums[i] <= 10⁴
	1 <= k <= nums.length

################################################################


# TODO
# template
# tag: sliding window, monotone queue, two pointer

239. 滑动窗口最大值

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。



示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


示例 2：

输入：nums = [1], k = 1
输出：[1]


提示：

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        index = 0
        # ans = [None] * (len(nums) - k + 1)
        ans = []
        # print(nums)
        for i, n in enumerate(nums):
            while q and nums[q[-1]] <= n:
                q.pop()
            q.append(i)

            while q and (i - q[0]) >= k:
                q.popleft()

            if i + 1 >= k:
                ans.append(nums[q[0]])
                # index += 1
            # print(i, q, ans, )

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        self.assertEqual(
            self.sl.maxSlidingWindow(nums, k),
            [3, 3, 5, 5, 6, 7],
        )

        nums = [1]
        k = 1
        self.assertEqual(self.sl.maxSlidingWindow(nums, k), [1])

        nums = [7, 2, 4]
        k = 2
        self.assertEqual(self.sl.maxSlidingWindow(nums, k), [7, 4])


if __name__ == "__main__":
    unittest.main()
