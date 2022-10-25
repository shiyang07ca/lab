"""

[538] Convert BST to Greater Tree


Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:


	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.



--------------------------------------------------

Example 1:


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]


--------------------------------------------------

Example 2:


Input: root = [0,null,1]
Output: [1,null,1]



Constraints:


	The number of nodes in the tree is in the range [0, 10⁴].
	-10⁴ <= Node.val <= 10⁴
	All the values in the tree are unique.
	root is guaranteed to be a valid binary search tree.



* * * * * * * * * * * * * * * * * * * * * * * * *

Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/


################################################################

538. 把二叉搜索树转换为累加树
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

提醒一下，二叉搜索树满足下列约束条件：

节点的左子树仅包含键 小于 节点键的节点。
节点的右子树仅包含键 大于 节点键的节点。
左右子树也必须是二叉搜索树。
注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同



示例 1：

                 4
             1       6
           0   2   5   7
                3       8

                 |
                 v

                   30
             36         21
           36   35    26    15
                  33           8


输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

示例 2：

输入：root = [0,null,1]
输出：[1,null,1]


示例 3：

输入：root = [1,0,2]
输出：[3,3,2]


示例 4：

输入：root = [3,2,4,1]
输出：[7,9,4,10]


提示：

树中的节点数介于 0 和 104 之间。
每个节点的值介于 -104 和 104 之间。
树中的所有值 互不相同 。
给定的树为二叉搜索树。

"""

import sys
import inspect
import os
from os.path import abspath, join, dirname


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import TreeNode


from typing import *


class Solution:
    def traverse_recur(self, root):
        if root is None:
            return

        self.traverse_recur(root.right)
        self.pre += root.val
        root.val = self.pre
        self.traverse_recur(root.left)

    # 右， 中，左遍历 BST
    def traverse_iter(self, root):
        if root is None:
            return

        stack = []
        pre = 0
        while root or stack:
            if root:
                stack.append(root)
                root = root.right
            else:
                node = stack.pop()

                # 更新当前节点
                pre += node.val
                node.val = pre

                root = node.left

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.traverse_iter(root)

        # self.pre = 0
        # self.traverse_recur(root)
        return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """

              4
          1       6
        0   2   5   7
             3       8

              |
              v

                30
          36         21
        36   35    26    15
               33          8

        """
        n1 = TreeNode(4)
        n2 = TreeNode(1)
        n2.left = TreeNode(0)
        n3 = TreeNode(6)
        n3.left = TreeNode(5)
        n4 = TreeNode(2)
        n4.right = TreeNode(3)
        n2.right = n4
        n5 = TreeNode(7)
        n5.right = TreeNode(8)
        n3.right = n5

        n1.left = n2
        n1.right = n3

        n1.log()

        root = self.sl.convertBST(n1)
        root.log()


if __name__ == "__main__":
    unittest.main()
