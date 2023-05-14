# Created by shiyang07ca at 2023/05/14 10:30
# https://leetcode.cn/problems/neighboring-bitwise-xor/
# https://leetcode.cn/contest/weekly-contest-345/problems/neighboring-bitwise-xor/

"""
6431. 相邻值的按位异或 (Medium)
下标从 **0** 开始、长度为 `n` 的数组 `derived` 是由同样长度
为 `n` 的原始 **二进制数组** `original` 通过计算相邻值的 **
按位异或（⊕）** 派生而来。

特别地，对于范围 `[0, n - 1]` 内的每个下标 `i` ：

- 如果 `i = n - 1` ，那么 `derived[i] = original[i] ⊕ origin
al[0]`
- 否则 `derived[i] = original[i] ⊕ original[i + 1]`

给你一个数组 `derived` ，请判断是否存在一个能够派生得到 `der
ived` 的 **有效原始二进制数组** `original` 。

如果存在满足要求的原始二进制数组，返回 **true**；否则，返回*
*false**。

- 二进制数组是仅由 **0** 和 **1** 组成的数组。

**示例 1：**

```
输入：derived = [1,1,0]
输出：true
解释：能够派生得到 [1,1,0] 的有效原始二进制数组是 [0,1,0] ：
derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1
derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0

```

**示例 2：**

```
输入：derived = [1,1]
输出：true
解释：能够派生得到 [1,1] 的有效原始二进制数组是 [0,1] ：
derived[0] = original[0] ⊕ original[1] = 1
derived[1] = original[1] ⊕ original[0] = 1

```

**示例 3：**

```
输入：derived = [1,0]
输出：false
解释：不存在能够派生得到 [1,0] 的有效原始二进制数组。

```

**提示：**

- `n == derived.length`
- `1 <= n <= 10⁵`
- `derived` 中的值不是 **0** 就是 **1** 。

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        t = [0]
        for d in derived:
            t.append(d ^ t[-1])
        if t[-1] == t[0] and t[-1] ^ t[-2] == derived[-1]:
            return True

        t = [1]
        for d in derived:
            t.append(d ^ t[-1])
        if t[-1] == t[0] and t[-1] ^ t[-2] == derived[-1]:
            return True

        return False

    # 作者：灵茶山艾府
    # 链接：https://leetcode.cn/problems/neighboring-bitwise-xor/solutions/2269241/tui-gong-shi-by-endlesscheng-90t5/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def doesValidArrayExist2(self, derived: List[int]) -> bool:
        return reduce(xor, derived) == 0


# @lc code=end

if __name__ == "__main__":
    derived: List[int] = deserialize("List[int]", read_line())
    ans = Solution().doesValidArrayExist(derived)
    print("output:", serialize(ans))
