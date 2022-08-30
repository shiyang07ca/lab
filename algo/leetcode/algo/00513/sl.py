"""

[513] Find Bottom Left Tree Value


Given the root of a binary tree, return the leftmost value in the last row of the tree.


--------------------------------------------------

Example 1:


Input: root = [2,1,3]
Output: 1


--------------------------------------------------

Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7



Constraints:


	The number of nodes in the tree is in the range [1, 10⁴].
	-2³¹ <= Node.val <= 2³¹ - 1

################################################################


513. 找树左下角的值
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。



示例 1:

     2
   1   3

输入: root = [2,1,3]
输出: 1


示例 2:
            1
        2     3
      4      5    6
           7


输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7


提示:

二叉树的节点个数的范围是 [1,104]
-231 <= Node.val <= 231 - 1

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return level[0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
          2
        1   3
        """
        n1 = TreeNode(2)
        n1.left = TreeNode(1)
        n1.right = TreeNode(3)
        n1.log()
        self.assertEqual(
            self.sl.findBottomLeftValue(n1),
            1,
        )

    def test_sl2(self):
        """
              1
          2      3
        4      5    6
             7

        """
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.left.left = TreeNode(4)
        n1.right = TreeNode(3)
        n1.right.left = TreeNode(5)
        n1.right.right = TreeNode(6)
        n1.right.left.left = TreeNode(7)
        n1.log()
        self.assertEqual(
            self.sl.findBottomLeftValue(n1),
            7,
        )


if __name__ == "__main__":
    unittest.main()
