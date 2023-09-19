# Created by shiyang07ca at 2023/09/18 08:26
# leetgo: dev
# https://leetcode.cn/problems/house-robber-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: binary search, dp


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mx):
            d0 = d1 = 0
            for n in nums:
                if n > mx:
                    d0 = d1
                else:
                    d0, d1 = d1, max(d0 + 1, d1)
            return d1

        l, r = 0, max(nums)
        while l < r:
            mid = (l + r) >> 1
            if check(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minCapability(nums, k)

    print("\noutput:", serialize(ans))
