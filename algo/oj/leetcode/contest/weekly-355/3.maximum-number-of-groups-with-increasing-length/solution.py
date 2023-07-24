# Created by shiyang07ca at 2023/07/23 15:06
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-of-groups-with-increasing-length/
# https://leetcode.cn/contest/weekly-contest-355/problems/maximum-number-of-groups-with-increasing-length/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        pass


# @lc code=end

if __name__ == "__main__":
    usageLimits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxIncreasingGroups(usageLimits)

    print("\noutput:", serialize(ans))
