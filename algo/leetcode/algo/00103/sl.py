"""

[103] Binary Tree Zigzag Level Order Traversal


Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).


--------------------------------------------------

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]


--------------------------------------------------

Example 2:


Input: root = [1]
Output: [[1]]


--------------------------------------------------

Example 3:


Input: root = []
Output: []



Constraints:


	The number of nodes in the tree is in the range [0, 2000].
	-100 <= Node.val <= 100

################################################################



103. 二叉树的锯齿形层序遍历
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。



示例 1：

          3
      9       20
          15      7


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]


示例 2：

输入：root = [1]
输出：[[1]]


示例 3：

输入：root = []
输出：[]


提示：

树中节点数目在范围 [0, 2000] 内
-100 <= Node.val <= 100

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        ans = []
        queue = [root]
        level = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if i == 0:
                    ans.append([cur.val])
                else:
                    if level % 2 == 0:
                        ans[-1].append(cur.val)
                    else:
                        ans[-1].insert(0, cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            level += 1

        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
            3
        9       20
            15      7
        """
        n1 = TreeNode(3)
        n1.left = TreeNode(9)
        n1.right = TreeNode(20)
        n1.right.left = TreeNode(15)
        n1.right.right = TreeNode(7)
        n1.log()
        print(self.sl.zigzagLevelOrder(n1))
        self.assertEqual(
            self.sl.zigzagLevelOrder(n1),
            [[3], [20, 9], [15, 7]],
        )

    def test_sl2(self):
        """
              1
          2       3
        4           5
        """
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.left.left = TreeNode(4)
        n1.right = TreeNode(3)
        n1.right.right = TreeNode(5)
        n1.log()
        self.assertEqual(self.sl.zigzagLevelOrder(n1), [[1], [3, 2], [4, 5]])


if __name__ == "__main__":
    unittest.main()
