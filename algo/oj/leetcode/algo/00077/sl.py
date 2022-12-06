"""

[77] Combinations


Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.


--------------------------------------------------

Example 1:


Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.


--------------------------------------------------

Example 2:


Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.



Constraints:


	1 <= n <= 20
	1 <= k <= n

################################################################

# TODO
# tag: combination

77. 组合

给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。



示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]


示例 2：

输入：n = 1, k = 1
输出：[[1]]


提示：

1 <= n <= 20
1 <= k <= n

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        pass


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n = 4
        k = 2
        # [
        #     [2, 4],
        #     [3, 4],
        #     [2, 3],
        #     [1, 2],
        #     [1, 3],
        #     [1, 4],
        # ]
        print(self.sl.combine(n, k))

        n = 1
        k = 1
        # [[1]]
        print(self.sl.combine(n, k))


if __name__ == "__main__":
    unittest.main()
