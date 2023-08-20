# Created by shiyang07ca at 2023/08/19 23:35
# leetgo: dev
# https://leetcode.cn/problems/make-string-a-subsequence-using-cyclic-increments/
# https://leetcode.cn/contest/biweekly-contest-111/problems/make-string-a-subsequence-using-cyclic-increments/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def check(a, b):
            if a == b or (ord(b) - ord(a) == 1) or (a == "z" and b == "a"):
                return True
            return False

        i = j = 0
        m, n = len(str1), len(str2)
        if n > m:
            return False

        while i < m:
            if check(str1[i], str2[j]):
                i += 1
                j += 1
            else:
                i += 1
            if j == n:
                return True

        return False

    # 链接：https://leetcode.cn/circle/discuss/s7qlIZ/view/iluIfU/
    def canMakeSubsequence2(self, str1: str, str2: str) -> bool:
        idx = 0
        n = len(str2)
        for c in str1:
            if idx < n and (ord(str2[idx]) - ord(c)) % 26 <= 1:
                idx += 1
        return idx == n


# @lc code=end

if __name__ == "__main__":
    str1: str = deserialize("str", read_line())
    str2: str = deserialize("str", read_line())
    ans = Solution().canMakeSubsequence(str1, str2)

    print("\noutput:", serialize(ans))
