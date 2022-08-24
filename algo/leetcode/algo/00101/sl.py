"""

[101] Symmetric Tree


Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


--------------------------------------------------

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true


--------------------------------------------------

Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false



Constraints:


	The number of nodes in the tree is in the range [1, 1000].
	-100 <= Node.val <= 100



Follow up: Could you solve it both recursively and iteratively?


################################################################


101. 对称二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。



示例 1：

              1
           2     2
         3  4   4 3

输入：root = [1,2,2,3,4,4,3]
输出：true


示例 2：
            1
         2     2
          3      3

输入：root = [1,2,2,null,3,null,3]
输出：false


提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100




"""

from typing import *

import sys
import inspect
import os
from os.path import abspath, join, dirname


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import TreeNode


class Solution:
    # recur
    def compare1(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        else:
            return (
                node1.val == node2.val
                and self.compare1(node1.left, node2.right)
                and self.compare1(node1.right, node2.left)
            )

    # iter
    def compare2(self, root):

        queue = [root.left, root.right]
        while queue:
            print(queue)
            n1 = queue.pop(0)
            n2 = queue.pop(0)
            if n1 is None and n2 is None:
                continue

            if n1 is None or n2 is None or n1.val != n2.val:
                return False

            queue.append(n1.left)
            queue.append(n2.right)
            queue.append(n1.right)
            queue.append(n2.left)

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # return self.compare1(root.left, root.right)

        return self.compare2(root)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
             1
          2     2
        3  4   4  3

        """
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.left.left = TreeNode(3)
        n1.left.right = TreeNode(4)
        n1.right = TreeNode(2)
        n1.right.left = TreeNode(4)
        n1.right.right = TreeNode(3)
        n1.log()
        self.assertEqual(
            self.sl.isSymmetric(n1),
            True,
        )

        """
            1
         2     2
          3      3
        """
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.left.right = TreeNode(3)
        n1.right = TreeNode(2)
        n1.right.right = TreeNode(3)
        n1.log()
        self.assertEqual(
            self.sl.isSymmetric(n1),
            False,
        )


if __name__ == "__main__":
    unittest.main()
