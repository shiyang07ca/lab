# Created by shiyang07ca at 2023/05/28 16:57
# https://leetcode.cn/problems/remove-trailing-zeros-from-a-string/
# https://leetcode.cn/contest/weekly-contest-347/problems/remove-trailing-zeros-from-a-string/

"""
6457. 移除字符串中的尾随零 (Easy)
给你一个用字符串表示的正整数 `num` ，请你以字符串形式返回不含尾随零的整数 `num`。

**示例 1：**

```
输入：num = "51230100"
输出："512301"
解释：整数 "51230100" 有 2 个尾随零，移除并返回整数 "512301" 。

```

**示例 2：**

```
输入：num = "123"
输出："123"
解释：整数 "123" 不含尾随零，返回整数 "123" 。

```

**提示：**

- `1 <= num.length <= 1000`
- `num` 仅由数字 `0` 到 `9` 组成
- `num` 不含前导零

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")


# @lc code=end

if __name__ == "__main__":
    num: str = deserialize("str", read_line())
    ans = Solution().removeTrailingZeros(num)

    print("\noutput:", serialize(ans))
