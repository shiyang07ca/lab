"""

[99] Recover Binary Search Tree


You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.


--------------------------------------------------

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.


--------------------------------------------------

Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.



Constraints:


	The number of nodes in the tree is in the range [2, 1000].
	-2³¹ <= Node.val <= 2³¹ - 1



Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?

################################################################


# TODO

99. 恢复二叉搜索树


给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。


示例 1：
         1                             3
     3                =>            1
      2                              2


输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。


示例 2：

         3                             2
     1       4         =>          1       4
           2                              3


输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。


提示：

树上节点的数目在范围 [2, 1000] 内
-231 <= Node.val <= 231 - 1


进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *
from itertools import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # oj
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *

"""
中序遍历，再找出两个节点
"""


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            arr.append(node)
            dfs(node.right)

        arr = []
        dfs(root)
        # print(arr)
        x = y = None
        for a, b in pairwise(arr):
            if not x and a.val >= b.val:
                x = a
            if x and a.val >= b.val:
                y = b

            # print(a.val, b.val)
        # print(x, y)
        x.val, y.val = y.val, x.val


# 迭代
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        x = y = None
        pre = TreeNode(float("-inf"))

        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
                continue
            else:
                node = stack.pop()

            if not x and pre.val > node.val:
                x = pre
            if x and pre.val > node.val:
                y = node
            pre = node
            root = node.right
        x.val, y.val = y.val, x.val


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        n1 = TreeNode(1)
        n1.left = TreeNode(3)
        n1.left.right = TreeNode(2)
        n1.log()
        print("################")
        self.sl.recoverTree(n1)
        n1.log()
        print("################")

    def test_sl2(self):
        n1 = TreeNode(3)
        n1.left = TreeNode(1)
        n1.right = TreeNode(4)
        n1.right.left = TreeNode(2)
        n1.log()
        print("################")
        self.sl.recoverTree(n1)
        n1.log()
        print("################")


if __name__ == "__main__":
    unittest.main()
