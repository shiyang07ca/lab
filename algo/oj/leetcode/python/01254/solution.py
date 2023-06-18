# Created by shiyang07ca at 2023/06/18 23:03
# https://leetcode.cn/problems/number-of-closed-islands/

"""
1254. 统计封闭岛屿的数目 (Medium)
二维矩阵 `grid` 由 `0` （土地）和 `1` （水）组成。岛是由最大的4个方向连通的 `0` 组成的群，封闭岛是一
个 `完全` 由1包围（左、上、右、下）的岛。

请返回 封闭岛屿 的数目。

**示例 1：**

![](https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png)

```
输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1
,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
```

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/07/sample_4_1610.png)

```
输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1

```

**示例 3：**

```
输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2

```

**提示：**

- `1 <= grid.length, grid[0].length <= 100`
- `0 <= grid[i][j] <=1`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO

# 链接：https://leetcode.cn/problems/number-of-closed-islands/solutions/2312631/python3javacgotypescript-yi-ti-shuang-ji-ttoe/
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int) -> int:
            res = int(0 < i < m - 1 and 0 < j < n - 1)
            grid[i][j] = 1
            for a, b in pairwise(dirs):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    res &= dfs(x, y)
            return res

        m, n = len(grid), len(grid[0])
        dirs = (-1, 0, 1, 0, -1)
        return sum(grid[i][j] == 0 and dfs(i, j) for i in range(m) for j in range(n))


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().closedIsland(grid)

    print("\noutput:", serialize(ans))
