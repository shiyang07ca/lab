# Created by shiyang07ca at 2023/05/07 13:38
# https://leetcode.cn/problems/number-of-adjacent-elements-with-the-same-color/
# https://leetcode.cn/contest/weekly-contest-344/problems/number-of-adjacent-elements-with-the-same-color/

"""
6418. 有相同颜色的相邻元素数目 (Medium)
给你一个下标从 **0** 开始、长度为 `n` 的数组 `nums` 。一开始
，所有元素都是 **未染色** （值为 `0` ）的。

给你一个二维整数数组 `queries` ，其中 `queries[i] = [indexᵢ,
colorᵢ]` 。

对于每个操作，你需要将数组 `nums` 中下标为 `indexᵢ` 的格子染
色为 `colorᵢ` 。

请你返回一个长度与 `queries` 相等的数组 `answer`，其中 `answ
er[i]` 是前 `i` 个操作 **之后** ，相邻元素颜色相同的数目。

更正式的， `answer[i]` 是执行完前 `i` 个操作后， `0 <= j < n
- 1` 的下标 `j` 中，满足 `nums[j] == nums[j + 1]` 且 `nums[j
] != 0` 的数目。

**示例 1：**

```
输入：n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
输出：[0,1,1,0,2]
解释：一开始数组 nums = [0,0,0,0] ，0 表示数组中还没染色的元
素。
- 第 1 个操作后，nums = [2,0,0,0] 。相邻元素颜色相同的数目为
0 。
- 第 2 个操作后，nums = [2,2,0,0] 。相邻元素颜色相同的数目为
1 。
- 第 3 个操作后，nums = [2,2,0,1] 。相邻元素颜色相同的数目为
1 。
- 第 4 个操作后，nums = [2,1,0,1] 。相邻元素颜色相同的数目为
0 。
- 第 5 个操作后，nums = [2,1,1,1] 。相邻元素颜色相同的数目为
2 。

```

**示例 2：**

```
输入：n = 1, queries = [[0,100000]]
输出：[0]
解释：一开始数组 nums = [0] ，0 表示数组中还没染色的元素。
- 第 1 个操作后，nums = [100000] 。相邻元素颜色相同的数目为
0 。

```

**提示：**

- `1 <= n <= 10⁵`
- `1 <= queries.length <= 10⁵`
- `queries[i].length == 2`
- `0 <= indexᵢ <= n - 1`
- `1 <=  colorᵢ <= 10⁵`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# 模拟


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        a = [0] * n
        ans = []
        cnt = 0  # 相邻相同的数目
        for i, c in queries:
            if a[i]:  # 消除相同对数的影响
                if i and a[i] == a[i - 1]:
                    cnt -= 1
                if i < n - 1 and a[i] == a[i + 1]:
                    cnt -= 1
            a[i] = c
            if i and a[i] == a[i - 1]:
                cnt += 1
            if i < n - 1 and a[i] == a[i + 1]:
                cnt += 1
            ans.append(cnt)

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().colorTheArray(n, queries)
    print("output:", serialize(ans))
