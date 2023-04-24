# Created by shiyang07ca at 2023/04/24 22:17
# https://leetcode.cn/problems/last-substring-in-lexicographical-order/

"""
1163. 按字典序排在最后的子串 (Hard)
给你一个字符串 `s` ，找出它的所有子串并按字典序排列，返回排
在最后的那个子串。

**示例 1：**

```
输入：s = "abab"
输出："bab"
解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b",
"ba", "bab"]。按字典序排在最后的子串是 "bab"。

```

**示例 2：**

```
输入：s = "leetcode"
输出："tcode"

```

**提示：**

- `1 <= s.length <= 4 * 10⁵`
- `s` 仅含有小写英文字符。

"""

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lastSubstring(self, s: str) -> str:
        return max(s[i:] for i in range(len(s)))

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lastSubstring(s)
    print("output:", serialize(ans))
