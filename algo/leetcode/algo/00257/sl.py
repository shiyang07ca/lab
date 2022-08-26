"""

[257] Binary Tree Paths


Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.


--------------------------------------------------

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]


--------------------------------------------------

Example 2:


Input: root = [1]
Output: ["1"]



Constraints:


	The number of nodes in the tree is in the range [1, 100].
	-100 <= Node.val <= 100


################################################################


257. 二叉树的所有路径
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。


示例 1：

         1
      2     3
       5

输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]


示例 2：

输入：root = [1]
输出：["1"]


提示：

树中节点的数目在范围 [1, 100] 内
-100 <= Node.val <= 100

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
    def recur(self, root, pre):
        if root is None:
            return

        pre = f"{pre}->{root.val}" if pre else f"{root.val}"
        if root.left is None and root.right is None:
            self.ans.append(pre)

        self.recur(root.left, pre)

        self.recur(root.right, pre)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.ans = []
        self.recur(root, "")
        return self.ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """

           1
        2     3
         5

        """
        n1 = TreeNode(1)
        n1.right = TreeNode(3)
        n1.left = TreeNode(2)
        n1.left.right = TreeNode(5)
        n1.log()
        # ["1->2->5","1->3"]
        print(self.sl.binaryTreePaths(n1))


if __name__ == "__main__":
    unittest.main()
