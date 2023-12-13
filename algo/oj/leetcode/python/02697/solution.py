# Created by shiyang07ca at 2023/12/13 23:31
# leetgo: dev
# https://leetcode.cn/problems/lexicographically-smallest-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = []
        n = len(s)
        for i in range(n // 2):
            if s[i] <= s[-i-1]:
                ans.append(s[i])
            else:
                ans.append(s[-i - 1])
        if n % 2:
            return "".join(ans + [s[n // 2]] + ans[::-1])
        else:
            return "".join(ans + ans[::-1])


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().makeSmallestPalindrome(s)

    print("\noutput:", serialize(ans))
