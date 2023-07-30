# Created by shiyang07ca at 2023/07/30 10:34
# leetgo: dev
# https://leetcode.cn/problems/count-complete-subarrays-in-an-array/
# https://leetcode.cn/contest/weekly-contest-356/problems/count-complete-subarrays-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# TOOD


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        m = len(set(nums))
        ans = 0
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                if len(s) == m:
                    ans += 1
        return ans

    # 链接：https://leetcode.cn/problems/count-complete-subarrays-in-an-array/solutions/2364671/on-hua-dong-chuang-kou-by-endlesscheng-9ztb/
    def countCompleteSubarrays2(self, nums: List[int]) -> int:
        m = len(set(nums))
        cnt = Counter()
        ans = left = 0
        for v in nums:  # 枚举子数组右端点 v=nums[i]
            cnt[v] += 1
            while len(cnt) == m:
                x = nums[left]
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
                left += 1
            ans += left  # 子数组左端点 < left 的都是合法的
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countCompleteSubarrays(nums)

    print("\noutput:", serialize(ans))
