# Created by shiyang07ca at 2023/05/15 13:03
# https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/

"""
1072. 按列翻转得到最大值等行数 (Medium)
给定 `m x n` 矩阵 `matrix` 。

你可以从中选出任意数量的列并翻转其上的 **每个** 单元格。（即翻转后，单元格的值从 `0` 变成 `1`，或者
从 `1` 变为 `0` 。）

返回 经过一些翻转后，行与行之间所有值都相等的最大行数 。

**示例 1：**

```
输入：matrix = [[0,1],[1,1]]
输出：1
解释：不进行翻转，有 1 行所有值都相等。

```

**示例 2：**

```
输入：matrix = [[0,1],[1,0]]
输出：2
解释：翻转第一列的值之后，这两行都由相等的值组成。

```

**示例 3：**

```
输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
输出：2
解释：翻转前两列的值之后，后两行由相等的值组成。
```

**提示：**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j] == 0` 或 `1`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO

"""
作者：ylb
链接：https://leetcode.cn/problems/flip-columns-for-maximum-number-of-equal-rows/solutions/2270337/python3javacgotypescript-yi-ti-yi-jie-ha-gl17/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            cnt[t] += 1
        return max(cnt.values())


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxEqualRowsAfterFlips(matrix)

    print("\noutput:", serialize(ans))
