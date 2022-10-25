"""

[199] Binary Tree Right Side View


Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.


--------------------------------------------------

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]


--------------------------------------------------

Example 2:


Input: root = [1,null,3]
Output: [1,3]


--------------------------------------------------

Example 3:


Input: root = []
Output: []



Constraints:


	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100


################################################################


199. 二叉树的右视图
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。



示例 1:

           1   <==
        2     3  <==
         5     4  <==

输入: [1,2,3,null,5,null,4]
输出: [1,3,4]


示例 2:

输入: [1,null,3]
输出: [1,3]


示例 3:

输入: []
输出: []


提示:

二叉树的节点个数的范围是 [0,100]
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


from algo.tree.builder import *


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        ans = []
        queue = [root]
        while queue:
            last = None
            for _ in range(len(queue)):
                cur = queue.pop(0)
                last = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(last)

        return ans


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
           1   <==
        2     3  <==
         5     4  <==

        """
        n1 = TreeNode(1)
        n1.right = TreeNode(3)
        n1.right.right = TreeNode(4)

        n1.left = TreeNode(2)
        n1.left.right = TreeNode(5)
        n1.log()
        self.assertEqual(
            self.sl.rightSideView(n1),
            [1, 3, 4],
        )


if __name__ == "__main__":
    unittest.main()
