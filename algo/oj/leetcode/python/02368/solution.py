# Created by shiyang07ca at 2024/03/02 12:49
# leetgo: dev
# https://leetcode.cn/problems/reachable-nodes-with-restrictions/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        restricted = set(restricted)

        ans = 0
        vis = set()

        def dfs(node):
            if node in vis or node in restricted:
                return

            nonlocal ans
            ans += 1
            vis.add(node)
            for c in g[node]:
                dfs(c)

        dfs(0)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    restricted: List[int] = deserialize("List[int]", read_line())
    ans = Solution().reachableNodes(n, edges, restricted)

    print("\noutput:", serialize(ans))
