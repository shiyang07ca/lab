# Created by shiyang07ca at 2023/07/23 15:06
# leetgo: dev
# https://leetcode.cn/problems/split-strings-by-separator/
# https://leetcode.cn/contest/weekly-contest-355/problems/split-strings-by-separator/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for w in words:
            ans.extend(t for t in w.split(separator) if t)
        return ans


# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    separator: str = deserialize("str", read_line())
    ans = Solution().splitWordsBySeparator(words, separator)

    print("\noutput:", serialize(ans))
