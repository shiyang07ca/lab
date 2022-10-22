"""

[1751] Maximum Number of Events That Can Be Attended II


You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.


Example 1:




Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.

Example 2:




Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.

Example 3:




Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.


Constraints:


	1 <= k <= events.length
	1 <= k * events.length <= 10⁶
	1 <= startDayi <= endDayi <= 10⁹
	1 <= valuei <= 10⁶


################################################################

# tag: dp, binary search


相似题目：

1235. 规划兼职工作
https://leetcode.cn/problems/maximum-profit-in-job-scheduling/

2008. 出租车的最大盈利
https://leetcode.cn/problems/maximum-earnings-from-taxi/

1751. 最多可以参加的会议数目 II
https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/


1751. 最多可以参加的会议数目 II

给你一个 events 数组，其中 events[i] = [startDayi, endDayi, valuei] ，表示第 i 个会议在 startDayi 天开始，第 endDayi 天结束，如果你参加这个会议，你能得到价值 valuei 。同时给你一个整数 k 表示你能参加的最多会议数目。

你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 完整 地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与另一个结束日期相同的两个会议。

请你返回能得到的会议价值 最大和


示例 1：

输入：events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
输出：7
解释：选择绿色的活动会议 0 和 1，得到总价值和为 4 + 3 = 7 。


示例 2：

输入：events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
输出：10
解释：参加会议 2 ，得到价值和为 10 。
你没法再参加别的会议了，因为跟会议 2 有重叠。你 不 需要参加满 k 个会议。


示例 3：

输入：events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
输出：9
解释：尽管会议互不重叠，你只能参加 3 个会议，所以选择价值最大的 3 个会议。


提示：

1 <= k <= events.length
1 <= k * events.length <= 106
1 <= startDayi <= endDayi <= 109
1 <= valuei <= 106

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


"""
https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/solution/dong-tai-gui-hua-er-fen-cha-zhao-you-hua-fuip/

"""


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        N = len(events)
        f = [[0] * (N + 1) for _ in range(k + 1)]
        events.sort(key=lambda x: x[1])
        ends = [e[1] for e in events]
        for i, (st, ed, v) in enumerate(events, 1):
            j = bisect_left(ends, st, hi=i - 1)
            for m in range(1, k + 1):
                f[m][i] = max(f[m][i - 1], f[m - 1][j] + v)

        return f[k][N]


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
