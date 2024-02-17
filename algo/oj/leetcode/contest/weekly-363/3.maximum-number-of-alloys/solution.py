# Created by shiyang07ca at 2023/09/17 10:30
# leetgo: dev
# https://leetcode.cn/problems/maximum-number-of-alloys/
# https://leetcode.cn/contest/weekly-contest-363/problems/maximum-number-of-alloys/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: binary search


class Solution:
    def maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: List[List[int]],
        stock: List[int],
        cost: List[int],
    ) -> int:
        def check(num):
            money = 0
            for s, base, c in zip(stock, com, cost):
                if s < base * num:  # 需要额外购买
                    money += (base * num - s) * c
                    if money > budget:
                        return False
            # return money <= budget
            return True

        ans = 0
        for com in composition:
            l, r = 0, 2 * 10**8
            while l < r:
                mid = (l + r + 1) >> 1
                if check(mid):
                    l = mid
                else:
                    r = mid - 1
            ans = max(ans, l)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    budget: int = deserialize("int", read_line())
    composition: List[List[int]] = deserialize("List[List[int]]", read_line())
    stock: List[int] = deserialize("List[int]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)

    print("\noutput:", serialize(ans))
