# Created by shiyang07ca at 2023/08/18 13:21
# leetgo: dev
# https://leetcode.cn/problems/pizza-with-3n-slices/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/pizza-with-3n-slices/solutions/2393650/python3javacgotypescript-yi-ti-yi-jie-do-mhhj/
    def maxSizeSlices(self, slices: List[int]) -> int:
        def g(nums: List[int]) -> int:
            m = len(nums)
            f = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    f[i][j] = max(
                        f[i - 1][j], (f[i - 2][j - 1] if i >= 2 else 0) + nums[i - 1]
                    )
            return f[m][n]

        n = len(slices) // 3
        a, b = g(slices[:-1]), g(slices[1:])
        return max(a, b)


# @lc code=end

if __name__ == "__main__":
    slices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSizeSlices(slices)

    print("\noutput:", serialize(ans))
