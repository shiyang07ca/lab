# Created by shiyang07ca at 2023/06/04 13:07
# https://leetcode.cn/problems/sum-of-matrix-after-queries/
# https://leetcode.cn/contest/weekly-contest-348/problems/sum-of-matrix-after-queries/

"""
6472. 查询后矩阵的和 (Medium)
给你一个整数 `n` 和一个下标从 **0** 开始的 **二维数组** `queries` ，其中 `queries[i] = [typeᵢ, index
ᵢ, valᵢ]` 。

一开始，给你一个下标从 **0** 开始的 `n x n` 矩阵，所有元素均为 `0` 。每一个查询，你需要执行以下操作
之一：

- 如果 `typeᵢ == 0` ，将第 `indexᵢ` 行的元素全部修改为 `valᵢ` ，覆盖任何之前的值。
- 如果 `typeᵢ == 1` ，将第 `indexᵢ` 列的元素全部修改为 `valᵢ` ，覆盖任何之前的值。

请你执行完所有查询以后，返回矩阵中所有整数的和。

**示例 1：**

![](https://assets.leetcode.com/uploads/2023/05/11/exm1.png)

```
输入：n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
输出：23
解释：上图展示了每个查询以后矩阵的值。所有操作执行完以后，矩阵元素之和为 23 。

```

**示例 2：**

![](https://assets.leetcode.com/uploads/2023/05/11/exm2.png)

```
输入：n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
输出：17
解释：上图展示了每一个查询操作之后的矩阵。所有操作执行完以后，矩阵元素之和为 17 。

```

**提示：**

- `1 <= n <= 10⁴`
- `1 <= queries.length <= 5 * 10⁴`
- `queries[i].length == 3`
- `0 <= typeᵢ <= 1`
- `0 <= indexᵢ < n`
- `0 <= valᵢ <= 10⁵`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ans = 0
        col_set, row_set = set(), set()
        for t, x, v in queries[::-1]:
            if t == 0:  # row
                if x not in row_set:
                    ans += v * (n - len(col_set))
                    row_set.add(x)
            else:  # col
                if x not in col_set:
                    ans += v * (n - len(row_set))
                    col_set.add(x)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().matrixSumQueries(n, queries)

    print("\noutput:", serialize(ans))
