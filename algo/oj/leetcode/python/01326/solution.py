# Created by shiyang07ca at 2025/01/05 15:05
# leetgo: 1.4.13
# https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/

from typing import *

from leetgo_py import *

# @lc code=begin

# tag: greedy, dynamic-programming

# TODO:


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # 链接：https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/solutions/2123855/yi-zhang-tu-miao-dong-pythonjavacgo-by-e-wqry/

        right_most = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(i - r, 0)
            right_most[left] = max(right_most[left], i + r)

        ans = 0
        cur_right = 0  # 已建造的桥的右端点
        next_right = 0  # 下一座桥的右端点的最大值
        for i in range(n):  # 如果走到 n-1 时没有返回 -1，那么必然可以到达 n
            next_right = max(next_right, right_most[i])
            if i == cur_right:  # 到达已建造的桥的右端点
                if i == next_right:  # 无论怎么造桥，都无法从 i 到 i+1
                    return -1
                cur_right = next_right  # 造一座桥
                ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ranges: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minTaps(n, ranges)
    print("\noutput:", serialize(ans, "integer"))
