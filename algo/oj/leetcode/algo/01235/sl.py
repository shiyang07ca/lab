"""

[1235] Maximum Profit in Job Scheduling


We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.


Example 1:




Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.


Example 2:




Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.


Example 3:




Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6



Constraints:


	1 <= startTime.length == endTime.length == profit.length <= 5 * 10⁴
	1 <= startTime[i] < endTime[i] <= 10⁹
	1 <= profit[i] <= 10⁴


################################################################

# TODO
# tag: dp, binary search


相似题目：

1235. 规划兼职工作
https://leetcode.cn/problems/maximum-profit-in-job-scheduling/

2008. 出租车的最大盈利
https://leetcode.cn/problems/maximum-earnings-from-taxi/

1751. 最多可以参加的会议数目 II
https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/



1235. 规划兼职工作
你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。



示例 1：

输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
输出：120
解释：
我们选出第 1 份和第 4 份工作，
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。


示例 2：

输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
输出：150
解释：
我们选择第 1，4，5 份工作。
共获得报酬 150 = 20 + 70 + 60。


示例 3：

输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
输出：6


提示：

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4

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


from bisect import *
from functools import cache


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        inv = sorted(zip(endTime, startTime, profit))
        ends = [i[0] for i in inv]
        dp = [0] * (len(inv) + 1)
        for i, (end, start, p) in enumerate(inv, 1):
            j = bisect_right(ends, start, hi=i - 1)
            # dp[i] 表示 当前 i 位置的最大利润，有两种选择，
            # 选 i 位置 + dp[j]，或者选择 i - 1 位置的最大利润，两者取最大值。
            # j 表示大于 target(start) 的下界, 因此应该将j - 1，又因为是从1
            # 开始循环，因此需要加 1，dp[j - 1 + 1]
            dp[i] = max(dp[i - 1], dp[j] + p)
        return dp[-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        startTime = [6, 15, 7, 11, 1, 3, 16, 2]
        endTime = [19, 18, 19, 16, 10, 8, 19, 8]
        profit = [2, 9, 1, 19, 5, 7, 3, 19]
        self.assertEqual(
            self.sl.jobScheduling(startTime, endTime, profit),
            41,
        )

        print("################################################################")

        startTime = [1, 2, 2, 3]
        endTime = [2, 5, 3, 4]
        profit = [3, 4, 1, 2]
        self.assertEqual(
            self.sl.jobScheduling(startTime, endTime, profit),
            7,
        )

        print("################################################################")

        startTime = [1, 2, 3, 3]
        endTime = [3, 4, 5, 6]
        profit = [50, 10, 40, 70]
        self.assertEqual(
            self.sl.jobScheduling(startTime, endTime, profit),
            # choose 1st and 4th work
            # segment is [1 ~ 3] + [3 ~ 6],  50 + 70 = 120
            120,
        )

        # return

        startTime = [1, 2, 3, 4, 6]
        endTime = [3, 5, 10, 6, 9]
        profit = [20, 20, 100, 70, 60]
        self.assertEqual(
            self.sl.jobScheduling(startTime, endTime, profit),
            # choose 1st, 4th and 5th  work
            # 20 + 70 + 60 = 150
            150,
        )

        startTime = [1, 1, 1]
        endTime = [2, 3, 4]
        profit = [5, 6, 4]
        self.assertEqual(
            self.sl.jobScheduling(startTime, endTime, profit),
            6,
        )

        return


if __name__ == "__main__":
    unittest.main()
