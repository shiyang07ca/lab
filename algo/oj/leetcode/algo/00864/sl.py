"""

[864] Shortest Path to Get All Keys


You are given an m x n grid grid where:


	'.' is an empty cell.
	'#' is a wall.
	'@' is the starting point.
	Lowercase letters represent keys.
	Uppercase letters represent locks.


You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.


Example 1:


Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.


Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6


Example 3:


Input: grid = ["@Aa"]
Output: -1



Constraints:


	m == grid.length
	n == grid[i].length
	1 <= m, n <= 30
	grid[i][j] is either an English letter, '.', '#', or '@'.
	The number of keys in the grid is in the range [1, 6].
	Each key in the grid is unique.
	Each key in the grid has a matching lock.

################################################################

# TODO
# template
# tag: BFS


864. 获取所有钥匙的最短路径
给定一个二维网格 grid ，其中：

'.' 代表一个空房间
'#' 代表一堵
'@' 是起点
小写字母代表钥匙
大写字母代表锁
我们从起点开始出发，一次移动是指向四个基本方向之一行走一个单位空间。我们不能在网
格外面行走，也无法穿过一堵墙。如果途经一个钥匙，我们就把它捡起来。除非我们手里有
对应的钥匙，否则无法通过锁。

假设 k 为 钥匙/锁 的个数，且满足 1 <= k <= 6，字母表中的前 k 个字母在网格中都有
自己对应的一个小写和一个大写字母。换言之，每个锁有唯一对应的钥匙，每个钥匙也有唯
一对应的锁。另外，代表钥匙和锁的字母互为大小写并按字母顺序排列。


返回获取所有钥匙所需要的移动的最少次数。如果无法获取所有钥匙，返回 -1 。


示例 1：

输入：grid = ["@.a.#",
              "###.#",
              "b.A.B"]
输出：8
解释：目标是获得所有钥匙，而不是打开所有锁。



示例 2：

输入：grid = ["@..aA","..B#.","....b"]
输出：6

示例 3:

输入: grid = ["@Aa"]
输出: -1


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] 只含有 '.', '#', '@', 'a'-'f' 以及 'A'-'F'
钥匙的数目范围是 [1, 6]
每个钥匙都对应一个 不同 的字母
每个钥匙正好打开一个对应的锁


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


# https://leetcode.cn/problems/shortest-path-to-get-all-keys/solution/by-lcbin-mk6o/


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        # 钥匙数目
        k = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    s = (i, j)
                if grid[i][j].islower():
                    k += 1

        q = [(*s, 0)]
        used = {(*s, 0)}
        d = (-1, 0, 1, 0, -1)
        ans = 0
        while q:
            for _ in range(len(q)):
                x, y, state = q.pop(0)
                # 找到所有钥匙
                if state == (1 << k) - 1:
                    return ans

                # 往四个方向搜索
                for a, b in pairwise(d):
                    i, j = x + a, y + b
                    nexts = state
                    if 0 <= i < m and 0 <= j < n:
                        c = grid[i][j]
                        # 是墙，或者是锁，但此时没有对应的钥匙，无法通过
                        if (
                            c == "#"
                            or c.isupper()
                            and (state & (1 << (ord(c) - ord("A")))) == 0
                        ):
                            continue
                        # 找到了钥匙, 更新状态
                        elif c.islower():
                            nexts |= 1 << (ord(c) - ord("a"))

                        # 此状态未访问过，入队
                        if (i, j, nexts) not in used:
                            used.add((i, j, nexts))
                            q.append((i, j, nexts))
            ans += 1

        return -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        grid = ["@.a.#", "###.#", "b.A.B"]
        self.assertEqual(
            self.sl.shortestPathAllKeys(grid),
            8,
        )
        grid = ["@..aA", "..B#.", "....b"]
        self.assertEqual(
            self.sl.shortestPathAllKeys(grid),
            6,
        )
        grid = ["@Aa"]
        self.assertEqual(
            self.sl.shortestPathAllKeys(grid),
            -1,
        )


if __name__ == "__main__":
    unittest.main()
