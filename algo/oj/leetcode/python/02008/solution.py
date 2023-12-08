# Created by shiyang07ca at 2023/12/08 21:37
# leetgo: dev
# https://leetcode.cn/problems/maximum-earnings-from-taxi/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/maximum-earnings-from-taxi/
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        groups = defaultdict(list)
        for start, end, tip in rides:
            groups[end].append((start, end - start + tip))

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            if i == 1:
                return 0
            return max(dfs(i - 1), max((dfs(s) + t for s, t in groups[i]), default=0))

        return dfs(n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    rides: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxTaxiEarnings(n, rides)

    print("\noutput:", serialize(ans))
