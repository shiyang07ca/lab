# Created by shiyang07ca at 2023/10/29 08:25
# leetgo: dev
# https://leetcode.cn/problems/h-index/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations, start=1):
            if c < i:
                return i - 1
        return len(citations)


# @lc code=end

if __name__ == "__main__":
    citations: List[int] = deserialize("List[int]", read_line())
    ans = Solution().hIndex(citations)

    print("\noutput:", serialize(ans))
