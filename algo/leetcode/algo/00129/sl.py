"""

[129] Sum Root to Leaf Numbers


You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.


	For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.


Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.


--------------------------------------------------

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.


--------------------------------------------------

Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.



Constraints:


	The number of nodes in the tree is in the range [1, 1000].
	0 <= Node.val <= 9
	The depth of the tree will not exceed 10.

################################################################


129. 求根节点到叶节点数字之和
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。



示例 1：
         1
       2   3

输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25


示例 2：
        4
     9    0
   5   1

输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026


提示：

树中节点的数目在范围 [1, 1000] 内
0 <= Node.val <= 9
树的深度不超过 10

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
    def process(self, root, pre):
        if root is None:
            return

        pre = pre * 10 + root.val
        # 来到叶子节点
        if root.left is None and root.right is None:
            self.ans += pre
            return

        self.process(root.left, pre)
        self.process(root.right, pre)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.process(root, 0)
        return self.ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):

        """
          1
        2   3

        """
        n1 = TreeNode(1)
        n1.left = TreeNode(2)
        n1.right = TreeNode(3)
        n1.log()
        self.assertEqual(
            self.sl.sumNumbers(n1),
            25,
        )

    def test_sl2(self):
        """
             4
          9    0
        5   1

        """
        n1 = TreeNode(4)
        n1.left = TreeNode(9)
        n1.left.left = TreeNode(5)
        n1.left.right = TreeNode(1)
        n1.right = TreeNode(0)
        n1.log()
        self.assertEqual(
            self.sl.sumNumbers(n1),
            1026,
        )


if __name__ == "__main__":
    unittest.main()
