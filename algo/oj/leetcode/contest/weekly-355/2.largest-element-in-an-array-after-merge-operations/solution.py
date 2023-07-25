# Created by shiyang07ca at 2023/07/25 22:58
# leetgo: dev
# https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/
# https://leetcode.cn/contest/weekly-contest-355/problems/largest-element-in-an-array-after-merge-operations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        i = n - 1
        ans = nums[0]
        while i > 0:
            t = nums[i]
            while i > 0 and nums[i - 1] <= t:
                t += nums[i - 1]
                i -= 1
            ans = max(ans, t)
            i -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArrayValue(nums)

    print("\noutput:", serialize(ans))
