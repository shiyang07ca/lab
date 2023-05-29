# Created by shiyang07ca at 2023/05/28 16:58
# https://leetcode.cn/problems/minimum-cost-to-make-all-characters-equal/
# https://leetcode.cn/contest/weekly-contest-347/problems/minimum-cost-to-make-all-characters-equal/

"""
6455. 使所有字符相等的最小成本 (Medium)
给你一个下标从 **0** 开始、长度为 `n` 的二进制字符串 `s` ，你可以对其执行两种操作：

- 选中一个下标 `i` 并且反转从下标 `0` 到下标 `i`（包括下标 `0` 和下标 `i` ）的所有字符，成本为 `i +
1` 。
- 选中一个下标 `i` 并且反转从下标 `i` 到下标 `n - 1`（包括下标 `i` 和下标 `n - 1` ）的所有字符，成本
为 `n - i` 。

返回使字符串内所有字符 **相等** 需要的 **最小成本** 。

**反转** 字符意味着：如果原来的值是 '0' ，则反转后值变为 '1' ，反之亦然。

**示例 1：**

```
输入：s = "0011"
输出：2
解释：执行第二种操作，选中下标 i = 2 ，可以得到 s = "0000" ，成本为 2 。可以证明 2 是使所有字符相等
的最小成本。

```

**示例 2：**

```
输入：s = "010101"
输出：9
解释：执行第一种操作，选中下标 i = 2 ，可以得到 s = "101101" ，成本为 3 。
执行第一种操作，选中下标 i = 1 ，可以得到 s = "011101" ，成本为 2 。
执行第一种操作，选中下标 i = 0 ，可以得到 s = "111101" ，成本为 1 。
执行第二种操作，选中下标 i = 4 ，可以得到 s = "111110" ，成本为 2 。
执行第一种操作，选中下标 i = 5 ，可以得到 s = "111111" ，成本为 1 。
使所有字符相等的总成本等于 9 。可以证明 9 是使所有字符相等的最小成本。
```

**提示：**

- `1 <= s.length == n <= 10⁵`
- `s[i]` 为 `'0'` 或 `'1'`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            if s[i] != s[i - 1]:
                ans += min(i, n - i)
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().minimumCost(s)

    print("\noutput:", serialize(ans))
