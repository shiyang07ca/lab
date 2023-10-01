# Created by shiyang07ca at 2023/10/02 00:01
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = prices[0]
        ans = 0
        for p in prices:
            if p > pre:
                ans += p - pre
            pre = p
        return ans


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)

    print("\noutput:", serialize(ans))
