# Created by shiyang07ca at 2024/06/09 21:55
# leetgo: dev
# https://leetcode.cn/problems/burst-balloons/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/burst-balloons/solutions/2805284/python3javacgotypescript-yi-ti-yi-jie-do-ptf8/
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] + nums + [1]
        f = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j])
        return f[0][-1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxCoins(nums)
    print("\noutput:", serialize(ans, "integer"))
