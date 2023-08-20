# Created by shiyang07ca at 2023/08/20 13:23
# leetgo: dev
# https://leetcode.cn/problems/check-if-a-string-is-an-acronym-of-words/
# https://leetcode.cn/contest/weekly-contest-359/problems/check-if-a-string-is-an-acronym-of-words/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i, w in enumerate(words):
            if s[i] != w[0]:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().isAcronym(words, s)

    print("\noutput:", serialize(ans))
