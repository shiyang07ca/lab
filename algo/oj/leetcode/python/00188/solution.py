# Created by shiyang07ca at 2023/10/04 20:48
# leetgo: dev
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/2201488/shi-pin-jiao-ni-yi-bu-bu-si-kao-dong-tai-kksg/
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i: int, j: int, hold: bool) -> int:
            if j < 0:
                return -inf
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j - 1, False) - prices[i])
            return max(dfs(i - 1, j, False), dfs(i - 1, j, True) + prices[i])

        return dfs(n - 1, k, False)


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(k, prices)

    print("\noutput:", serialize(ans))
