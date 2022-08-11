"""

958. 二叉树的完全性检验
给定一个二叉树的 root ，确定它是否是一个 完全二叉树 。

在一个 完全二叉树 中，除了最后一个关卡外，所有关卡都是完全被填满的，并且最后一个关卡中的所有节点都是尽可能靠左的。它可以包含 1 到 2h 节点之间的最后一级 h 。



示例 1：

     1
  2    3
4  5  6

输入：root = [1,2,3,4,5,6]
输出：true
解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。


示例 2：
     1
  2    3
4  5    7


输入：root = [1,2,3,4,5,null,7]
输出：false
解释：值为 7 的结点没有尽可能靠向左侧。


提示：

树的结点数在范围  [1, 100] 内。
1 <= Node.val <= 1000

"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.val}>"


"""
广度优先遍历二叉树，完全二叉树需要满足如下两个条件：
1. 如果一个节点只有一个子节点，一旦出现有右无左，返回 False
2. 如果一旦出现一个节点子节点小于等于1，则后面遍历的所有节点一定都是叶子点，
否则返回 False
"""


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        flag = False

        while queue:
            cur = queue.pop(0)
            L = cur.left
            R = cur.right
            if flag and (L is not None or R is not None):
                return False

            if L is None and R is not None:
                return False

            if L is None or R is None:
                flag = True

            if L:
                queue.append(L)
            if R:
                queue.append(R)

        return True


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

        # self.assertEqual(self.sl.isCompleteTree(root), False)

        #      1
        #   2    3
        # 4  5  6

        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n2.left = TreeNode(4)
        n2.right = TreeNode(5)
        n3 = TreeNode(3)
        n1.left = n2
        n1.right = n3
        n3.left = TreeNode(6)
        root = n1

        self.assertEqual(self.sl.isCompleteTree(root), True)

        #      1
        #   2    3
        # 4  5    7

        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n2.left = TreeNode(4)
        n2.right = TreeNode(5)
        n3 = TreeNode(3)
        n3.right = TreeNode(7)
        n1.left = n2
        n1.right = n3
        root = n1

        self.assertEqual(self.sl.isCompleteTree(root), False)


if __name__ == "__main__":
    unittest.main()
