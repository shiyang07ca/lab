# Created by shiyang07ca at 2023/07/30 10:34
# leetgo: dev
# https://leetcode.cn/problems/number-of-employees-who-met-the-target/
# https://leetcode.cn/contest/weekly-contest-356/problems/number-of-employees-who-met-the-target/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for h in hours if h >= target)


# @lc code=end

if __name__ == "__main__":
    hours: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numberOfEmployeesWhoMetTarget(hours, target)

    print("\noutput:", serialize(ans))
