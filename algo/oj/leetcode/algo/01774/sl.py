"""

[1774] Closest Dessert Cost


You would like to make dessert and are preparing to buy the ingredients. You have n ice cream base flavors and m types of toppings to choose from. You must follow these rules when making your dessert:


	There must be exactly one ice cream base.
	You can add one or more types of topping or have no toppings at all.
	There are at most two of each type of topping.


You are given three inputs:


	baseCosts, an integer array of length n, where each baseCosts[i] represents the price of the ith ice cream base flavor.
	toppingCosts, an integer array of length m, where each toppingCosts[i] is the price of one of the ith topping.
	target, an integer representing your target price for dessert.


You want to make a dessert with a total cost as close to target as possible.

Return the closest possible cost of the dessert to target. If there are multiple, return the lower one.


Example 1:


Input: baseCosts = [1,7], toppingCosts = [3,4], target = 10
Output: 10
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 7
- Take 1 of topping 0: cost 1 x 3 = 3
- Take 0 of topping 1: cost 0 x 4 = 0
Total: 7 + 3 + 0 = 10.


Example 2:


Input: baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
Output: 17
Explanation: Consider the following combination (all 0-indexed):
- Choose base 1: cost 3
- Take 1 of topping 0: cost 1 x 4 = 4
- Take 2 of topping 1: cost 2 x 5 = 10
- Take 0 of topping 2: cost 0 x 100 = 0
Total: 3 + 4 + 10 + 0 = 17. You cannot make a dessert with a total cost of 18.


Example 3:


Input: baseCosts = [3,10], toppingCosts = [2,5], target = 9
Output: 8
Explanation: It is possible to make desserts with cost 8 and 10. Return 8 as it is the lower cost.



Constraints:


	n == baseCosts.length
	m == toppingCosts.length
	1 <= n, m <= 10
	1 <= baseCosts[i], toppingCosts[i] <= 10⁴
	1 <= target <= 10⁴

################################################################

# TODO
# tag: dp

1774. 最接近目标价格的甜点成本


你打算做甜点，现在需要购买配料。目前共有 n 种冰激凌基料和 m 种配料可供选购。而制作甜点需要遵循以下几条规则：

必须选择 一种 冰激凌基料。
可以添加 一种或多种 配料，也可以不添加任何配料。
每种类型的配料 最多两份 。
给你以下三个输入：

baseCosts ，一个长度为 n 的整数数组，其中每个 baseCosts[i] 表示第 i 种冰激凌基料的价格。
toppingCosts，一个长度为 m 的整数数组，其中每个 toppingCosts[i] 表示 一份 第 i 种冰激凌配料的价格。
target ，一个整数，表示你制作甜点的目标价格。
你希望自己做的甜点总成本尽可能接近目标价格 target 。

返回最接近 target 的甜点成本。如果有多种方案，返回 成本相对较低 的一种。



示例 1：

输入：baseCosts = [1,7], toppingCosts = [3,4], target = 10
输出：10
解释：考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 7
- 选择 1 份 0 号配料：成本 1 x 3 = 3
- 选择 0 份 1 号配料：成本 0 x 4 = 0
总成本：7 + 3 + 0 = 10 。


示例 2：

输入：baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
输出：17
解释：考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 3
- 选择 1 份 0 号配料：成本 1 x 4 = 4
- 选择 2 份 1 号配料：成本 2 x 5 = 10
- 选择 0 份 2 号配料：成本 0 x 100 = 0
总成本：3 + 4 + 10 + 0 = 17 。不存在总成本为 18 的甜点制作方案。


示例 3：

输入：baseCosts = [3,10], toppingCosts = [2,5], target = 9
输出：8
解释：可以制作总成本为 8 和 10 的甜点。返回 8 ，因为这是成本更低的方案。


示例 4：

输入：baseCosts = [10], toppingCosts = [1], target = 1
输出：10
解释：注意，你可以选择不添加任何配料，但你必须选择一种基料。


提示：

n == baseCosts.length
m == toppingCosts.length
1 <= n, m <= 10
1 <= baseCosts[i], toppingCosts[i] <= 104
1 <= target <= 104

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


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], t: int) -> int:

        NT = len(toppingCosts)

        def cmp(c1, c2):
            if abs(c1 - t) < abs(c2 - t):
                return c1
            elif abs(c1 - t) == abs(c2 - t):
                return c1 if c1 < c2 else c2
            else:
                return c2

        ans = inf

        @cache
        def dfs(j, mi):
            if j == NT:
                nonlocal ans
                ans = cmp(ans, mi)
                return mi
            else:
                dfs(j + 1, mi)

                c1 = mi + toppingCosts[j] * 1
                c2 = cmp(c1, mi)
                dfs(j + 1, c2)

                c3 = mi + toppingCosts[j] * 2
                mi = cmp(c3, c2)
                dfs(j + 1, mi)

        for c in baseCosts:
            dfs(0, c)
        #         print(ans)
        return ans


"""
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/closest-dessert-cost/solution/zui-jie-jin-mu-biao-jie-ge-de-tian-dian-2ck06/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

首先题目给出长度分别为 nn 的冰淇淋基料数组 baseCosts 和长度为 mm 的配料数组
toppingCosts，其中 baseCosts[i] 表示第 i 种冰淇淋基料的价格，toppingCosts[j] 表
示一份第 j 种冰淇淋配料的价格，以及一个整数 target 表示我们需要制作甜点的目标价
格。现在在制作甜品上我们需要遵守以下三条规则：

必须选择一种冰淇淋基料；
可以添加一种或多种配料，也可以不添加任何配料；
每种配料最多两份。
我们希望做的甜点总成本尽可能接近目标价格 target，那么我们现在按照规则对于每一种
冰淇淋基料用回溯的方式来针对它进行甜品制作。又因为每一种配料都是正整数，所以在回
溯的过程中总开销只能只增不减，当回溯过程中当前开销大于目标价格 target 后，继续往
下搜索只能使开销与 target 的差值更大，所以如果此时差值已经大于等于我们已有最优方
案的差值，我们可以停止继续往下搜索，及时回溯。


"""


class Solution:
    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        ans = min(baseCosts)

        def dfs(p: int, cur_cost: int) -> None:
            nonlocal ans
            if abs(ans - target) < cur_cost - target:
                return
            if abs(ans - target) >= abs(cur_cost - target):
                if abs(ans - target) > abs(cur_cost - target):
                    ans = cur_cost
                else:
                    ans = min(ans, cur_cost)
            if p == len(toppingCosts):
                return
            dfs(p + 1, cur_cost + toppingCosts[p] * 2)
            dfs(p + 1, cur_cost + toppingCosts[p])
            dfs(p + 1, cur_cost)

        for c in baseCosts:
            dfs(0, c)
        return ans


"""

作者：lcbin
链接：https://leetcode.cn/problems/closest-dessert-cost/solution/by-lcbin-oaao/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

每种类型的配料最多可以选两份，因此，我们可以复制一份配料，然后利用 DFS 枚举子集
之和。在实现上，我们可以只枚举一半的配料的所有子集和，然后在另一半配料子集和中，
利用二分查找找到最接近的配料。

"""


class Solution:
    def closestCost(
        self, baseCosts: List[int], toppingCosts: List[int], target: int
    ) -> int:
        def dfs(i, t):
            if i >= len(toppingCosts):
                arr.append(t)
                return
            dfs(i + 1, t)
            dfs(i + 1, t + toppingCosts[i])

        arr = []
        dfs(0, 0)
        arr.sort()
        d = ans = inf

        # 选择一种冰激淋基料
        for x in baseCosts:
            # 枚举子集和
            for y in arr:
                # 二分查找
                i = bisect_left(arr, target - x - y)
                for j in (i, i - 1):
                    if 0 <= j < len(arr):
                        t = abs(x + y + arr[j] - target)
                        if d > t or (d == t and ans > x + y + arr[j]):
                            d = t
                            ans = x + y + arr[j]
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
