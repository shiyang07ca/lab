"""

[889] Construct Binary Tree from Preorder and Postorder Traversal


Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.


--------------------------------------------------

Example 1:


Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]


--------------------------------------------------

Example 2:


Input: preorder = [1], postorder = [1]
Output: [1]



Constraints:


	1 <= preorder.length <= 30
	1 <= preorder[i] <= preorder.length
	All the values of preorder are unique.
	postorder.length == preorder.length
	1 <= postorder[i] <= postorder.length
	All the values of postorder are unique.
	It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

################################################################


889. 根据前序和后序遍历构造二叉树
给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。

如果存在多个答案，您可以返回其中 任何 一个。



示例 1：

           1
        2     3
       4 5   6  7

输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]


示例 2:

输入: preorder = [1], postorder = [1]
输出: [1]


提示：

1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
preorder 中所有值都 不同
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
postorder 中所有值都 不同
保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历

"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.val}>"


class Solution:
    def build(self, preorder, postorder, prel, prer, postl, postr):
        if prel > prer or postl > postr:
            return None

        # 注意处理prel, prer 越界的情况
        if prel == prer:
            return TreeNode(preorder[prel])

        root_val = postorder[postr]
        root = TreeNode(root_val)
        # left_root_val 表示左子树的根节点，根据 post 数组位置映射，找到
        # 左子树根节点在 post 数组中的位置
        left_root_val = preorder[prel + 1]
        left_root_index = self.post_val_index[left_root_val]
        left_size = left_root_index - postl + 1

        root.left = self.build(
            preorder,
            postorder,
            prel + 1,
            prel + left_size,
            postl,
            left_root_index,
        )
        root.right = self.build(
            preorder,
            postorder,
            prel + left_size + 1,
            prer,
            left_root_index + 1,
            postr - 1,
        )

        return root

    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        self.post_val_index = {}
        for i, val in enumerate(postorder):
            self.post_val_index[val] = i

        return self.build(
            preorder, postorder, 0, len(preorder) - 1, 0, len(postorder) - 1
        )


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """

            1
         2     3
        4 5   6  7

        """
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n2.left = TreeNode(4)
        n2.right = TreeNode(5)
        n3 = TreeNode(3)
        n3.left = TreeNode(6)
        n3.right = TreeNode(7)

        n1.left = n2
        n1.right = n3

        root = n1

        preorder = [1, 2, 4, 5, 3, 6, 7]
        postorder = [4, 5, 2, 6, 7, 3, 1]

        print(self.sl.constructFromPrePost(preorder, postorder))


if __name__ == "__main__":
    unittest.main()
