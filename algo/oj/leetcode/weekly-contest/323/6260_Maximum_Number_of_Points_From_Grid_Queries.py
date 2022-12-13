"""
"""

"""

6260. Maximum Number of Points From Grid Queries

You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queres[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.



Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.


Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106


################################################################

# TODO

6260. 矩阵查询可获得的最大分数

给你一个大小为 m x n 的整数矩阵 grid 和一个大小为 k 的数组 queries 。

找出一个大小为 k 的数组 answer ，且满足对于每个整数 queres[i] ，你从矩阵 左上角 单元格开始，重复以下过程：

如果 queries[i] 严格 大于你当前所处位置单元格，如果该单元格是第一次访问，则获得 1 分，并且你可以移动到所有 4 个方向（上、下、左、右）上任一 相邻 单元格。
否则，你不能获得任何分，并且结束这一过程。
在过程结束后，answer[i] 是你可以获得的最大分数。注意，对于每个查询，你可以访问同一个单元格 多次 。

返回结果数组 answer 。



示例 1：


输入：grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
输出：[5,8,1]
解释：上图展示了每个查询中访问并获得分数的单元格。


示例 2：


输入：grid = [[5,2,1],[1,1,2]], queries = [3]
输出：[0]
解释：无法获得分数，因为左上角单元格的值大于等于 3 。


提示：

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106

"""

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/maximum-number-of-points-from-grid-queries/solution/by-endlesscheng-qeei/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


方法一：离线询问 + 并查集

把矩阵的元素值从小到大排序，询问也从小到大排序。

用双指针遍历矩阵元素值和询问，如果矩阵元素值小于询问值，就把该格子和周围四个格子
中的小于询问值的格子相连。

用并查集可以实现相连的过程，同时维护每个连通块的大小。

答案就是左上角的连通块的大小（前提是左上角小于询问值）。


方法二：离线询问 + 最小堆

仍然是离线询问，还可以从左上角出发向外搜索，用最小堆，初始把左上角的元素值及其坐
标入堆。对每个询问，不断循环，如果堆顶元素值小于询问值，则弹出堆顶，继续搜索。

循环结束时，出堆的元素个数就是答案。

代码实现时，可以用 grid 作为 vis 数组。


"""


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        mn = m * n

        # 并查集模板
        fa = list(range(mn))
        size = [1] * mn

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def merge(from_: int, to: int) -> None:
            from_ = find(from_)
            to = find(to)
            if from_ != to:
                fa[from_] = to
                size[to] += size[from_]

        # 矩阵元素从小到大排序，方便离线
        a = sorted((x, i, j) for i, row in enumerate(grid) for j, x in enumerate(row))

        ans, t = [0] * len(queries), 0
        # 查询的下标按照查询值从小到大排序，方便离线
        for qi, q in sorted(enumerate(queries), key=lambda p: p[1]):
            while t < mn and a[t][0] < q:
                _, i, j = a[t]
                # 枚举周围四个格子，值小于 q 才可以合并
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] < q:
                        merge(i * n + j, x * n + y)  # 把坐标压缩成一维的编号
                t += 1
            if grid[0][0] < q:
                ans[qi] = size[find(0)]  # 左上角的连通块的大小
        return ans


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [0] * len(queries)
        h = [(grid[0][0], 0, 0)]
        grid[0][0] = 0  # 充当 vis 数组的作用
        cnt = 0
        # 查询的下标按照查询值从小到大排序，方便离线
        for qi, q in sorted(enumerate(queries), key=lambda p: p[1]):
            while h and h[0][0] < q:
                cnt += 1
                _, i, j = heappop(h)
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):  # 枚举周围四个格子
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        heappush(h, (grid[x][y], x, y))
                        grid[x][y] = 0
            ans[qi] = cnt

        return ans
