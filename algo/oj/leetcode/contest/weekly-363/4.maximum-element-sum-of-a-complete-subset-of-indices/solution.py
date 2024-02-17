# Created by shiyang07ca at 2023/09/17 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-element-sum-of-a-complete-subset-of-indices/
# https://leetcode.cn/contest/weekly-contest-363/problems/maximum-element-sum-of-a-complete-subset-of-indices/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: math

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSum(nums)

    print("\noutput:", serialize(ans))
