"""

[106] Construct Binary Tree from Inorder and Postorder Traversal


Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.


--------------------------------------------------

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]


--------------------------------------------------

Example 2:


Input: inorder = [-1], postorder = [-1]
Output: [-1]



Constraints:


	1 <= inorder.length <= 3000
	postorder.length == inorder.length
	-3000 <= inorder[i], postorder[i] <= 3000
	inorder and postorder consist of unique values.
	Each value of postorder also appears in inorder.
	inorder is guaranteed to be the inorder traversal of the tree.
	postorder is guaranteed to be the postorder traversal of the tree.

################################################################


106. 从中序与后序遍历序列构造二叉树
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。



示例 1:

        3
   9         20
          15    7

输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]


示例 2:

输入：inorder = [-1], postorder = [-1]
输出：[-1]


提示:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder 和 postorder 都由 不同 的值组成
postorder 中每一个值都在 inorder 中
inorder 保证是树的中序遍历
postorder 保证是树的后序遍历

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.val}>"


from typing import *


class Solution:
    def build(self, postorder, pl, pr, inorder, il, ir):
        if pl > pr or il > ir:
            return None

        root_val = postorder[pr]
        root_index = self.inorder_val_index[root_val]
        root = TreeNode(root_val)
        left_size = root_index - il
        root.left = self.build(
            postorder, pl, pl + left_size - 1, inorder, il, root_index - 1
        )
        root.right = self.build(
            postorder, pl + left_size, pr - 1, inorder, root_index + 1, ir
        )

        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.inorder_val_index = {}
        for i, val in enumerate(inorder):
            self.inorder_val_index[val] = i

        return self.build(
            postorder, 0, len(postorder) - 1, inorder, 0, len(inorder) - 1
        )


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """

            3
        9      20
             15   7


        """
        n1 = TreeNode(3)
        n2 = TreeNode(20)
        n2.left = TreeNode(15)
        n2.right = TreeNode(7)
        n1.left = TreeNode(9)
        n1.right = n2
        root = n1

        postorder = [9, 15, 7, 20, 3]
        inorder = [9, 3, 15, 20, 7]
        print(self.sl.buildTree(inorder, postorder))

        root = TreeNode(-1)
        postorder = [-1]
        inorder = [-1]
        print(self.sl.buildTree(inorder, postorder))


if __name__ == "__main__":
    unittest.main()
