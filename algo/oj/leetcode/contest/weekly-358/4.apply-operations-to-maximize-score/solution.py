# Created by shiyang07ca at 2023/08/13 10:32
# leetgo: dev
# https://leetcode.cn/problems/apply-operations-to-maximize-score/
# https://leetcode.cn/contest/weekly-contest-358/problems/apply-operations-to-maximize-score/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:

# 链接：https://leetcode.cn/circle/discuss/9wQ08W/view/4drty4/
maxi = 10**5
score = [0] * (maxi + 1)
for i in range(2, maxi + 1):
    if not score[i]:
        for j in range(i, maxi + 1, i):
            score[j] += 1

mod = 10**9 + 7


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        note = [score[x] for x in nums]  # 不一定要创建数组，可以直接在后面调用的时候去查；这里为了更直观地展示
        n = len(nums)

        # 单调栈可以设定一个哨兵元素
        left = [None] * n
        stack = [(-1, inf)]
        for i in range(n):
            while stack[-1][1] < note[i]:
                stack.pop()
            left[i] = stack[-1][0]
            stack.append((i, note[i]))

        right = [None] * n
        stack = [(n, inf)]
        for i in range(n - 1, -1, -1):
            while stack[-1][1] <= note[i]:
                stack.pop()
            right[i] = stack[-1][0]
            stack.append((i, note[i]))

        counts = [(right[i] - i) * (i - left[i]) for i in range(n)]
        ans = 1
        for i in sorted(range(n), key=lambda x: -nums[x]):
            if k < counts[i]:
                ans *= pow(nums[i], k, mod)
                ans %= mod
                break
            else:
                ans *= pow(nums[i], counts[i], mod)
                ans %= mod
                k -= counts[i]

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumScore(nums, k)

    print("\noutput:", serialize(ans))
