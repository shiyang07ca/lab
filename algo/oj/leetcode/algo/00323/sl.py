"""

[323] Number of Connected Components in an Undirected Graph


You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.



Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1


Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.


################################################################

# TODO
# template: BFS, DFS, union find

323. 无向图中连通分量的数目

你有一个包含 n 个节点的图。给定一个整数 n 和一个数组 edges ，其中 edges[i] = [ai, bi] 表示图中 ai 和 bi 之间有一条边。

返回 图中已连接分量的数目 。



示例 1:

  0 --- 1 --- 2
  3 --- 4

输入: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
输出: 2


示例 2:

 0 --- 1 --- 2 --- 3 --- 4


输入: n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]
输出:  1


提示：

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
edges 中不会出现重复的边


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

# 并查集
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        ans = n
        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa != pb:
                p[pa] = pb
                ans -= 1
        return ans


# DFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = set()
        ans = 0

        def dfs(u):
            vis.add(u)
            for v in g[u]:
                if v not in vis:
                    dfs(v)

        for i in range(n):
            if i not in vis:
                ans += 1
                dfs(i)

        return ans


# BFS
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        vis = set()
        ans = 0
        for i in range(n):
            if i not in vis:
                ans += 1
                vis.add(i)
                q = deque([i])
                while q:
                    u = q.popleft()
                    for v in g[u]:
                        if v not in vis:
                            vis.add(v)
                            q.append(v)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl,
            None,
        )


if __name__ == "__main__":
    unittest.main()
