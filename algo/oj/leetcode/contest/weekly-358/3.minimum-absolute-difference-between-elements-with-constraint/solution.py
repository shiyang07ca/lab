# Created by shiyang07ca at 2023/08/13 10:32
# leetgo: dev
# https://leetcode.cn/problems/minimum-absolute-difference-between-elements-with-constraint/
# https://leetcode.cn/contest/weekly-contest-358/problems/minimum-absolute-difference-between-elements-with-constraint/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: binary search

# 链接：https://leetcode.cn/circle/discuss/9wQ08W/view/4drty4/
from sortedcontainers import *


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        stl = SortedList()
        n = len(nums)
        ans = inf
        for i in range(n):
            if i >= x:
                stl.add(nums[i - x])
                pos = stl.bisect_left(nums[i])
                # 查看二分位置的两边
                for j in range(pos - 1, pos + 1):
                    if 0 <= j < len(stl):
                        ans = min(ans, abs(nums[i] - stl[j]))
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().minAbsoluteDifference(nums, x)

    print("\noutput:", serialize(ans))
