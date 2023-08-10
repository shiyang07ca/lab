# Created by shiyang07ca at 2023/08/06 15:42
# leetgo: dev
# https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/
# https://leetcode.cn/contest/weekly-contest-357/problems/maximum-elegance-of-a-k-length-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: 反悔贪心, greedy


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/solutions/2375128/fan-hui-tan-xin-pythonjavacgo-by-endless-v2w1/
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda i: -i[0])  # 把利润从大到小排序
        ans = total_profit = 0
        vis = set()
        duplicate = []  # 重复类别的利润
        for i, (profit, category) in enumerate(items):
            if i < k:
                total_profit += profit
                if category not in vis:
                    vis.add(category)
                else:  # 重复类别
                    duplicate.append(profit)
            elif duplicate and category not in vis:
                vis.add(category)
                total_profit += profit - duplicate.pop()  # 用最小利润替换
            # else: 比前面的利润小，而且类别还重复了，选它只会让 total_profit 变小，len(vis) 不变，优雅度不会变大
            ans = max(ans, total_profit + len(vis) * len(vis))
        return ans


# @lc code=end

if __name__ == "__main__":
    items: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaximumElegance(items, k)

    print("\noutput:", serialize(ans))
