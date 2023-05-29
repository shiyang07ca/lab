# Created by shiyang07ca at 2023/05/28 16:57
# https://leetcode.cn/problems/difference-of-number-of-distinct-values-on-diagonals/
# https://leetcode.cn/contest/weekly-contest-347/problems/difference-of-number-of-distinct-values-on-diagonals/

"""
6440. 对角线上不同值的数量差 (Easy)
给你一个下标从 `0` 开始、大小为 `m x n` 的二维矩阵 `grid` ，请你求解大小同样为 `m x n` 的答案矩阵 `a
nswer` 。

矩阵 `answer` 中每个单元格 `(r, c)` 的值可以按下述方式进行计算：

- 令 `topLeft[r][c]` 为矩阵 `grid` 中单元格 `(r, c)` 左上角对角线上 **不同值** 的数量。
- 令 `bottomRight[r][c]` 为矩阵 `grid` 中单元格 `(r, c)` 右下角对角线上 **不同值** 的数量。

然后 `answer[r][c] = |topLeft[r][c] - bottomRight[r][c]|` 。

返回矩阵 `answer` 。

**矩阵对角线** 是从最顶行或最左列的某个单元格开始，向右下方向走到矩阵末尾的对角线。

如果单元格 `(r1, c1)` 和单元格 `(r, c) ` 属于同一条对角线且 `r1 < r` ，则单元格 `(r1, c1)` 属于单元
格 `(r, c)` 的左上对角线。类似地，可以定义右下对角线。

**示例 1：**

![](https://assets.leetcode.com/uploads/2023/04/19/ex2.png)

```
输入：grid = [[1,2,3],[3,1,5],[3,2,1]]
输出：[[1,1,0],[1,0,1],[0,1,1]]
解释：第 1 个图表示最初的矩阵 grid 。
第 2 个图表示对单元格 (0,0) 计算，其中蓝色单元格是位于右下对角线的单元格。
第 3 个图表示对单元格 (1,2) 计算，其中红色单元格是位于左上对角线的单元格。
第 4 个图表示对单元格 (1,1) 计算，其中蓝色单元格是位于右下对角线的单元格，红色单元格是位于左上对角线
的单元格。
- 单元格 (0,0) 的右下对角线包含 [1,1] ，而左上对角线包含 [] 。对应答案是 |1 - 0| = 1 。
- 单元格 (1,2) 的右下对角线包含 [] ，而左上对角线包含 [2] 。对应答案是 |0 - 1| = 1 。
- 单元格 (1,1) 的右下对角线包含 [1] ，而左上对角线包含 [1] 。对应答案是 |1 - 1| = 0 。
其他单元格的对应答案也可以按照这样的流程进行计算。

```

**示例 2：**

```
输入：grid = [[1]]
输出：[[0]]
解释：- 单元格 (0,0) 的右下对角线包含 [] ，左上对角线包含 [] 。对应答案是 |0 - 0| = 0 。

```

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n, grid[i][j] <= 50`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        def lu(i, j):
            cnt = set()
            k = 1
            while True:
                if 0 <= i - k and 0 <= j - k:
                    cnt.add(grid[i - k][j - k])
                    k += 1
                else:
                    return len(cnt)

        def rd(i, j):
            cnt = set()
            k = 1
            while True:
                if i + k < m and j + k < n:
                    cnt.add(grid[i + k][j + k])
                    k += 1
                else:
                    return len(cnt)

        for i in range(m):
            for j in range(n):
                ans[i][j] = abs(lu(i, j) - rd(i, j))

        return ans


# TODO
# tag: prefix sum
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            x, y = i, 0
            tmp = set()
            while x < n and y < m:
                ans[x][y] = len(tmp)
                tmp.add(grid[x][y])
                x += 1
                y += 1
        for j in range(1, m):
            x, y = 0, j
            tmp = set()
            while x < n and y < m:
                ans[x][y] = len(tmp)
                tmp.add(grid[x][y])
                x += 1
                y += 1
        for i in range(n):
            x, y = i, m - 1
            tmp = set()
            while x >= 0 and y >= 0:
                ans[x][y] = abs(ans[x][y] - len(tmp))
                tmp.add(grid[x][y])
                x -= 1
                y -= 1
        for j in range(m - 1):
            x, y = n - 1, j
            tmp = set()
            while x >= 0 and y >= 0:
                ans[x][y] = abs(ans[x][y] - len(tmp))
                tmp.add(grid[x][y])
                x -= 1
                y -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().differenceOfDistinctValues(grid)

    print("\noutput:", serialize(ans))
