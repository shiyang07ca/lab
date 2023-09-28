# Created by shiyang07ca at 2023/09/28 17:35
# leetgo: dev
# https://leetcode.cn/problems/number-of-flowers-in-full-bloom/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/number-of-flowers-in-full-bloom/description/
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        starts = sorted(s for s, _ in flowers)
        ends = sorted(e for _, e in flowers)
        return [bisect_right(starts, p) - bisect_left(ends, p) for p in people]


# @lc code=end

if __name__ == "__main__":
    flowers: List[List[int]] = deserialize("List[List[int]]", read_line())
    people: List[int] = deserialize("List[int]", read_line())
    ans = Solution().fullBloomFlowers(flowers, people)

    print("\noutput:", serialize(ans))
