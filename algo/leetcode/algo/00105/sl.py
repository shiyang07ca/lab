"""

[105] Construct Binary Tree from Preorder and Inorder Traversal


Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


--------------------------------------------------

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


--------------------------------------------------

Example 2:


Input: preorder = [-1], inorder = [-1]
Output: [-1]



Constraints:


	1 <= preorder.length <= 3000
	inorder.length == preorder.length
	-3000 <= preorder[i], inorder[i] <= 3000
	preorder and inorder consist of unique values.
	Each value of inorder also appears in preorder.
	preorder is guaranteed to be the preorder traversal of the tree.
	inorder is guaranteed to be the inorder traversal of the tree.

################################################################

105. 从前序与中序遍历序列构造二叉树
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。



示例 1:

    3
  9   20
     15 7


输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]


示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]


提示:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证 为二叉树的前序遍历序列
inorder 保证 为二叉树的中序遍历序列

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
    def build(self, preorder, pl, pr, inorder, il, ir):
        if pl > pr or il > ir:
            return None

        root_val = preorder[pl]
        # 根节点在 inorder 中的位置
        root_index = self.inorder_val_index[root_val]
        root = TreeNode(root_val)
        # 注意：
        # left_size = root_index - il 等于 ineorder 中左树的 *长度*
        left_size = root_index - il
        # preoder
        #    root          left                                right
        # | pl | pl+1  ....   pl + left_size  |   pl + left_size + 1  ....     lr |

        # inorder
        #       left                        root                  right
        # | il .......  root_index - 1 | root_index  | root_index + 1  ...... ir  |
        root.left = self.build(
            preorder, pl + 1, pl + left_size, inorder, il, root_index - 1
        )
        root.right = self.build(
            preorder, pl + left_size + 1, pr, inorder, root_index + 1, ir
        )

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorder_val_index = {}
        for i, val in enumerate(inorder):
            self.inorder_val_index[val] = i

        return self.build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)


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

        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        print(self.sl.buildTree(preorder, inorder))

        root = TreeNode(-1)
        preorder = [-1]
        inorder = [-1]
        print(self.sl.buildTree(preorder, inorder))


if __name__ == "__main__":
    unittest.main()
