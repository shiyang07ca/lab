"""

[1302] Deepest Leaves Sum


Given the root of a binary tree, return the sum of values of its deepest leaves.

--------------------------------------------------

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15


--------------------------------------------------

Example 2:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19



Constraints:


	The number of nodes in the tree is in the range [1, 10⁴].
	1 <= Node.val <= 100

################################################################


给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。



示例 1：

          1
       2    3
     4  5     6
   7            8


输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
示例 2：

输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：19


提示：

树中节点数目在范围 [1, 104] 之间。
1 <= Node.val <= 100

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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            last_level = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                last_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return sum(last_level)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """

               1
            2    3
          4  5     6
        7            8

        """
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.left.left = TreeNode(4)
        n1.left.right = TreeNode(5)
        n1.left.left.left = TreeNode(7)
        n1.right = TreeNode(3)
        n1.right.right = TreeNode(6)
        n1.right.right.right = TreeNode(8)
        n1.log()

        self.assertEqual(
            self.sl.deepestLeavesSum(n1),
            15,
        )


if __name__ == "__main__":
    unittest.main()
