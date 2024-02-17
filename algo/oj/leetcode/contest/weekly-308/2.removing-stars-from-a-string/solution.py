# Created by shiyang07ca at 2023/07/29 19:41
# leetgo: dev
# https://leetcode.cn/problems/removing-stars-from-a-string/
# https://leetcode.cn/contest/weekly-contest-308/problems/removing-stars-from-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeStars(self, s: str) -> str:

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removeStars(s)

    print("\noutput:", serialize(ans))
