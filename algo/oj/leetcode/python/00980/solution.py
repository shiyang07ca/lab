# Created by shiyang07ca at 2023/08/04 12:59
# leetgo: dev
# https://leetcode.cn/problems/unique-paths-iii/

from collections import deque
from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: Backtracking


class Solution:
    def uniquePathsIII1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        c1 = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    start = (i, j)
                elif v == -1:
                    c1 += 1

        c0 = m * n - 2 - c1
        print(f"cnt: {c0}")
        q = deque([start])
        vis = set()
        dirs = (-1, 0, 1, 0, -1)
        ans = 0
        print("================================================================")
        while q:
            x, y = q.popleft()
            for a, b in pairwise(dirs):
                i, j = x + a, y + b
                print(i, j)
                if 0 <= i < m and 0 <= j < n and (i, j) not in vis:
                    if grid[i][j] == 0:
                        vis.add((i, j))
                        q.append((i, j))
                    if grid[i][j] == 2 and len(vis) == c0:
                        ans += 1

        return ans

    # 链接：https://leetcode.cn/problems/unique-paths-iii/solutions/2372252/liang-chong-fang-fa-hui-su-zhuang-tai-ya-26py/
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x: int, y: int, left: int) -> int:
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0:
                return 0  # 不合法
            if grid[x][y] == 2:  # 到达终点
                return left == 0  # 必须访问所有的无障碍方格
            grid[x][y] = -1  # 标记成访问过，因为题目要求「不能重复通过同一个方格」
            ans = (
                dfs(x - 1, y, left - 1)
                + dfs(x, y - 1, left - 1)
                + dfs(x + 1, y, left - 1)
                + dfs(x, y + 1, left - 1)
            )
            grid[x][y] = 0  # 恢复现场
            return ans

        cnt0 = sum(row.count(0) for row in grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:  # 起点
                    return dfs(i, j, cnt0 + 1)  # +1 把起点也算上


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().uniquePathsIII(grid)

    print("\noutput:", serialize(ans))
