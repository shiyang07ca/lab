# Created by shiyang07ca at 2023/10/15 18:02
# leetgo: dev
# https://leetcode.cn/problems/single-number-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        nums.sort()
        for i in range(0, n - 1, 3):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            cnt = Counter([a, b, c])
            for x, c in cnt.items():
                if c == 1:
                    return x

        return nums[n - 1]


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)

    print("\noutput:", serialize(ans))
