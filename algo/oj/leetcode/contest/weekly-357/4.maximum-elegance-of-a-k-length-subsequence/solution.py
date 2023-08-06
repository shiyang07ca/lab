# Created by shiyang07ca at 2023/08/06 15:42
# leetgo: dev
# https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/
# https://leetcode.cn/contest/weekly-contest-357/problems/maximum-elegance-of-a-k-length-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        pass


# @lc code=end

if __name__ == "__main__":
    items: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaximumElegance(items, k)

    print("\noutput:", serialize(ans))
