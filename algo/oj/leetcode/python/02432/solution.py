# Created by shiyang07ca at 2023/05/05 09:02
# https://leetcode.cn/problems/the-employee-that-worked-on-the-longest-task/

"""
2432. 处理用时最长的那个任务的员工 (Easy)
共有 `n` 位员工，每位员工都有一个从 `0` 到 `n - 1` 的唯一 id
。

给你一个二维整数数组 `logs` ，其中 `logs[i] = [idᵢ, leaveTim
eᵢ]` ：

- `idᵢ` 是处理第 `i` 个任务的员工的 id ，且
- `leaveTimeᵢ` 是员工完成第 `i` 个任务的时刻。所有 `leaveTim
eᵢ` 的值都是 **唯一** 的。

注意，第 `i` 个任务在第 `(i - 1)` 个任务结束后立即开始，且第
`0` 个任务从时刻 `0` 开始。

返回处理用时最长的那个任务的员工的 id 。如果存在两个或多个员
工同时满足，则返回几人中 **最小** 的 id 。

**示例 1：**

```
输入：n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]
输出：1
解释：
任务 0 于时刻 0 开始，且在时刻 3 结束，共计 3 个单位时间。
任务 1 于时刻 3 开始，且在时刻 5 结束，共计 2 个单位时间。
任务 2 于时刻 5 开始，且在时刻 9 结束，共计 4 个单位时间。
任务 3 于时刻 9 开始，且在时刻 15 结束，共计 6 个单位时间。
时间最长的任务是任务 3 ，而 id 为 1 的员工是处理此任务的员工
，所以返回 1 。

```

**示例 2：**

```
输入：n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]
输出：3
解释：
任务 0 于时刻 0 开始，且在时刻 1 结束，共计 1 个单位时间。
任务 1 于时刻 1 开始，且在时刻 7 结束，共计 6 个单位时间。
任务 2 于时刻 7 开始，且在时刻 12 结束，共计 5 个单位时间。
任务 3 于时刻 12 开始，且在时刻 17 结束，共计 5 个单位时间。
时间最长的任务是任务 1 ，而 id 为 3 的员工是处理此任务的员工
，所以返回 3 。

```

**示例 3：**

```
输入：n = 2, logs = [[0,10],[1,20]]
输出：0
解释：
任务 0 于时刻 0 开始，且在时刻 10 结束，共计 10 个单位时间。
任务 1 于时刻 10 开始，且在时刻 20 结束，共计 10 个单位时间
。
时间最长的任务是任务 0 和 1 ，处理这两个任务的员工的 id 分别
是 0 和 1 ，所以返回最小的 0 。

```

**提示：**

- `2 <= n <= 500`
- `1 <= logs.length <= 500`
- `logs[i].length == 2`
- `0 <= idᵢ <= n - 1`
- `1 <= leaveTimeᵢ <= 500`
- `idᵢ != idᵢ + ₁`
- `leaveTimeᵢ` 按严格递增顺序排列

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        start = 0
        ans, ma = logs[0][0], logs[0][1]
        for i, end in logs:
            if end - start == ma:
                ans = min(ans, i)
            elif end - start > ma:
                ans = i
                ma = end - start
            start = end

        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    logs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().hardestWorker(n, logs)
    print("output:", serialize(ans))
