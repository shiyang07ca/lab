# Created by shiyang07ca at 2023/07/09 17:31
# leetgo: dev
# https://leetcode.cn/problems/longest-non-decreasing-subarray-from-two-arrays/
# https://leetcode.cn/contest/weekly-contest-353/problems/longest-non-decreasing-subarray-from-two-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums = (nums1, nums2)

        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return 1
            res = 1
            if nums1[i - 1] <= nums[j][i]:
                res = dfs(i - 1, 0) + 1
            if nums2[i - 1] <= nums[j][i]:
                res = max(res, dfs(i - 1, 1) + 1)
            return res

        return max(dfs(i, j) for j in range(2) for i in range(len(nums1)))

    # f[i][j] = max(1, f[i-1][0] + 1, f[i-1][1] + 1)
    def maxNonDecreasingLength2(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums = (nums1, nums2)
        f = [[1, 1] for _ in range(n)]
        for i in range(1, n):
            for j in range(2):
                if nums1[i - 1] <= nums[j][i]:
                    f[i][j] = f[i - 1][0] + 1
                if nums2[i - 1] <= nums[j][i]:
                    f[i][j] = max(f[i][j], f[i - 1][1] + 1)
        return max(map(max, f))


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNonDecreasingLength(nums1, nums2)

    print("\noutput:", serialize(ans))
