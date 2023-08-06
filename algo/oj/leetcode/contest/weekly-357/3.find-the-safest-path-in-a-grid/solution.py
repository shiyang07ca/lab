# Created by shiyang07ca at 2023/08/06 15:42
# leetgo: dev
# https://leetcode.cn/problems/find-the-safest-path-in-a-grid/
# https://leetcode.cn/contest/weekly-contest-357/problems/find-the-safest-path-in-a-grid/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        a = self.parent[a]
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        self.parent[pb] = pa
        return True


class Solution:
    # 链接：https://leetcode.cn/circle/discuss/chtVBq/view/fkWx2v/
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[inf] * n for _ in range(n)]
        tmp = deque([(i, j) for i in range(n) for j in range(n) if grid[i][j]])
        for i, j in tmp:
            dist[i][j] = 0
        while tmp:
            i, j = tmp.popleft()
            for dx, dy in pairwise([-1, 0, 1, 0, -1]):
                if 0 <= i + dx < n and 0 <= j + dy < n and dist[i + dx][j + dy] == inf:
                    dist[i + dx][j + dy] = dist[i][j] + 1
                    tmp.append((i + dx, j + dy))

        l, r = 0, 2 * n - 2
        while l <= r:
            m = (l + r) // 2
            union = UnionFind(n * n)
            for i in range(n):
                for j in range(n):
                    if dist[i][j] >= m:
                        if i < n - 1 and dist[i + 1][j] >= m:
                            union.merge(i * n + j, (i + 1) * n + j)
                        if j < n - 1 and dist[i][j + 1] >= m:
                            union.merge(i * n + j, i * n + j + 1)
            if union.find(0) == union.find(n * n - 1):
                l = m + 1
            else:
                r = m - 1
        return r

    # 链接：https://leetcode.cn/problems/find-the-safest-path-in-a-grid/solutions/2375565/jie-jin-on2-de-zuo-fa-duo-yuan-bfsdao-xu-r5um/
    def maximumSafenessFactor2(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = []
        dis = [[-1] * n for _ in range(n)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    q.append((i, j))
                    dis[i][j] = 0

        groups = [q]
        while q:  # 多源 BFS
            tmp = q
            q = []
            for i, j in tmp:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] < 0:
                        q.append((x, y))
                        dis[x][y] = len(groups)
            groups.append(q)  # 相同 dis 分组记录

        # 并查集模板
        fa = list(range(n * n))

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        for d in range(len(groups) - 2, 0, -1):
            for i, j in groups[d]:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] >= dis[i][j]:
                        fa[find(x * n + y)] = find(i * n + j)
            if find(0) == find(n * n - 1):  # 写这里判断更快些
                return d
        return 0


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumSafenessFactor(grid)

    print("\noutput:", serialize(ans))
