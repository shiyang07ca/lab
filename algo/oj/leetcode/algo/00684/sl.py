"""

[684] Redundant Connection


In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.


Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]


Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]



Constraints:


	n == edges.length
	3 <= n <= 1000
	edges[i].length == 2
	1 <= ai < bi <= edges.length
	ai != bi
	There are no repeated edges.
	The given graph is connected.

################################################################

# TODO
# tag: dsu, 并查集

684. 冗余连接
树可以看成是一个连通且 无环 的 无向 图。

给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含
在 1 到 n 中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 n 的二
维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个
答案，则返回数组 edges 中最后出现的边。


示例 1：

   1-------2
   |       |
   |       |
   |       |
   3--------



输入: edges = [[1,2], [1,3], [2,3]]
输出: [2,3]


示例 2：

      2----1----5
      |    |
      |    |
      3----4
输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]


提示:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
edges 中无重复元素
给定的图是连通的

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
https://algo.itcharge.cn/Solutions/0600-0699/redundant-connection/

树可以看做是无环的图，这道题就是要找出那条添加边之后成环的边。可以考虑用并查集来
做。

- 从前向后遍历每一条边。
- 如果边的两个节点不在同一个集合，就加入到一个集合（链接到同一个根节点）。
- 如果边的节点已经出现在同一个集合里，说明边的两个节点已经连在一起了，再加入这条
边一定会出现环，则这条边就是所求答案。


"""

# 并查集
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = list(range(len(edges) + 1))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        ans = []
        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa != pb:
                p[pa] = pb
            else:
                ans = [a, b]

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
