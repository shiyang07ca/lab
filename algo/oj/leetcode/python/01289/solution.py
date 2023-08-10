# Created by shiyang07ca at 2023/08/10 10:04
# leetgo: dev
# https://leetcode.cn/problems/minimum-falling-path-sum-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cur = grid[0][:]
        pre = grid[0][:]
        for row in grid[1:]:
            for i in range(n):
                cur[i] = row[i] + min(*pre[:i], *pre[i + 1 :])
            pre = cur[:]
        return min(cur)


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minFallingPathSum(grid)

    print("\noutput:", serialize(ans))
