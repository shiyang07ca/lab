# Created by shiyang07ca at 2023/10/02 00:01
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        pre = prices[0]
        ans = 0
        for p in prices:
            if p > pre:
                ans += p - pre
            pre = p
        return ans

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0

            if hold:
                return max(dfs(i - 1, hold), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, hold), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
