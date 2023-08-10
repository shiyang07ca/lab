# Created by shiyang07ca at 2023/05/28 16:58
# https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/
# https://leetcode.cn/contest/weekly-contest-347/problems/maximum-strictly-increasing-cells-in-a-matrix/

"""
6456. 矩阵中严格递增的单元格数 (Hard)
给你一个下标从 **1** 开始、大小为 `m x n` 的整数矩阵 `mat`，你可以选择任一单元格作为 **起始单元格**
。

从起始单元格出发，你可以移动到 **同一行或同一列** 中的任何其他单元格，但前提是目标单元格的值 **严格
大于** 当前单元格的值。

你可以多次重复这一过程，从一个单元格移动到另一个单元格，直到无法再进行任何移动。

请你找出从某个单元开始访问矩阵所能访问的 **单元格的最大数量** 。

返回一个表示可访问单元格最大数量的整数。

**示例 1：**

**![](https://assets.leetcode.com/uploads/2023/04/23/diag1drawio.png)**

```
输入：mat = [[3,1],[3,4]]
输出：2
解释：上图展示了从第 1 行、第 2 列的单元格开始，可以访问 2 个单元格。可以证明，无论从哪个单元格开始
，最多只能访问 2 个单元格，因此答案是 2 。

```

**示例 2：**

**![](https://assets.leetcode.com/uploads/2023/04/23/diag3drawio.png)**

```
输入：mat = [[1,1],[1,1]]
输出：1
解释：由于目标单元格必须严格大于当前单元格，在本示例中只能访问 1 个单元格。

```

**示例 3：**

**![](https://assets.leetcode.com/uploads/2023/04/23/diag4drawio.png)**

```
输入：mat = [[3,1,6],[-9,5,7]]
输出：4
解释：上图展示了从第 2 行、第 1 列的单元格开始，可以访问 4 个单元格。可以证明，无论从哪个单元格开始
，最多只能访问 4 个单元格，因此答案是 4 。

```

**提示：**

- `m == mat.length `
- `n == mat[i].length `
- `1 <= m, n <= 10⁵`
- `1 <= m * n <= 10⁵`
- `-10⁵ <= mat[i][j] <= 10⁵`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp


# 链接：https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/solutions/2286920/dong-tai-gui-hua-you-hua-pythonjavacgo-b-axv0/
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        g = defaultdict(list)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                g[x].append((i, j))  # 相同元素放在同一组，统计位置

        ans = 0
        row_max = [0] * len(mat)
        col_max = [0] * len(mat[0])
        for _, pos in sorted(g.items(), key=lambda p: p[0]):
            # 先把最大值算出来，再更新 row_max 和 col_max
            mx = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            ans = max(ans, max(mx))
            for (i, j), f in zip(pos, mx):
                row_max[i] = max(row_max[i], f)  # 更新第 i 行的最大 f 值
                col_max[j] = max(col_max[j], f)  # 更新第 j 列的最大 f 值
        return ans


# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxIncreasingCells(mat)

    print("\noutput:", serialize(ans))
