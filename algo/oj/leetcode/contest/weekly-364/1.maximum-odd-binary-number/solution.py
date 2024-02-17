# Created by shiyang07ca at 2023/09/24 10:33
# leetgo: dev
# https://leetcode.cn/problems/maximum-odd-binary-number/
# https://leetcode.cn/contest/weekly-contest-364/problems/maximum-odd-binary-number/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        c1 = s.count("1")
        return "1" * (c1 - 1) + "0" * (n - c1) + "1"


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maximumOddBinaryNumber(s)

    print("\noutput:", serialize(ans))
