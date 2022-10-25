"""

[450] Delete Node in a BST


Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:


	Search for a node to remove.
	If the node is found, delete the node.



--------------------------------------------------

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.



--------------------------------------------------

Example 2:


Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.


--------------------------------------------------

Example 3:


Input: root = [], key = 0
Output: []



Constraints:


	The number of nodes in the tree is in the range [0, 10⁴].
	-10⁵ <= Node.val <= 10⁵
	Each node has a unique value.
	root is a valid binary search tree.
	-10⁵ <= key <= 10⁵



Follow up: Could you solve it with time complexity O(height of tree)?


################################################################


450. 删除二叉搜索树中的节点

给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。


示例 1:

          5                                  5
      3       6         =>              4        6
    2   4        7                   2             7



输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

                    5
                 2    6
                   4   7
另一个正确答案是 [5,2,6,null,4,null,7]。


示例 2:

输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点
示例 3:

输入: root = [], key = 0
输出: []


提示:

节点数的范围 [0, 104].
-105 <= Node.val <= 105
节点值唯一
root 是合法的二叉搜索树
-105 <= key <= 105


进阶： 要求算法时间复杂度为 O(h)，h 为树的高度

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


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return

        if key == root.val:
            # 分三种情况讨论
            # 如果当前节点是叶子节点，原地去世
            if root.left is None and root.right is None:
                return None
            # 如果当前节点只有一个孩子
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # 如果左右节点都有孩子，需要找到左孩子的最大值或右孩子的最小值，
            # 来替换当前根节点
            # 需要把找到的节点放到 root 上，同时 *删除* 找到的节点
            else:
                cur = root.left
                while cur.right is not None:
                    cur = cur.right
                root.val = cur.val
                # 注意：递归删除找到的节点
                root.left = self.deleteNode(root.left, cur.val)
                return root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        return root


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):

        """

              5                                  5
          3       6         =>              4        6
        2   4        7                   2              7


        """
        n1 = TreeNode(5)
        n2 = TreeNode(3)
        n2.left = TreeNode(2)
        n2.right = TreeNode(4)
        n3 = TreeNode(6)
        n3.right = TreeNode(7)
        n1.left = n2
        n1.right = n3

        n1.log()

        n1 = self.sl.deleteNode(n1, 3)
        n1.log()

    def test_sl2(self):

        n1 = TreeNode(5)
        n2 = TreeNode(3)
        n2.left = TreeNode(2)
        n2.right = TreeNode(4)
        n3 = TreeNode(6)
        n3.right = TreeNode(7)
        n1.left = n2
        n1.right = n3

        n1 = self.sl.deleteNode(n1, 5)
        n1.log()


if __name__ == "__main__":
    unittest.main()
