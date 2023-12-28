# Created by shiyang07ca at 2023/12/28 10:41
# leetgo: dev
# https://leetcode.cn/problems/collecting-chocolates/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/collecting-chocolates/solutions/2582444/python3javacgorust-yi-ti-yi-jie-mei-ju-q-y3b3/
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        for i, v in enumerate(nums):
            f[i][0] = v
            for j in range(1, n):
                f[i][j] = min(f[i][j - 1], nums[(i - j) % n])
        return min(sum(f[i][j] for i in range(n)) + x * j for j in range(n))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minCost(nums, x)

    print("\noutput:", serialize(ans))
