"""

[1624] Largest Substring Between Two Equal Characters


Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.


--------------------------------------------------

Example 1:


Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

--------------------------------------------------

Example 2:


Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".


--------------------------------------------------

Example 3:


Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.



Constraints:


	1 <= s.length <= 300
	s contains only lowercase English letters.

################################################################

# TODO

1642. 可以到达的最远建筑


给你一个整数数组 heights ，表示建筑物的高度。另有一些砖块 bricks 和梯子 ladders 。

你从建筑物 0 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。

当从建筑物 i 移动到建筑物 i+1（下标 从 0 开始 ）时：

如果当前建筑物的高度 大于或等于 下一建筑物的高度，则不需要梯子或砖块
如果当前建筑的高度 小于 下一个建筑的高度，您可以使用 一架梯子 或 (h[i+1] - h[i]) 个砖块
如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 从 0 开始 ）。


示例 1：


输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
输出：4
解释：从建筑物 0 出发，你可以按此方案完成旅程：
- 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
- 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 < 7
- 不使用砖块或梯子到达建筑物 3 ，因为 7 >= 6
- 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
无法越过建筑物 4 ，因为没有更多砖块或梯子。


示例 2：

输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
输出：7


示例 3：

输入：heights = [14,3,19,3], bricks = 17, ladders = 0
输出：3


提示：

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length

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


from collections import *
from heapq import *


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        sum_brick = 0
        N = len(heights)
        for i in range(1, N):
            cost = heights[i] - heights[i - 1]
            if cost <= 0:
                continue

            """
            贪心，优先队列


            维护长度为 ladders 的小根堆，用来存储遍历到当前位置代价最大的长度。
            当堆的长度大于 ladders 时，需要消耗砖块来到达下一位置。

            每次弹出堆顶，表示通过当前节点必须消耗砖块数目，当总砖块花销大于 bricks 时，
            循环结束，找到答案
            """
            heappush(heap, cost)
            if len(heap) > ladders:
                c = heappop(heap)
                sum_brick += c
                if sum_brick > bricks:
                    return i - 1
        return N - 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        heights = [4, 2, 7, 6, 9, 14, 12]
        bricks = 5
        ladders = 1
        self.assertEqual(
            self.sl.furthestBuilding(heights, bricks, ladders),
            4,
        )

        heights = [4, 12, 2, 7, 3, 18, 20, 3, 19]
        bricks = 10
        ladders = 2
        self.assertEqual(
            self.sl.furthestBuilding(heights, bricks, ladders),
            7,
        )

        heights = [14, 3, 19, 3]
        bricks = 17
        ladders = 0
        self.assertEqual(
            self.sl.furthestBuilding(heights, bricks, ladders),
            3,
        )

        heights = [1, 5, 1, 2, 3, 4, 10000]
        bricks = 4
        ladders = 1
        self.assertEqual(
            self.sl.furthestBuilding(heights, bricks, ladders),
            5,
        )


if __name__ == "__main__":
    unittest.main()
