# Created by shiyang07ca at 2024/06/10 23:57
# leetgo: dev
# https://leetcode.cn/problems/boats-to-save-people/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/boats-to-save-people/solutions/958838/jiu-sheng-ting-by-leetcode-solution-0nsp/
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        light, heavy = 0, len(people) - 1
        while light <= heavy:
            if people[light] + people[heavy] > limit:
                heavy -= 1
            else:
                light += 1
                heavy -= 1
            ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    people: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().numRescueBoats(people, limit)
    print("\noutput:", serialize(ans, "integer"))
