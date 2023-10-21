# Created by shiyang07ca at 2023/10/22 00:20
# leetgo: dev
# https://leetcode.cn/problems/reducing-dishes/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxSatisfaction(self, sati: List[int]) -> int:
        sati.sort()
        n = len(sati)
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = sati[i] + suf[i + 1]
        ans = 0
        for i in range(n):
            ans += (i + 1) * sati[i]
        for i in range(n):
            ans = max(ans, ans - suf[i])

        return max(ans, 0)


# @lc code=end

if __name__ == "__main__":
    satisfaction: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSatisfaction(satisfaction)

    print("\noutput:", serialize(ans))
