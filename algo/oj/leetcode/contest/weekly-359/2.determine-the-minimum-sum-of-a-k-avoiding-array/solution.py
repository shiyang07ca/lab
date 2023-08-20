# Created by shiyang07ca at 2023/08/20 13:23
# leetgo: dev
# https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/
# https://leetcode.cn/contest/weekly-contest-359/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        mem = set()
        i = ans = 0
        j = 1
        while i < n:
            if j not in mem:
                ans += j
                i += 1
            mem.add(k - j)
            j += 1

        return ans

    # 链接：https://leetcode.cn/problems/determine-the-minimum-sum-of-a-k-avoiding-array/solutions/2396408/o1-gong-shi-pythonjavacgo-by-endlesschen-cztk/
    def minimumSum2(self, n: int, k: int) -> int:
        m = min(k // 2, n)
        return (m * (m + 1) + (k * 2 + n - m - 1) * (n - m)) // 2


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumSum(n, k)

    print("\noutput:", serialize(ans))
