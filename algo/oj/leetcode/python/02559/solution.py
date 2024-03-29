# Created by shiyang07ca at 2023/06/02 00:16
# https://leetcode.cn/problems/count-vowel-strings-in-ranges/

"""
2559. 统计范围内的元音字符串数 (Medium)
给你一个下标从 **0** 开始的字符串数组 `words` 以及一个二维整数数组 `queries` 。

每个查询 `queries[i] = [lᵢ, rᵢ]` 会要求我们统计在 `words` 中下标在 `lᵢ` 到 `rᵢ` 范围内（ **包含** 这
两个值）并且以元音开头和结尾的字符串的数目。

返回一个整数数组，其中数组的第 `i` 个元素对应第 `i` 个查询的答案。

**注意：** 元音字母是 `'a'`、 `'e'`、 `'i'`、 `'o'` 和 `'u'` 。

**示例 1：**

```
输入：words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
输出：[2,3,0]
解释：以元音开头和结尾的字符串是 "aba"、"ece"、"aa" 和 "e" 。
查询 [0,2] 结果为 2（字符串 "aba" 和 "ece"）。
查询 [1,4] 结果为 3（字符串 "ece"、"aa"、"e"）。
查询 [1,1] 结果为 0 。
返回结果 [2,3,0] 。

```

**示例 2：**

```
输入：words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
输出：[3,2,1]
解释：每个字符串都满足这一条件，所以返回 [3,2,1] 。
```

**提示：**

- `1 <= words.length <= 10⁵`
- `1 <= words[i].length <= 40`
- `words[i]` 仅由小写英文字母组成
- `sum(words[i].length) <= 3 * 10⁵`
- `1 <= queries.length <= 10⁵`
- `0 <= queries[j][0] <= queries[j][1] < words.length`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        s = list(
            accumulate((w[0] in "aeiou" and w[-1] in "aeiou" for w in words), initial=0)
        )
        return [s[r + 1] - s[l] for l, r in queries]


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().vowelStrings(words, queries)

    print("\noutput:", serialize(ans))
