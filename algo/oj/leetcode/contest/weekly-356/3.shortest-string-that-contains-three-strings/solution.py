# Created by shiyang07ca at 2023/07/30 10:34
# leetgo: dev
# https://leetcode.cn/problems/shortest-string-that-contains-three-strings/
# https://leetcode.cn/contest/weekly-contest-356/problems/shortest-string-that-contains-three-strings/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    # 链接：https://leetcode.cn/problems/shortest-string-that-contains-three-strings/solutions/2364733/mei-ju-by-endlesscheng-qc44/
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(s: str, t: str) -> str:
            # 先特判完全包含的情况
            if t in s:
                return s
            if s in t:
                return t
            for i in range(min(len(s), len(t)), 0, -1):
                # 枚举：s 的后 i 个字母和 t 的前 i 个字母是一样的
                if s[-i:] == t[:i]:
                    return s + t[i:]
            return s + t

        ans = ""
        for a, b, c in permutations((a, b, c)):
            s = merge(merge(a, b), c)
            if ans == "" or len(s) < len(ans) or len(s) == len(ans) and s < ans:
                ans = s
        return ans


# @lc code=end

if __name__ == "__main__":
    a: str = deserialize("str", read_line())
    b: str = deserialize("str", read_line())
    c: str = deserialize("str", read_line())
    ans = Solution().minimumString(a, b, c)

    print("\noutput:", serialize(ans))
