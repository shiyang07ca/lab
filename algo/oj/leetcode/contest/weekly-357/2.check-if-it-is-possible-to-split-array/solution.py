# Created by shiyang07ca at 2023/08/06 15:42
# leetgo: dev
# https://leetcode.cn/problems/check-if-it-is-possible-to-split-array/
# https://leetcode.cn/contest/weekly-contest-357/problems/check-if-it-is-possible-to-split-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        acc = list(accumulate(nums, initial=0))

        # [l, r)
        # [l, i), [i, r)
        @cache
        def dfs(l, r):
            if r - l == 1:
                return True

            for i in range(l, r):
                left = acc[i] - acc[l]
                right = acc[r] - acc[i]
                if i - l == 1 and r - i == 1:
                    return True
                elif i - l == 1 and right >= m:
                    if dfs(i, r):
                        return True
                elif r - i == 1 and left >= m:
                    if dfs(l, i):
                        return True
                elif left >= m and right >= m:
                    if dfs(l, i) and dfs(i, r):
                        return True
            return False

        return dfs(0, n)

    # 脑筋急转弯
    # 拆分过程中数组最短数组长度为 2。因此，只要有一组相邻和超过了 m，那么整个数
    # 组就都可以进行最终拆分
    def canSplitArray1(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        return n <= 2 or any(nums[i] + nums[i + 1] >= m for i in range(n - 1))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().canSplitArray(nums, m)

    print("\noutput:", serialize(ans))
