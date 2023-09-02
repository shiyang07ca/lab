# Created by shiyang07ca at 2023/09/03 00:47
# leetgo: dev
# https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ans = 0
        time = [math.ceil(d / s) for d, s in zip(dist, speed)]
        heapify(time)
        while time and time[0] > ans:
            heappop(time)
            ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    dist: List[int] = deserialize("List[int]", read_line())
    speed: List[int] = deserialize("List[int]", read_line())
    ans = Solution().eliminateMaximum(dist, speed)

    print("\noutput:", serialize(ans))
