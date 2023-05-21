# Created by shiyang07ca at 2023/05/21 12:19
# https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/
# https://leetcode.cn/contest/weekly-contest-346/problems/find-the-punishment-number-of-an-integer/

"""
6441. 求一个整数的惩罚数 (Medium)
给你一个正整数 `n` ，请你返回 `n` 的 **惩罚数** 。

`n` 的 **惩罚数** 定义为所有满足以下条件 `i` 的数的平方和：

- `1 <= i <= n`
- `i * i` 的十进制表示的字符串可以分割成若干连续子字符串，且这些子字符串对应的整数值之和等于 `i` 。

**示例 1：**

```
输入：n = 10
输出：182
解释：总共有 3 个整数 i 满足要求：
- 1 ，因为 1 * 1 = 1
- 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
- 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
因此，10 的惩罚数为 1 + 81 + 100 = 182

```

**示例 2：**

```
输入：n = 37
输出：1478
解释：总共有 4 个整数 i 满足要求：
- 1 ，因为 1 * 1 = 1
- 9 ，因为 9 * 9 = 81 ，且 81 可以分割成 8 + 1 。
- 10 ，因为 10 * 10 = 100 ，且 100 可以分割成 10 + 0 。
- 36 ，因为 36 * 36 = 1296 ，且 1296 可以分割成 1 + 29 + 6 。
因此，37 的惩罚数为 1 + 81 + 100 + 1296 = 1478

```

**提示：**

- `1 <= n <= 1000`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/solutions/2277792/yu-chu-li-hui-su-by-endlesscheng-ro3s/
# 预处理 + 回溯
PRE_SUM = [0] * 1001  # 预处理
for i in range(1, 1001):
    s = str(i * i)
    n = len(s)

    def dfs(p: int, sum: int) -> bool:
        if p == n:  # 递归终点
            return sum == i  # i 是惩罚数
        x = 0
        for j in range(p, n):  # 从 s[p] 到 s[j] 组成的子串
            x = x * 10 + int(s[j])  # 对应的整数值
            if dfs(j + 1, sum + x):
                return True
        return False

    PRE_SUM[i] = PRE_SUM[i - 1] + (i * i if dfs(0, 0) else 0)


class Solution:
    def punishmentNumber1(self, n: int) -> int:
        @cache
        def dfs(i, c, s):
            if c == int(s[i:]):
                return True
            for j in range(i + 1, len(s)):
                nc = int(s[i:j])
                if nc <= c and dfs(j, c - nc, s):
                    return True
                elif nc > c:
                    break

            return False

        ans = 0
        for i in range(n + 1):
            if dfs(0, i, str(i * i)):
                ans += i * i
        return ans

    def punishmentNumber(self, n: int) -> int:
        return PRE_SUM[n]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().punishmentNumber(n)

    print("\noutput:", serialize(ans))
