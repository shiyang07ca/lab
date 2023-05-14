# Created by shiyang07ca at 2023/05/14 10:30
# https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/
# https://leetcode.cn/contest/weekly-contest-345/problems/maximum-number-of-moves-in-a-grid/

"""
6433. 矩阵中移动的最大次数 (Medium)
给你一个下标从 **0** 开始、大小为 `m x n` 的矩阵 `grid` ，矩
阵由若干 **正** 整数组成。

你可以从矩阵第一列中的 **任一** 单元格出发，按以下方式遍历 `
grid` ：

- 从单元格 `(row, col)` 可以移动到 `(row - 1, col + 1)`、 `(
row, col + 1)` 和 `(row + 1, col + 1)` 三个单元格中任一满足
值 **严格** 大于当前单元格的单元格。

返回你在矩阵中能够 **移动** 的 **最大** 次数。

**示例 1：**

![](https://assets.leetcode.com/uploads/2023/04/11/yetgriddr
awio-10.png)

```
输入：grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
输出：3
解释：可以从单元格 (0, 0) 开始并且按下面的路径移动：
- (0, 0) -> (0, 1).
- (0, 1) -> (1, 2).
- (1, 2) -> (2, 3).
可以证明这是能够移动的最大次数。
```

**示例 2：**

```

输入：grid = [[3,2,4],[2,1,9],[1,1,7]]
输出：0
解释：从第一列的任一单元格开始都无法移动。

```

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 10⁵`
- `1 <= grid[i][j] <= 10⁶`

"""
from functools import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxMoves(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])

        @cache
        def dfs(i, j):
            if i >= m or j >= n:
                return 0
            c = g[i][j]
            ans = 0
            if j + 1 < n and i >= 1 and c < g[i - 1][j + 1]:
                ans = max(ans, dfs(i - 1, j + 1) + 1)
            if j + 1 < n and i + 1 < m and c < g[i + 1][j + 1]:
                ans = max(ans, dfs(i + 1, j + 1) + 1)
            if j + 1 < n and c < g[i][j + 1]:
                ans = max(ans, dfs(i, j + 1) + 1)
            return ans

        return max(dfs(i, 0) for i in range(0, m))


"""
作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/solutions/2269244/cong-ji-yi-hua-sou-suo-dao-di-tui-by-end-pgq3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# 记忆化搜索
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int) -> int:
            if j == n - 1:
                return 0
            res = 0
            for k in i - 1, i, i + 1:
                if 0 <= k < m and grid[k][j + 1] > grid[i][j]:
                    res = max(res, dfs(k, j + 1) + 1)
            return res

        return max(dfs(i, 0) for i in range(m))


# 递推
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[0] * n for _ in range(m)]
        for j in range(n - 2, -1, -1):
            for i, row in enumerate(grid):
                for k in i - 1, i, i + 1:
                    if 0 <= k < m and grid[k][j + 1] > row[j]:
                        f[i][j] = max(f[i][j], f[k][j + 1] + 1)
        return max(row[0] for row in f)


# BFS
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = range(m)
        vis = [-1] * m
        for j in range(n - 1):
            tmp = q
            q = []
            for i in tmp:
                for k in i - 1, i, i + 1:
                    if 0 <= k < m and vis[k] != j and grid[k][j + 1] > grid[i][j]:
                        vis[k] = j  # 时间戳标记，避免重复创建 vis 数组
                        q.append(k)
            if len(q) == 0:
                return j
        return n - 1


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxMoves(grid)
    print("output:", serialize(ans))
