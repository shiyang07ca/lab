# Created by shiyang07ca at 2023/05/03 11:36
# https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions/

"""
1003. 检查替换后的词是否有效 (Medium)
给你一个字符串 `s` ，请你判断它是否 **有效** 。

字符串 `s` **有效** 需要满足：假设开始有一个空字符串 `t = ""
` ，你可以执行 **任意次** 下述操作将 `t` **转换为** `s` ：

- 将字符串 `"abc"` 插入到 `t` 中的任意位置。形式上， `t` 变
为 `tₗₑfₜ + "abc" + trᵢgₕₜ`，其中 `t == tₗₑfₜ + trᵢgₕₜ` 。注
意， `tₗₑfₜ` 和 `trᵢgₕₜ` 可能为 **空** 。

如果字符串 `s` 有效，则返回 `true`；否则，返回 `false`。

**示例 1：**

```
输入：s = "aabcbc"
输出：true
解释：
"" -> "abc" -> "aabcbc"
因此，"aabcbc" 有效。
```

**示例 2：**

```
输入：s = "abcabcababcc"
输出：true
解释：
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
因此，"abcabcababcc" 有效。
```

**示例 3：**

```
输入：s = "abccba"
输出：false
解释：执行操作无法得到 "abccba" 。
```

**提示：**

- `1 <= s.length <= 2 * 10⁴`
- `s` 由字母 `'a'`、 `'b'` 和 `'c'` 组成

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 3 != 0:
            return False

        while s:
            i = s.find("abc")
            if i == -1 or len(s) == 3 and s != "abc":
                return False
            s = s[:i] + s[i + 3 :]
        return True


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)
    print("output:", serialize(ans))
