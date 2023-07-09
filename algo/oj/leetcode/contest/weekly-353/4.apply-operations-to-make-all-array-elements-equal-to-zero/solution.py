# Created by shiyang07ca at 2023/07/09 17:31
# leetgo: dev
# https://leetcode.cn/problems/apply-operations-to-make-all-array-elements-equal-to-zero/
# https://leetcode.cn/contest/weekly-contest-353/problems/apply-operations-to-make-all-array-elements-equal-to-zero/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: greedy

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        # 计算差分数组
        d = [0] * (n + 1)
        d[0] = nums[0]
        d[n] = -nums[n - 1]
        for i in range(1, n):
            d[i] = nums[i] - nums[i - 1]
        # 从左到右对差分数组里的每个元素进行操作
        for i in range(n - k + 1):
            if d[i] > 0:
                d[i + k] += d[i]
                d[i] = 0
        # 检查差分数组中是否所有元素均为 0
        for i in range(n):
            if d[i] != 0:
                return False
        return True


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().checkArray(nums, k)

    print("\noutput:", serialize(ans))
