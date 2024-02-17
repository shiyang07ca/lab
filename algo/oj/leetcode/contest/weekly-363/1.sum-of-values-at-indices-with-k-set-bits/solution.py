# Created by shiyang07ca at 2023/09/17 10:30
# leetgo: dev
# https://leetcode.cn/problems/sum-of-values-at-indices-with-k-set-bits/
# https://leetcode.cn/contest/weekly-contest-363/problems/sum-of-values-at-indices-with-k-set-bits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, x in enumerate(nums):
            if i.bit_count() == k:
                ans += x
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().sumIndicesWithKSetBits(nums, k)

    print("\noutput:", serialize(ans))
