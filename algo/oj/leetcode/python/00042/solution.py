# Created by shiyang07ca at 2023/07/23 08:47
# leetgo: dev
# https://leetcode.cn/problems/trapping-rain-water/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = left = pre_max = suf_max = 0
        right = len(height) - 1
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trap(height)

    print("\noutput:", serialize(ans))
