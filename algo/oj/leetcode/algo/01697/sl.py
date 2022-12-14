"""

[1697] Checking Existence of Edge Length Limited Paths


An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.


Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.


Example 2:


Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.



Constraints:


	2 <= n <= 10⁵
	1 <= edgeList.length, queries.length <= 10⁵
	edgeList[i].length == 3
	queries[j].length == 3
	0 <= ui, vi, pj, qj <= n - 1
	ui != vi
	pj != qj
	1 <= disi, limitj <= 10⁹
	There may be multiple edges between two nodes.

################################################################


# TODO

1697. 检查边长度限制的路径是否存在

给你一个 n 个点组成的无向图边集 edgeList ，其中 edgeList[i] = [ui, vi, disi] 表
示点 ui 和点 vi 之间有一条长度为 disi 的边。请注意，两个点之间可能有 超过一条边 。

给你一个查询数组queries ，其中 queries[j] = [pj, qj, limitj] ，你的任务是对于每
个查询 queries[j] ，判断是否存在从 pj 到 qj 的路径，且这条路径上的每一条边都 严
格小于 limitj 。

请你返回一个 布尔数组 answer ，其中 answer.length == queries.length ，当
 queries[j] 的查询结果为 true 时， answer 第 j 个值为 true ，否则为 false 。


示例 1：


输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
输出：[false,true]
解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。
对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。
对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。
示例 2：


输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
输出：[true,false]
解释：上图为给定数据。


提示：

2 <= n <= 10^5
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
两个点之间可能有 多条 边。


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

作者：lcbin
链接：https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/solution/by-lcbin-uwd2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


根据题目要求，我们需要对每个查询 queries[i] 进行判断，即判断当前查询的两个点 a
和 b 之间是否存在一条边权小于等于 limit 的路径。

判断两点是否连通可以通过并查集来实现。另外，由于查询的顺序对结果没有影响，因此我
们可以先将所有查询按照 limit 从小到大排序，所有边也按照边权从小到大排序。

然后对于每个查询，我们从边权最小的边开始，将边权严格小于 limit 的所有边加入并查
集，接着利用并查集的查询操作判断两点是否连通即可。


"""


class Solution:
    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # 并查集模板
        fa = list(range(n))

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans, j = [False] * len(queries), 0
        edgeList.sort(key=lambda x: x[2])
        for i, (a, b, limit) in sorted(enumerate(queries), key=lambda x: x[1][2]):
            while j < len(edgeList) and edgeList[j][2] < limit:
                u, v, _ = edgeList[j]
                fa[find(u)] = find(v)
                j += 1
            ans[i] = find(a) == find(b)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n = 3
        edgeList = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]]
        queries = [[0, 1, 2], [0, 2, 5]]
        self.assertEqual(
            self.sl.distanceLimitedPathsExist(n, edgeList, queries),
            [False, True],
        )

        n = 5
        edgeList = [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]]
        queries = [[0, 4, 14], [1, 4, 13]]
        self.assertEqual(
            self.sl.distanceLimitedPathsExist(n, edgeList, queries),
            [True, False],
        )


if __name__ == "__main__":
    unittest.main()
