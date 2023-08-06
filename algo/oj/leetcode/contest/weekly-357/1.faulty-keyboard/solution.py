# Created by shiyang07ca at 2023/08/06 15:42
# leetgo: dev
# https://leetcode.cn/problems/faulty-keyboard/
# https://leetcode.cn/contest/weekly-contest-357/problems/faulty-keyboard/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for c in s:
            if c == "i":
                ans = ans[::-1]
            else:
                ans.append(c)
        return "".join(ans)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().finalString(s)

    print("\noutput:", serialize(ans))
