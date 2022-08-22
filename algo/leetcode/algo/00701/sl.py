"""

[701] Insert into a Binary Search Tree


You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.


--------------------------------------------------

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:



--------------------------------------------------

Example 2:


Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]


--------------------------------------------------

Example 3:


Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]



Constraints:


	The number of nodes in the tree will be in the range [0, 10⁴].
	-10⁸ <= Node.val <= 10⁸
	All the values Node.val are unique.
	-10⁸ <= val <= 10⁸
	It's guaranteed that val does not exist in the original BST.


################################################################


701. 二叉搜索树中的插入操作
给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。

注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。



示例 1：

          4                           4
       2     7    =>              2      7
    1    3                     1    3   5

输入：root = [4,2,7,1,3], val = 5
输出：[4,2,7,1,3,5]
解释：另一个满足题目要求可以通过的树是：

              5
            2   7
          1  3
              4

示例 2：

输入：root = [40,20,60,10,30,50,70], val = 25
输出：[40,20,60,10,30,50,70,null,null,25]


示例 3：

输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
输出：[4,2,7,1,3,5]


提示：

树中的节点数将在 [0, 104]的范围内。
-108 <= Node.val <= 108
所有值 Node.val 是 独一无二 的。
-108 <= val <= 108

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
    def traverse(self, root, val):
        if root.left is None and val < root.val:
            root.left = TreeNode(val)
            return
        if root.right is None and val > root.val:
            root.right = TreeNode(val)
            return

        if val < root.val:
            self.traverse(root.left, val)

        if val > root.val:
            self.traverse(root.right, val)

    def insertIntoBST1(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        self.traverse(root, val)
        return root

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)

        return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
              4                           4
           2     7    =>              2      7
        1    3                     1    3   5

        """
        n1 = TreeNode(4)
        n2 = TreeNode(2)
        n2.left = TreeNode(1)
        n2.right = TreeNode(3)
        n1.left = n2
        n1.right = TreeNode(7)

        n1.log()

        # n1.right.left = TreeNode(5)

        n1 = self.sl.insertIntoBST(n1, 5)
        n1.log()


if __name__ == "__main__":
    unittest.main()
