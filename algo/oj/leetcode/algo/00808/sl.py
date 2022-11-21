"""

[808] Soup Servings


There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:


	Serve 100 ml of soup A and 0 ml of soup B,
	Serve 75 ml of soup A and 25 ml of soup B,
	Serve 50 ml of soup A and 50 ml of soup B, and
	Serve 25 ml of soup A and 75 ml of soup B.


When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

* * * * * * * * * * * * * * * * * * * * * * * * *

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.


Example 1:


Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.


Example 2:


Input: n = 100
Output: 0.71875



Constraints:


	0 <= n <= 10⁹

################################################################

# TODO


808. 分汤


有 A 和 B 两种类型 的汤。一开始每种类型的汤有 n 毫升。有四种分配操作：

提供 100ml 的 汤A 和 0ml 的 汤B 。
提供 75ml 的 汤A 和 25ml 的 汤B 。
提供 50ml 的 汤A 和 50ml 的 汤B 。
提供 25ml 的 汤A 和 75ml 的 汤B 。
当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为 0.25 的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。

注意 不存在先分配 100 ml 汤B 的操作。

需要返回的值： 汤A 先分配完的概率 +  汤A和汤B 同时分配完的概率 / 2。返回值在正确答案 10-5 的范围内将被认为是正确的。



示例 1:

输入: n = 50
输出: 0.62500
解释:如果我们选择前两个操作，A 首先将变为空。
对于第三个操作，A 和 B 会同时变为空。
对于第四个操作，B 首先将变为空。
所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.25 *(1 + 1 + 0.5 + 0)= 0.625。


示例 2:

输入: n = 100
输出: 0.71875


提示:

0 <= n <= 109

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *
from copy import *
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

# https://leetcode.cn/problems/soup-servings/solution/by-lcbin-44pu/


class Solution:
    def soupServings(self, n: int) -> float:
        op = [[-100, 0], [-75, -25], [-50, -50], [-25, -75]]

        @cache
        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0 and b > 0:
                return 1.0
            elif a > 0 and b <= 0:
                return 0.0

            ans = 0.0
            for o in op:
                ans += dfs(a + o[0], b + o[1])
            return 0.25 * ans

        return 1.0 if n >= 5000 else dfs(n, n)


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
