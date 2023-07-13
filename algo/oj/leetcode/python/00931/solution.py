# Created by shiyang07ca at 2023/07/13 10:02
# leetgo: dev
# https://leetcode.cn/problems/minimum-falling-path-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return min(matrix[0])
        pre = matrix[0]
        for row in matrix[1:]:
            new = [0] * n
            for j, x in enumerate(row):
                if j == 0:
                    new[j] = x + min(pre[j], pre[j + 1])
                elif j == n - 1:
                    new[j] = x + min(pre[j], pre[j - 1])
                else:
                    new[j] = x + min(pre[j - 1], pre[j], pre[j + 1])
            pre = new
        return min(pre)


# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minFallingPathSum(matrix)

    print("\noutput:", serialize(ans))
