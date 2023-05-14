# Created by shiyang07ca at 2023/05/14 10:30
# https://leetcode.cn/problems/find-the-losers-of-the-circular-game/
# https://leetcode.cn/contest/weekly-contest-345/problems/find-the-losers-of-the-circular-game/

"""
6430. 找出转圈游戏输家 (Easy)
`n` 个朋友在玩游戏。这些朋友坐成一个圈，按 **顺时针方向** 从
`1` 到 `n` 编号。从第 `i` 个朋友的位置开始顺时针移动 `1` 步
会到达第 `(i + 1)` 个朋友的位置（ `1 <= i < n`），而从第 `n`
个朋友的位置开始顺时针移动 `1` 步会回到第 `1` 个朋友的位置。

游戏规则如下：

第 `1` 个朋友接球。

- 接着，第 `1` 个朋友将球传给距离他顺时针方向 `k` 步的朋友。
- 然后，接球的朋友应该把球传给距离他顺时针方向 `2 * k` 步的
朋友。
- 接着，接球的朋友应该把球传给距离他顺时针方向 `3 * k` 步的
朋友，以此类推。

换句话说，在第 `i` 轮中持有球的那位朋友需要将球传递给距离他
顺时针方向 `i * k` 步的朋友。

当某个朋友第 2 次接到球时，游戏结束。

在整场游戏中没有接到过球的朋友是 **输家** 。

给你参与游戏的朋友数量 `n` 和一个整数 `k` ，请按升序排列返回
包含所有输家编号的数组 `answer` 作为答案。

**示例 1：**

```
输入：n = 5, k = 2
输出：[4,5]
解释：以下为游戏进行情况：
1）第 1 个朋友接球，第 1 个朋友将球传给距离他顺时针方向 2 步
的玩家 —— 第 3 个朋友。
2）第 3 个朋友将球传给距离他顺时针方向 4 步的玩家 —— 第 2 个
朋友。
3）第 2 个朋友将球传给距离他顺时针方向 6 步的玩家 —— 第 3 个
朋友。
4）第 3 个朋友接到两次球，游戏结束。

```

**示例 2：**

```
输入：n = 4, k = 4
输出：[2,3,4]
解释：以下为游戏进行情况：
1）第 1 个朋友接球，第 1 个朋友将球传给距离他顺时针方向 4 步
的玩家 —— 第 1 个朋友。
2）第 1 个朋友接到两次球，游戏结束。
```

**提示：**

- `1 <= k <= n <= 50`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        p = set()
        i = j = 0
        while j not in p:
            i += 1
            p.add(j)
            j = (j + i * k) % n
        return [i + 1 for i in range(n) if i not in p]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().circularGameLosers(n, k)
    print("output:", serialize(ans))
