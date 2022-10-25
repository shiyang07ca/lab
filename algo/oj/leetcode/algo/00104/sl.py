"""

[104] Maximum Depth of Binary Tree


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


--------------------------------------------------

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3


--------------------------------------------------

Example 2:


Input: root = [1,null,2]
Output: 2



Constraints:


	The number of nodes in the tree is in the range [0, 10⁴].
	-100 <= Node.val <= 100

104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ans = 0
        queue = [(root, 1)]
        while queue:
            cur, level = queue.pop()
            ans = max(ans, level)

            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))

        return ans


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
            self.sl.maxDepth(root),
            3,
        )


if __name__ == "__main__":
    unittest.main()
