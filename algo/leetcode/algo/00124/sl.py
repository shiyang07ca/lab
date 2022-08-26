"""

[124] Binary Tree Maximum Path Sum


A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.


--------------------------------------------------

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.


--------------------------------------------------

Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.



Constraints:


	The number of nodes in the tree is in the range [1, 3 * 10⁴].
	-1000 <= Node.val <= 1000


################################################################


124. 二叉树中的最大路径和
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。



示例 1：
          1
       2     3

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6


示例 2：
             -10
          9       20
                15  7

输入：root = [-10,9,20,null,null,15,7]
输出：42

解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


提示：

树中节点数目范围是 [1, 3 * 10^4]
-1000 <= Node.val <= 1000

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


import math


class Solution:
    # 这个递归函数返回包含 root 节点的最大路径和
    def recur(self, root):
        if root is None:
            return 0
        # 分别返回包含左右子节点的最大路径和，
        # 如果路径和小于零，那么不使用当前左右子树，返回零
        l = max(0, self.recur(root.left))
        r = max(0, self.recur(root.right))
        # 更新最大路径和
        self.ans = max(self.ans, l + root.val + r)
        return max(l, r) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.ans = -math.inf
        self.recur(root)
        return self.ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
           1
        2     3
        """
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.right = TreeNode(3)
        n1.log()
        self.assertEqual(
            self.sl.maxPathSum(n1),
            6,
        )

    def test_sl2(self):
        """
           -10
        9       20
              15  7
        """
        n1 = TreeNode(-10)
        n1.left = TreeNode(9)
        n1.right = TreeNode(20)
        n1.right.left = TreeNode(15)
        n1.right.right = TreeNode(7)
        n1.log()
        self.assertEqual(
            self.sl.maxPathSum(n1),
            42,
        )

    def test_sl3(self):
        n1 = TreeNode(-10)
        self.assertEqual(
            self.sl.maxPathSum(n1),
            -10,
        )

        """
            -2
         -1
        """
        n1 = TreeNode(-2)
        n1.left = TreeNode(-1)
        n1.log()
        self.assertEqual(
            self.sl.maxPathSum(n1),
            -1,
        )

    def test_sl4(self):

        """
           1
        2
        """
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.log()
        self.assertEqual(
            self.sl.maxPathSum(n1),
            3,
        )

    def test_sl5(self):

        """
           -1
        0     1
        """
        n1 = TreeNode(-1)
        n1.left = TreeNode(0)
        n1.right = TreeNode(1)
        n1.log()
        self.assertEqual(
            self.sl.maxPathSum(n1),
            1,
        )

    def test_sl6(self):

        """
                  1
            -2        -3
          1    3   -2
        -1
        """
        n1 = TreeNode(1)
        n1.left = TreeNode(-2)
        n1.right = TreeNode(-3)
        n1.left.left = TreeNode(1)
        n1.left.right = TreeNode(3)
        n1.right.left = TreeNode(-2)
        n1.left.left.left = TreeNode(-1)
        n1.log()
        self.assertEqual(
            self.sl.maxPathSum(n1),
            3,
        )


if __name__ == "__main__":
    unittest.main()
