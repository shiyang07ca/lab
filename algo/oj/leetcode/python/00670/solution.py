# Created by shiyang07ca at 2024/01/22 12:38
# leetgo: dev
# https://leetcode.cn/problems/maximum-swap/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = []
        while num:
            nums.insert(0, num % 10)
            num //= 10

        sns = sorted(nums, reverse=True)
        ans = nums
        for i, n in enumerate(nums):
            if sns[i] != n:
                ans[i] = sns[i]
                for j in range(len(nums) - 1, i, -1):
                    if sns[i] == ans[j]:
                        ans[j] = n
                        print(ans)
                        return int("".join(str(n) for n in ans))
        return int("".join(str(n) for n in ans))


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().maximumSwap(num)

    print("\noutput:", serialize(ans))
