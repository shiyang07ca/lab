# Created by shiyang07ca at 2023/07/09 17:31
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-of-jumps-to-reach-the-last-index/
# https://leetcode.cn/contest/weekly-contest-353/problems/maximum-number-of-jumps-to-reach-the-last-index/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp


class Solution:
    def maximumJumps1(self, nums: List[int], t: int) -> int:
        n = len(nums)

        @cache
        def dfs(j):
            if j == 0:
                return 0
            res = -inf
            for i in range(j):
                if -t <= nums[j] - nums[i] <= t:
                    res = max(res, dfs(i) + 1)
            return res

        ans = dfs(n - 1)
        return -1 if ans <= 0 else ans

    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [-inf] * n
        f[0] = 0
        for i in range(1, n):
            for j in range(i):
                if -target <= nums[i] - nums[j] <= target:
                    f[i] = max(f[i], f[j] + 1)
        return -1 if f[-1] < 0 else f[-1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().maximumJumps(nums, target)

    print("\noutput:", serialize(ans))
