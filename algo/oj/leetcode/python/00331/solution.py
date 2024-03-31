# Created by shiyang07ca at 2024/03/31 21:03
# leetgo: dev
# https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/verify-preorder-serialization-of-a-binary-tree/solutions/2716508/python3javacgotypescript-yi-ti-yi-jie-zh-mqy9/
    def isValidSerialization(self, preorder: str) -> bool:
        stk = []
        for c in preorder.split(","):
            stk.append(c)
            while len(stk) > 2 and stk[-1] == stk[-2] == "#" and stk[-3] != "#":
                stk = stk[:-3]
                stk.append("#")
        return len(stk) == 1 and stk[0] == "#"


# @lc code=end

if __name__ == "__main__":
    preorder: str = deserialize("str", read_line())
    ans = Solution().isValidSerialization(preorder)

    print("\noutput:", serialize(ans))
