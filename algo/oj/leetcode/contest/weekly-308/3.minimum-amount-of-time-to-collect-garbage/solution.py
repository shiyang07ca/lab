# Created by shiyang07ca at 2023/07/29 19:41
# leetgo: dev
# https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/
# https://leetcode.cn/contest/weekly-contest-308/problems/minimum-amount-of-time-to-collect-garbage/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

# @lc code=end

if __name__ == "__main__":
    garbage: List[str] = deserialize("List[str]", read_line())
    travel: List[int] = deserialize("List[int]", read_line())
    ans = Solution().garbageCollection(garbage, travel)

    print("\noutput:", serialize(ans))
