# Created by shiyang07ca at 2023/07/20 12:55
# leetgo: dev
# https://leetcode.cn/problems/maximum-sum-circular-subarray/

from functools import lru_cache as cache

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        if n == 1:
            return nums[0]

        @cache
        def dfs(j):
            if j == 0:
                return nums[j]
            else:
                return min(nums[j], dfs(j - 1) + nums[j])

        @cache
        def dfs2(j):
            if j == 0:
                return nums[j]
            else:
                return max(nums[j], dfs2(j - 1) + nums[j])

        mi = min(dfs(i) for i in range(n))
        ma = max(dfs2(i) for i in range(n))
        if s - mi == 0:
            return ma
        else:
            return max(s - mi, ma, s)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubarraySumCircular(nums)

    print("\noutput:", serialize(ans))
