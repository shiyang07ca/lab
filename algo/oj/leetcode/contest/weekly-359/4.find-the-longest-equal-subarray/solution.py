# Created by shiyang07ca at 2023/08/20 13:23
# leetgo: dev
# https://leetcode.cn/problems/find-the-longest-equal-subarray/
# https://leetcode.cn/contest/weekly-contest-359/problems/find-the-longest-equal-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: two pointer; sliding window; 双指针; 同向双指针; 滑动窗口;


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pos = [[] for _ in range(len(nums) + 1)]
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = 0
        for ps in pos:
            left = 0
            for right, p in enumerate(ps):
                while (p - ps[left] + 1) - (right - left + 1) > k:
                    left += 1
                ans = max(ans, right - left + 1)

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().longestEqualSubarray(nums, k)

    print("\noutput:", serialize(ans))
