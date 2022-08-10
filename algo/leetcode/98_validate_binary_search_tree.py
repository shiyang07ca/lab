"""

给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。


示例 1：

      2
    /   \
   1     3

输入：root = [2,1,3]
输出：true

示例 2：

      5
    /   \
   1     4
       /   \
      3     6

输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node<{self.val}>"


import math


# 中序遍历，如果不满足单调性，返回 False，其他所有情况返回 True
class Solution:
    def iter_root(self, root):
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if node.val <= self.pre:
                    return False
                else:
                    self.pre = node.val
                root = node.right

        return True

    def recur_root(self, root):
        if root is None:
            return True

        if not self.recur_root(root.left):
            return False

        if root.val <= self.pre:
            return False
        else:
            self.pre = root.val

        if not self.recur_root(root.right):
            return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre = -math.inf
        # return self.recur_root(root)

        return self.iter_root(root)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):

        #    2
        #  /   \
        # 1     3

        n1 = TreeNode(2)
        n1.left = TreeNode(1)
        n1.right = TreeNode(3)
        root = n1

        self.assertEqual(self.sl.isValidBST(root), True)

        #    5
        #  /   \
        # 1     4
        #     /   \
        #    3     6

        n1 = TreeNode(5)
        n2 = TreeNode(4)
        n2.left = TreeNode(3)
        n2.right = TreeNode(6)

        n1.left = TreeNode(1)
        n1.right = n2

        root = n1
        self.assertEqual(self.sl.isValidBST(root), False)


if __name__ == "__main__":
    unittest.main()
