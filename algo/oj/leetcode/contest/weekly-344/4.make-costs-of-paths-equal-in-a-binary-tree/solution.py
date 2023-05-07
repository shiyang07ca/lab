# Created by shiyang07ca at 2023/05/07 13:38
# https://leetcode.cn/problems/make-costs-of-paths-equal-in-a-binary-tree/
# https://leetcode.cn/contest/weekly-contest-344/problems/make-costs-of-paths-equal-in-a-binary-tree/

"""
6419. 使二叉树所有路径值相等的最小代价 (Medium)
给你一个整数 `n` 表示一棵 **满二叉树** 里面节点的数目，节点
编号从 `1` 到 `n` 。根节点编号为 `1` ，树中每个非叶子节点 `i
` 都有两个孩子，分别是左孩子 `2 * i` 和右孩子 `2 * i + 1` 。

树中每个节点都有一个值，用下标从 **0** 开始、长度为 `n` 的整
数数组 `cost` 表示，其中 `cost[i]` 是第 `i + 1` 个节点的值。
每次操作，你可以将树中 **任意** 节点的值 **增加** `1` 。你可
以执行操作 **任意** 次。

你的目标是让根到每一个 **叶子结点** 的路径值相等。请你返回 *
*最少** 需要执行增加操作多少次。

**注意：**

- **满二叉树** 指的是一棵树，它满足树中除了叶子节点外每个节
点都恰好有 2 个节点，且所有叶子节点距离根节点距离相同。
- **路径值** 指的是路径上所有节点的值之和。

**示例 1：**

![](https://assets.leetcode.com/uploads/2023/04/04/binaryytr
eeedrawio-4.png)

```
输入：n = 7, cost = [1,5,2,2,3,3,1]
输出：6
解释：我们执行以下的增加操作：
- 将节点 4 的值增加一次。
- 将节点 3 的值增加三次。
- 将节点 7 的值增加两次。
从根到叶子的每一条路径值都为 9 。
总共增加次数为 1 + 3 + 2 = 6 。
这是最小的答案。

```

**示例 2：**

![](https://assets.leetcode.com/uploads/2023/04/04/binaryytr
eee2drawio.png)

```
输入：n = 3, cost = [5,3,3]
输出：0
解释：两条路径已经有相等的路径值，所以不需要执行任何增加操作
。

```

**提示：**

- `3 <= n <= 10⁵`
- `n + 1` 是 `2` 的幂
- `cost.length == n`
- `1 <= cost[i] <= 10⁴`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: greedy


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        for i in range(2, n + 1):
            cost[i - 1] += cost[i // 2 - 1]  # 累加路径和
        ans = 0
        for i in range(n // 2, 0, -1):  # 从叶子开始遍历
            ans += abs(cost[i * 2 - 1] - cost[i * 2])  # 两个子节点变成一样的
            cost[i - 1] = max(cost[i * 2 - 1], cost[i * 2])  # 把子节点的路径和返给当前节点
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minIncrements(n, cost)
    print("output:", serialize(ans))
