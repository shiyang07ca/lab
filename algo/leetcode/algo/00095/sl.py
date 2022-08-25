"""

[95] Unique Binary Search Trees II


Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.


--------------------------------------------------

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]


--------------------------------------------------

Example 2:


Input: n = 1
Output: [[1]]



Constraints:


	1 <= n <= 8


################################################################


95. 不同的二叉搜索树 II
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。



示例 1：

   1               1
     3              2
   2                 3
================================================================
   2               3
  1 3             2
                 1
================================================================
   3
  1 2

输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]



示例 2：

输入：n = 1
输出：[[1]]


提示：

1 <= n <= 8

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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        return self.build(1, n)

    def build(self, lo, hi):
        ans = []
        if lo > hi:
            ans.append(None)
            return ans

        for i in range(lo, hi + 1):
            left_trees = self.build(lo, i - 1)
            right_trees = self.build(i + 1, hi)
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    ans.append(root)

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        nodes = self.sl.generateTrees(3)
        for n in nodes:
            n.log()


if __name__ == "__main__":
    unittest.main()
