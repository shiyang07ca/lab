"""

[1124] Longest Well-Performing Interval


We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.


Example 1:


Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].


Example 2:


Input: hours = [6,6,6]
Output: 0



Constraints:


	1 <= hours.length <= 10⁴
	0 <= hours[i] <= 16

################################################################

# TODO
# tag: 单调栈；前缀和；哈希表; Prefix Sum; Monotonic Stack


1124. 表现良好的最长时间段

给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。

我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。

所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。

请你返回「表现良好时间段」的最大长度。



示例 1：

输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。


示例 2：

输入：hours = [6,6,6]
输出：0


提示：

1 <= hours.length <= 104
0 <= hours[i] <= 16


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

作者：lcbin
链接：https://leetcode.cn/problems/longest-well-performing-interval/solution/python3javacgo-yi-ti-yi-jie-qian-zhui-he-0os2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



方法一：前缀和 + 哈希表

我们可以利用前缀和的思想，维护一个变量 s，表示从下标 0 到当前下标的这一段，「劳
累的天数」与「不劳累的天数」的差值。如果 s 大于 0，说明从下标 0 到当前下标的这一
段，满足「表现良好的时间段」。另外，用哈希表 pos 记录每个 s 第一次出现的下标。

接下来，我们遍历数组 hours，对于每个下标 i：

* 如果 hours[i] > 8，我们就让 s 加 1，否则减 1。
* 如果 s 大于 0，说明从下标 0 到当前下标的这一段，满足「表现良好的时间段」，我们
更新结果 ans = i + 1。否则，如果 s−1 在哈希表 pos 中，记 j = pos[s−1]，说明从下
标 j+1 到当前下标 i 的这一段，满足「表现良好的时间段」，我们更新结果
ans=max(ans,i−j)。
* 如果 s 不在哈希表 pos 中，我们就记录 pos[s]=i。继续遍历下一个。


"""


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans = s = 0
        pos = {}
        for i, x in enumerate(hours):
            s += 1 if x > 8 else -1
            if s > 0:
                ans = i + 1
            elif s - 1 in pos:
                ans = max(ans, i - pos[s - 1])
            if s not in pos:
                pos[s] = i
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-well-performing-interval/solution/liang-chong-zuo-fa-liang-zhang-tu-miao-d-hysl/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1)  # 前缀和
        st = [0]  # s[0]
        for j, h in enumerate(hours, 1):
            s[j] = s[j - 1] + (1 if h > 8 else -1)
            if s[j] < s[st[-1]]:
                st.append(j)  # 感兴趣的 j
        ans = 0
        for i in range(n, 0, -1):
            while st and s[i] > s[st[-1]]:
                ans = max(ans, i - st.pop())  # [st[-1],i) 可能是最长子数组
        return ans


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
