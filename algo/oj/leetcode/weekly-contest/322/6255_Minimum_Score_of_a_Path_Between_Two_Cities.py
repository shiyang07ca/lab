"""

6255. Minimum Score of a Path Between Two Cities

You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.


Example 1:


Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
Example 2:


Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.


Constraints:

2 <= n <= 105
1 <= roads.length <= 105
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 104
There are no repeated edges.
There is at least one path between 1 and n.

################################################################

# TODO

https://leetcode.cn/contest/weekly-contest-322/problems/minimum-score-of-a-path-between-two-cities/

6255. 两个城市间路径的最小分数 显示英文描述

给你一个正整数 n ，表示总共有 n 个城市，城市从 1 到 n 编号。给你一个二维数组
roads ，其中 roads[i] = [ai, bi, distancei] 表示城市 ai 和 bi 之间有一条 双向 道
路，道路距离为 distancei 。城市构成的图不一定是连通的。


两个城市之间一条路径的 分数 定义为这条路径中道路的 最小 距离。

城市 1 和城市 n 之间的所有路径的 最小 分数。

注意：

一条路径指的是两个城市之间的道路序列。
一条路径可以 多次 包含同一条道路，你也可以沿着路径多次到达城市 1 和城市 n 。
测试数据保证城市 1 和城市n 之间 至少 有一条路径。


示例 1：



输入：n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
输出：5
解释：城市 1 到城市 4 的路径中，分数最小的一条为：1 -> 2 -> 4 。这条路径的分数是 min(9,5) = 5 。
不存在分数更小的路径。


示例 2：



输入：n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
输出：2
解释：城市 1 到城市 4 分数最小的路径是：1 -> 2 -> 1 -> 3 -> 4 。这条路径的分数是 min(2,2,4,7) = 2 。


提示：

2 <= n <= 105
1 <= roads.length <= 105
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 104
不会有重复的边。
城市 1 和城市 n 之间至少有一条路径。

"""

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/minimum-score-of-a-path-between-two-cities/solution/du-ti-ti-by-endlesscheng-qp1m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # 连通块内的最小边权
        g = [[] for _ in range(n)]
        for x, y, d in roads:
            g[x - 1].append((y - 1, d))
            g[y - 1].append((x - 1, d))
        ans = inf
        vis = [False] * n

        def dfs(x: int) -> None:
            nonlocal ans
            vis[x] = True
            for y, d in g[x]:
                ans = min(ans, d)
                if not vis[y]:
                    dfs(y)

        dfs(0)
        return ans


"""
我们发现，一个连通块内，两个城市间路径的最小分数即为该连通块内最小的路径价值（因
为我们可以过去绕路），实际上只需要进行一次 BFS 或者 DFS 即可，中途维护最小路径价
值；我们也可以使用并查集，先获得连通块，再对每条边判断是否在连通块内（有并查集模
板的话，代码量相对更少，因为不需要建图）。

如使用 BFS 或者 DFS 为 O(n)，使用并查集为 O(n α(n))，可以认为是 O(n)。

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/T0eOvC/view/CXzRey/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        union = UnionFind(n + 1)
        for x, y, v in roads:
            union.merge(x, y)
        return min(v for x, y, v in roads if union.find(x) == union.find(1))
