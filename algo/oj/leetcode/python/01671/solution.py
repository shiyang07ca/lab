# Created by shiyang07ca at 2023/12/22 11:57
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/solutions/2575540/python3javacgorust-yi-ti-yi-jie-dong-tai-wtkr/?envType=daily-question&envId=2023-12-22
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        return n - max(a + b - 1 for a, b in zip(left, right) if a > 1 and b > 1)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumMountainRemovals(nums)

    print("\noutput:", serialize(ans))
