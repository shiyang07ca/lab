"""

[236] Lowest Common Ancestor of a Binary Tree


Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


--------------------------------------------------

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.


--------------------------------------------------

Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


--------------------------------------------------

Example 3:


Input: root = [1,2], p = 1, q = 2
Output: 1



Constraints:


	The number of nodes in the tree is in the range [2, 10⁵].
	-10⁹ <= Node.val <= 10⁹
	All Node.val are unique.
	p != q
	p and q will exist in the tree.


################################################################


236. 二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”



示例 1：

           3
      5        1
    6   2    0   8
       7 4

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。


示例 2：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：

输入：root = [1,2], p = 1, q = 2
输出：1


提示：

树中节点数目在范围 [2, 105] 内。
-109 <= Node.val <= 109
所有 Node.val 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。

"""

from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.val}>"

    def __eq__(self, other):
        return self.val == other.val


class Solution:
    def find(self, root, p, q):
        if root is None:
            return None

        # 如果当前节点的值等于 p 或 q，则找到了节点????
        if root.val == p.val or root.val == q.val:
            return root

        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)
        # 在 root 的左子树和右子树分别找到了 p 和 q
        if left is not None and right is not None:
            return root

        return left if left is not None else right

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        return self.find(root, p, q)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
               3
          5        1
        6   2    0   8
           7 4

        """
        n0 = TreeNode(0)
        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n3 = TreeNode(3)
        n4 = TreeNode(4)
        n5 = TreeNode(5)
        n6 = TreeNode(6)
        n7 = TreeNode(7)
        n8 = TreeNode(8)

        n2.left = n7
        n2.right = n4
        n5.left = n6
        n5.right = n2
        n1.left = n0
        n1.right = n8
        n3.left = n5
        n3.right = n1
        root = n3

        print(n3 == TreeNode(3))

        self.assertEqual(
            self.sl.lowestCommonAncestor(root, n5, n1),
            n3,
        )

        """
               3
          5        1
        6   2    0   8
           7 4

        """


if __name__ == "__main__":
    unittest.main()
