"""

[968] Binary Tree Cameras


You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.


--------------------------------------------------

Example 1:


Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.


--------------------------------------------------

Example 2:


Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.



Constraints:


	The number of nodes in the tree is in the range [1, 1000].
	Node.val == 0


################################################################


968. 监控二叉树
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视其父对象、自身及其直接子对象。

计算监控树的所有节点所需的最小摄像头数量。



示例 1：

         0
      x
    0   0


输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。



示例 2：

              0
            x
          0
        x
         0


输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

提示：

给定树的节点数的范围是 [1, 1000]。
每个节点的值都是 0。
通过次数44,509提交次数85,759

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
    def process(self, root):
        if root is None:
            return 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        return self.process(root)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
             0
          x
        0   0

        """
        n1 = TreeNode(0)
        n1.left = TreeNode(0)
        n1.left.left = TreeNode(0)
        n1.left.right = TreeNode(0)
        n1.log()
        self.assertEqual(
            self.sl.minCameraCover(n1),
            1,
        )

    def test_sl2(self):
        """

              0
            x
          0
        x
         0

        """
        n1 = TreeNode(0)
        n1.left = TreeNode(0)
        n1.left.left = TreeNode(0)
        n1.left.left.left = TreeNode(0)
        n1.left.left.left.right = TreeNode(0)
        n1.log()
        self.assertEqual(
            self.sl.minCameraCover(n1),
            2,
        )


if __name__ == "__main__":
    unittest.main()
