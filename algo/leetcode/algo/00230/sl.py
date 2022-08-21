"""

[230] Kth Smallest Element in a BST


Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


--------------------------------------------------

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1


--------------------------------------------------

Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3



Constraints:


	The number of nodes in the tree is n.
	1 <= k <= n <= 10⁴
	0 <= Node.val <= 10⁴



Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


################################################################


230. 二叉搜索树中第K小的元素
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。



示例 1：
              3
          1       4
            2

输入：root = [3,1,4,null,2], k = 1
输出：1


示例 2：

                    5
              3           6
           2     4
         1


输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3


提示：

树中的节点数为 n 。
1 <= k <= n <= 104
0 <= Node.val <= 104


进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？

"""


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

from typing import *

import unittest


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # 中序遍历
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                k -= 1
                # print(k, node.val)
                if k == 0:
                    return node.val
                root = node.right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
              3
          1       4
            2

        """
        n1 = TreeNode(3)
        n2 = TreeNode(1)
        n2.right = TreeNode(2)
        n1.left = n2
        n1.right = TreeNode(4)

        root = n1
        root.log()
        self.assertEqual(
            self.sl.kthSmallest(root, 1),
            1,
        )

        """

                    5
              3           6
           2     4
         1

        """
        n1 = TreeNode(5)

        n2 = TreeNode(3)
        n3 = TreeNode(2)
        n3.left = TreeNode(1)
        n2.right = TreeNode(4)
        n2.left = n3

        n1.left = n2
        n1.right = TreeNode(6)

        root = n1
        root.log()
        self.assertEqual(
            self.sl.kthSmallest(root, 3),
            3,
        )



if __name__ == "__main__":
    unittest.main()
