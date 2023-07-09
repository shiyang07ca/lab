# Created by shiyang07ca at 2023/07/09 17:31
# leetgo: dev
# https://leetcode.cn/problems/find-the-maximum-achievable-number/
# https://leetcode.cn/contest/weekly-contest-353/problems/find-the-maximum-achievable-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + 2 * t


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    t: int = deserialize("int", read_line())
    ans = Solution().theMaximumAchievableX(num, t)

    print("\noutput:", serialize(ans))
