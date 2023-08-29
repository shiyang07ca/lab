# Created by shiyang07ca at 2023/08/29 09:02
# leetgo: dev
# https://leetcode.cn/problems/binary-trees-with-factors/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        arr.sort()
        t = defaultdict(list)
        pos = {x: i for i, x in enumerate(arr)}

        for i, x in enumerate(arr):
            if x * x in pos:
                t[pos[x * x]].append((i, i))
            for j in range(i + 1, n):
                if x * arr[j] in pos:
                    t[pos[x * arr[j]]].append((i, j))

        @cache
        def dfs(i):
            ans = 1
            for a, b in t[i]:
                if a == b:
                    ans = (ans + dfs(a) * dfs(b)) % MOD
                else:
                    ans = (ans + dfs(a) * dfs(b) * 2) % MOD
            return ans

        return sum(dfs(i) for i in range(n)) % MOD


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numFactoredBinaryTrees(arr)

    print("\noutput:", serialize(ans))
