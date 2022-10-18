"""

[886] Possible Bipartition


We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.


Example 1:


Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].


Example 2:


Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false


Example 3:


Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false



Constraints:


	1 <= n <= 2000
	0 <= dislikes.length <= 10⁴
	dislikes[i].length == 2
	1 <= dislikes[i][j] <= n
	ai < bi
	All the pairs of dislikes are unique.

################################################################

# TODO
# tag: dsu

886. 可能的二分法
给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。

给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。当可以用这种方法将所有人分进两组时，返回 true；否则返回 false。



示例 1：

输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]


示例 2：

输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false


示例 3：

输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false


提示：

1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
dislikes 中每一组都 不同

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *
from collections import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *

# https://leetcode.cn/problems/possible-bipartition/solution/by-lcbin-rgi1/


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        p = list(range(n + 1))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        dis = defaultdict(list)
        for a, b in dislikes:
            dis[a].append(b)
            dis[b].append(a)

        for i in range(1, n + 1):
            for j in dis[i]:
                pi, pj = find(i), find(j)
                if pi == pj:
                    return False
                else:
                    # 将所有 i 不喜欢的元素放到一个集合
                    p[j] = dis[i][0]

        return True


# 错误
# class Solution1:
#     def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
#         g1, g2 = set(), set()

#         dislikes.sort()
#         for a, b in dislikes:
#             #             print(g1, g2)
#             if (a in g1 and b in g1) or (a in g2 and b in g2):
#                 return False

#             if a in g1:
#                 g2.add(b)
#             elif b in g1:
#                 g2.add(a)
#             elif a in g2:
#                 g1.add(b)
#             elif b in g2:
#                 g1.add(a)
#             else:
#                 g1.add(a)
#                 g2.add(b)

#         return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):

        n = 10
        ds = [[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]]
        self.assertEqual(
            self.sl.possibleBipartition(n, ds),
            True,
        )

        n = 4
        ds = [[1, 2], [1, 3], [2, 4]]

        self.assertEqual(
            self.sl.possibleBipartition(n, ds),
            True,
        )

        n = 3
        ds = [[1, 2], [1, 3], [2, 3]]
        self.assertEqual(
            self.sl.possibleBipartition(n, ds),
            False,
        )

        n = 5
        ds = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        self.assertEqual(
            self.sl.possibleBipartition(n, ds),
            False,
        )

        n = 50
        ds = [
            [21, 47],
            [4, 41],
            [2, 41],
            [36, 42],
            [32, 45],
            [26, 28],
            [32, 44],
            [5, 41],
            [29, 44],
            [10, 46],
            [1, 6],
            [7, 42],
            [46, 49],
            [17, 46],
            [32, 35],
            [11, 48],
            [37, 48],
            [37, 43],
            [8, 41],
            [16, 22],
            [41, 43],
            [11, 27],
            [22, 44],
            [22, 28],
            [18, 37],
            [5, 11],
            [18, 46],
            [22, 48],
            [1, 17],
            [2, 32],
            [21, 37],
            [7, 22],
            [23, 41],
            [30, 39],
            [6, 41],
            [10, 22],
            [36, 41],
            [22, 25],
            [1, 12],
            [2, 11],
            [45, 46],
            [2, 22],
            [1, 38],
            [47, 50],
            [11, 15],
            [2, 37],
            [1, 43],
            [30, 45],
            [4, 32],
            [28, 37],
            [1, 21],
            [23, 37],
            [5, 37],
            [29, 40],
            [6, 42],
            [3, 11],
            [40, 42],
            [26, 49],
            [41, 50],
            [13, 41],
            [20, 47],
            [15, 26],
            [47, 49],
            [5, 30],
            [4, 42],
            [10, 30],
            [6, 29],
            [20, 42],
            [4, 37],
            [28, 42],
            [1, 16],
            [8, 32],
            [16, 29],
            [31, 47],
            [15, 47],
            [1, 5],
            [7, 37],
            [14, 47],
            [30, 48],
            [1, 10],
            [26, 43],
            [15, 46],
            [42, 45],
            [18, 42],
            [25, 42],
            [38, 41],
            [32, 39],
            [6, 30],
            [29, 33],
            [34, 37],
            [26, 38],
            [3, 22],
            [18, 47],
            [42, 48],
            [22, 49],
            [26, 34],
            [22, 36],
            [29, 36],
            [11, 25],
            [41, 44],
            [6, 46],
            [13, 22],
            [11, 16],
            [10, 37],
            [42, 43],
            [12, 32],
            [1, 48],
            [26, 40],
            [22, 50],
            [17, 26],
            [4, 22],
            [11, 14],
            [26, 39],
            [7, 11],
            [23, 26],
            [1, 20],
            [32, 33],
            [30, 33],
            [1, 25],
            [2, 30],
            [2, 46],
            [26, 45],
            [47, 48],
            [5, 29],
            [3, 37],
            [22, 34],
            [20, 22],
            [9, 47],
            [1, 4],
            [36, 46],
            [30, 49],
            [1, 9],
            [3, 26],
            [25, 41],
            [14, 29],
            [1, 35],
            [23, 42],
            [21, 32],
            [24, 46],
            [3, 32],
            [9, 42],
            [33, 37],
            [7, 30],
            [29, 45],
            [27, 30],
            [1, 7],
            [33, 42],
            [17, 47],
            [12, 47],
            [19, 41],
            [3, 42],
            [24, 26],
            [20, 29],
            [11, 23],
            [22, 40],
            [9, 37],
            [31, 32],
            [23, 46],
            [11, 38],
            [27, 29],
            [17, 37],
            [23, 30],
            [14, 42],
            [28, 30],
            [29, 31],
            [1, 8],
            [1, 36],
            [42, 50],
            [21, 41],
            [11, 18],
            [39, 41],
            [32, 34],
            [6, 37],
            [30, 38],
            [21, 46],
            [16, 37],
            [22, 24],
            [17, 32],
            [23, 29],
            [3, 30],
            [8, 30],
            [41, 48],
            [1, 39],
            [8, 47],
            [30, 44],
            [9, 46],
            [22, 45],
            [7, 26],
            [35, 42],
            [1, 27],
            [17, 30],
            [20, 46],
            [18, 29],
            [3, 29],
            [4, 30],
            [3, 46],
        ]
        self.assertEqual(
            self.sl.possibleBipartition(n, ds),
            True,
        )


if __name__ == "__main__":
    unittest.main()
