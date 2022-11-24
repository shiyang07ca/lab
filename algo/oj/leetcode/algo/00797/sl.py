"""

[797] All Paths From Source to Target


Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]



Constraints:


	n == graph.length
	2 <= n <= 15
	0 <= graph[i][j] < n
	graph[i][j] != i (i.e., there will be no self-loops).
	All the elements of graph[i] are unique.
	The input graph is guaranteed to be a DAG.

################################################################

# TODO
# template
# tag: DFS, backtracking

797. 所有可能的路径
给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

 graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。



示例 1：
   0  ->  1
   |      |
   v      v
   2  ->  3


输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3

示例 2：

输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


提示：

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i（即不存在自环）
graph[i] 中的所有元素 互不相同
保证输入为 有向无环图（DAG）

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *
from copy import *
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # oj
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        target = len(graph) - 1

        def dfs(i, path):
            if i == target:
                ans.append(path[:])
                return

            for n in graph[i]:
                path.append(n)
                dfs(n, path)
                path.pop()

        dfs(0, [0])
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        graph = [[1, 2], [3], [3], []]
        self.assertEqual(
            self.sl.allPathsSourceTarget(graph),
            [[0, 1, 3], [0, 2, 3]],
        )

        graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
        self.assertEqual(
            self.sl.allPathsSourceTarget(graph),
            [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]],
        )


if __name__ == "__main__":
    unittest.main()
