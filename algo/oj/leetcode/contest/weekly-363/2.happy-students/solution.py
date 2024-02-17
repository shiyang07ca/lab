# Created by shiyang07ca at 2023/09/17 10:30
# leetgo: dev
# https://leetcode.cn/problems/happy-students/
# https://leetcode.cn/contest/weekly-contest-363/problems/happy-students/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: greedy


class Solution:
    # 链接：https://leetcode.cn/circle/discuss/SwCGEn/view/Ukiom8/
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] > 0  # 一个都不选
        for i, (x, y) in enumerate(pairwise(nums)):
            if x < i + 1 < y:
                ans += 1
        return ans + 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countWays(nums)

    print("\noutput:", serialize(ans))
