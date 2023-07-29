# Created by shiyang07ca at 2023/07/29 19:41
# leetgo: dev
# https://leetcode.cn/problems/build-a-matrix-with-conditions/
# https://leetcode.cn/contest/weekly-contest-308/problems/build-a-matrix-with-conditions/

from typing import *
from leetgo_py import *

# @lc code=begin


# https://leetcode.cn/problems/build-a-matrix-with-conditions/solutions/1781092/by-endlesscheng-gpev/
# 1. 题目给的约束，是行与行之间，列与列之间的，并没有行与列之间的
# 2. 分别处理 行与行，列与列
# 3. 找到一种合理的顺序
# 4. 拓扑排序
class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        def topo_sort(edges: List[List[int]]) -> List[int]:
            g = [[] for _ in range(k)]
            left = [0] * k  # 第 i 门课剩余的先修课数目，一旦这个数为 0，则可以修第 i 门课
            for x, y in edges:
                x -= 1
                y -= 1
                g[x].append(y)
                left[y] += 1

            order = []  # 拓扑序
            q = deque(i for i, v in enumerate(left) if v == 0)

            while q:
                x = q.popleft()
                order.append(x)
                for y in g[x]:
                    left[y] -= 1  # x 指向的课程，它的先修课 -1
                    if left[y] == 0:
                        q.append(y)
            return order if len(order) == k else None

        row = topo_sort(rowConditions)
        if row is None:
            return []
        col = topo_sort(colConditions)
        if col is None:
            return []

        pos = {x: i for i, x in enumerate(col)}
        ans = [[0] * k for _ in range(k)]
        for i, x in enumerate(row):
            ans[i][pos[x]] = x + 1

        return ans


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    rowConditions: List[List[int]] = deserialize("List[List[int]]", read_line())
    colConditions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().buildMatrix(k, rowConditions, colConditions)

    print("\noutput:", serialize(ans))
