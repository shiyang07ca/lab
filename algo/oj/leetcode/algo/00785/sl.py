"""

[785] Is Graph Bipartite?



[785] Is Graph Bipartite?


There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:


	There are no self-edges (graph[u] does not contain u).
	There are no parallel edges (graph[u] does not contain duplicate values).
	If v is in graph[u], then u is in graph[v] (the graph is undirected).
	The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.


A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.


Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

Example 2:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.


Constraints:


	graph.length == n
	1 <= n <= 100
	0 <= graph[u].length < n
	0 <= graph[u][i] <= n - 1
	graph[u] does not contain u.
	All the values of graph[u] are unique.
	If graph[u] contains v, then graph[v] contains u.

################################################################

# TODO

785. 判断二分图

存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯
一编号。给你一个二维数组 graph ，其中 graph[u] 是一个节点数组，由节点 u 的邻接节
点组成。形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的
无向边。该无向图同时具有以下属性：

- 不存在自环（graph[u] 不包含 u）。
- 不存在平行边（graph[u] 不包含重复值）。
- 如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
- 这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。

二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每
一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 二分图 。

如果图是二分图，返回 true ；否则，返回 false 。


示例 1：
      0 ------- 1
      |  \      |
      |    \    |
      |      \  |
      3 ------- 2

输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
输出：false
解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。


示例 2：

      0 ------- 1
      |         |
      |         |
      |         |
      3 ------- 2

输入：graph = [[1,3],[0,2],[1,3],[0,2]]
输出：true
解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。


提示：

graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] 不会包含 u
graph[u] 的所有值 互不相同
如果 graph[u] 包含 v，那么 graph[v] 也会包含 u


"""

import sys
import inspect
import os
import unittest

from itertools import *
from collections import *
from copy import *
from typing import *
from math import *

from os.path import abspath, join, dirname

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # oj
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *

"""
https://algo.itcharge.cn/Solutions/0700-0799/is-graph-bipartite/

对于图中的任意节点 u 和 v，如果 u 和 v 之间有一条无向边，那么 u 和 v 必然属于不同的集合。

我们可以通过在深度优先搜索中对邻接点染色标记的方式，来识别该图是否是二分图。具体做法如下：

- 找到一个没有染色的节点 u，将其染成红色。
- 然后遍历该节点直接相连的节点 v，如果该节点没有被染色，则将该节点直接相连的节点染
成蓝色，表示两个节点不是同一集合。如果该节点已经被染色并且颜色跟 u 一样，则说明
该图不是二分图，直接返回 False。
- 从上面染成蓝色的节点 v 出发，遍历该节点直接相连的节点。。。依次类推的递归下去。
- 如果所有节点都顺利染上色，则说明该图为二分图，返回 True。否则，如果在途中不能顺
利染色，则返回 False。

"""

# DFS
class Solution:
    def isBipartite(self, g: List[List[int]]) -> bool:
        N = len(g)
        color = [0] * N

        def dfs(node, c):
            color[node] = c
            for neighbor in g[node]:
                if color[neighbor] == 0 and not dfs(neighbor, -c):
                    return False
                elif color[neighbor] != -c:
                    return False

            return True

        for i in range(N):
            if color[i] == 0 and not dfs(i, 1):
                return False

        return True


# BFS
class Solution1:
    def isBipartite(self, g: List[List[int]]) -> bool:
        N = len(g)
        color = [0] * N

        for i in range(N):
            if color[i] == 0:
                q = deque([i])
                color[i] = 1
                while q:
                    node = q.popleft()
                    for neighbor in g[node]:
                        if color[neighbor] == 0:
                            q.append(neighbor)
                            color[neighbor] = -color[node]
                        elif color[neighbor] != -color[node]:
                            return False
        return True


"""
遍历每个顶点，将当前顶点所有邻居节点进行合并，并判断是否存在邻居节点已经和当前节
点处于同一集合
"""

# DSU
class Solution2:
    def isBipartite(self, g: List[List[int]]) -> bool:
        N = len(g)
        p = list(range(N))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])

            return p[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                p[pa] = pb

        for i, neighbor in enumerate(g):
            for j in neighbor:
                if p[i] == p[j]:
                    return False
                union(neighbor[0], j)
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution2()

    def test_sl(self):

        g = [[1, 3], [0, 2], [1, 3], [0, 2]]
        self.assertEqual(
            self.sl.isBipartite(g),
            True,
        )

        g = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
        self.assertEqual(
            self.sl.isBipartite(g),
            False,
        )


if __name__ == "__main__":
    unittest.main()
