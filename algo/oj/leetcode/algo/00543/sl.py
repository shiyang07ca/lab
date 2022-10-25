"""

[543] Diameter of Binary Tree


Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.


--------------------------------------------------

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


--------------------------------------------------

Example 2:


Input: root = [1,2]
Output: 1



Constraints:


	The number of nodes in the tree is in the range [1, 10⁴].
	-100 <= Node.val <= 100


################################################################

543. 二叉树的直径
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。



示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。



注意：两结点之间的路径长度是以它们之间边的数目表示。



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
    # 返回两个信息：
    # 当前节点的高度
    # 以当前节点 x 为根节点的最大距离
    # 分两种情况：
    # 最大距离跨过 x：最大距离 = x.left 高度 + x.right 高度
    #
    #                    1   ==> x
    #                 2    3
    #                4 5

    # 最大距离不跨过 x：最大距离 = max(x.left 最大距离, x.right 最大距离)
    #
    #                  1 ===> x
    #              2       3
    #           4    6
    #         5        7
    #

    def recur(self, root):
        if root is None:
            return 0, 0

        l_h, l_max_dis = self.recur(root.left)
        r_h, r_max_dis = self.recur(root.right)

        height = max(l_h, r_h) + 1
        max_dis = max(max(l_max_dis, r_max_dis), l_h + r_h)

        return height, max_dis

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.recur(root)[1]


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        #      1
        #   2    3
        #       7  8

        n1 = TreeNode(1)
        n2 = TreeNode(3)
        n2.left = TreeNode(7)
        n2.right = TreeNode(8)

        n1.left = TreeNode(2)
        n1.right = n2

        root = n1

        self.assertEqual(
            self.sl.diameterOfBinaryTree(root),
            3,
        )


if __name__ == "__main__":
    unittest.main()
