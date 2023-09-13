# Created by shiyang07ca at 2023/09/13 13:06
# leetgo: dev
# https://leetcode.cn/problems/check-knight-tour-configuration/

from itertools import *

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        pos = [0] * (n * n)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                pos[x] = (i, j)
        if pos[0] != (0, 0):
            return False
        for (x1, y1), (x2, y2) in pairwise(pos):
            if not (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) and not (
                abs(x1 - x2) == 1 and abs(y1 - y2) == 2
            ):
                return False

        return True


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().checkValidGrid(grid)

    print("\noutput:", serialize(ans))
