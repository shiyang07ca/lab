# Created by shiyang07ca at 2023/12/07 00:06
# leetgo: dev
# https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        g1 = [[] for _ in range(n)]
        g2 = [[] for _ in range(n)]
        for x, y in connections:
            g1[x].append(y)
            g2[y].append(x)

        ans = 0
        q = deque([0])
        vis = {0}
        while q:
            u = q.popleft()
            for v in g1[u]:
                if v not in vis:
                    ans += 1
                    q.append(v)
                    vis.add(v)
            for v in g2[u]:
                if v not in vis:
                    q.append(v)
                    vis.add(v)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    connections: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minReorder(n, connections)

    print("\noutput:", serialize(ans))
