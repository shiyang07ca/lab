"""

[222] Count Complete Tree Nodes


Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.


--------------------------------------------------

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6


--------------------------------------------------

Example 2:


Input: root = []
Output: 0


--------------------------------------------------

Example 3:


Input: root = [1]
Output: 1



Constraints:


	The number of nodes in the tree is in the range [0, 5 * 10⁴].
	0 <= Node.val <= 5 * 10⁴
	The tree is guaranteed to be complete.

################################################################

222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。



示例 1：

          1
       2    3
     4  5  6


输入：root = [1,2,3,4,5,6]
输出：6


示例 2：

输入：root = []
输出：0
示例 3：

输入：root = [1]
输出：1


提示：

树中节点的数目范围是[0, 5 * 104]
0 <= Node.val <= 5 * 104
题目数据保证输入的树是 完全二叉树


进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？

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
    def tranverse_count(self, root):
        stack = [root]
        count = 0
        while stack:
            cur = stack.pop()
            count += 1
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return count

    # 首先，求整个二叉树的高度：一直往左遍历，
    # 到叶子节点的高度就是完全二叉树的高度。
    #
    # 然后看当前节点一直向右边遍历，得到右子树的高度
    #
    # 如果左子树高度等于右子树高度，则以当前节点为根的树一定是满二叉树
    # ans = (左子树高度^ 2 - 1)
    # 否则
    # 递归求解 ans = r(左子树) + 1 + (右子树)
    def recur_count(self, root):
        if root is None:
            return 0

        lh, rh = 0, 0
        node = root.left
        while node:
            lh += 1
            node = node.left

        node = root.right
        while node:
            rh += 1
            node = node.right

        if lh == rh:
            return 2 ** (lh + 1) - 1

        return self.recur_count(root.left) + 1 + self.recur_count(root.right)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # return self.tranverse_count(root)
        return self.recur_count(root)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        #      1
        #   2    3
        # 4  5  6

        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n2.left = TreeNode(4)
        n2.right = TreeNode(5)
        n3 = TreeNode(3)
        n3.left = TreeNode(6)

        n1.left = n2
        n1.right = n3

        root = n1

        self.assertEqual(
            self.sl.countNodes(root),
            6,
        )


if __name__ == "__main__":
    unittest.main()
