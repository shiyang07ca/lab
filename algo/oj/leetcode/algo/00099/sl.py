"""

[99] Recover Binary Search Tree


You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.


--------------------------------------------------

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.


--------------------------------------------------

Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.



Constraints:


	The number of nodes in the tree is in the range [2, 1000].
	-2³¹ <= Node.val <= 2³¹ - 1



Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?

################################################################


# TODO

99. 恢复二叉搜索树


给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。


示例 1：
         1                             3
     3                =>            1
      2                              2


输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。


示例 2：

         3                             2
     1       4         =>          1       4
           2                              3


输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。


提示：

树上节点的数目在范围 [2, 1000] 内
-231 <= Node.val <= 231 - 1


进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？

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


class Solution2:
    def swap(self, n1, n2, n1_parent, n2_parent):

        if n1_parent is not None:
            if n1_parent.val > n2.val:
                n1_parent.left = n2
            else:
                n1_parent.right = n2

        if n2_parent is not None:
            if n2_parent.val > n1.val:
                n2_parent.left = n1
            else:
                n2_parent.right = n1

        n1_val = n1.val
        left = n1.left
        right = n1.right

        n1.left = n2.left
        n1.right = n2.right
        n1.val = n2.val

        n2.left = left
        n2.right = right
        n2.val = n1_val

    def process(self, root, node, root_parent, node_parent):
        if node is None:
            return

        if node.left and root.val < node.left.val:
            print(root, node.left)
            self.swap(root, node.left, root_parent, node)
            return
        elif node.left:
            self.process(root, node.left, root_parent, node)

        if node.right and root.val > node.right.val:
            print(root, node.right)
            self.swap(root, node.right, root_parent, node)
            return
        elif node.right:
            self.process(root, node.right, root_parent, node)

        self.process(root.left, root.left, root, root)
        self.process(root.right, root.right, root, root)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.process(root, root, None, None)


class Solution:
    def process(self):
        pass

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.process(root)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n1 = TreeNode(1)
        n1.left = TreeNode(3)
        n1.left.right = TreeNode(2)
        n1.log()
        print("################")
        self.sl.recoverTree(n1)
        n1.log()
        print("################")

    def test_sl2(self):
        n1 = TreeNode(3)
        n1.left = TreeNode(1)
        n1.right = TreeNode(4)
        n1.right.left = TreeNode(2)
        n1.log()
        print("################")
        self.sl.recoverTree(n1)
        n1.log()
        print("################")


if __name__ == "__main__":
    unittest.main()
