"""

[116] Populating Next Right Pointers in Each Node


You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:


struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}


Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


--------------------------------------------------

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


--------------------------------------------------

Example 2:


Input: root = []
Output: []



Constraints:


	The number of nodes in the tree is in the range [0, 2¹² - 1].
	-1000 <= Node.val <= 1000



Follow-up:


	You may only use constant extra space.
	The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.


################################################################

116. 填充每个节点的下一个右侧节点指针
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。



示例 1：
           1                           1         -> NULL
      2        3        =>       2    ->    3    -> NULL
   4   5     6   7            4 -> 5 ->  6 -> 7  -> NULL

输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。



示例 2:

输入：root = []
输出：[]


提示：

树中节点的数量在 [0, 212 - 1] 范围内
-1000 <= node.val <= 1000


进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

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


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if root is None:
            return

        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                level.append(cur)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            for i, e in enumerate(level[:-1]):
                e.next = level[i + 1]

            level[-1].next = None

        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        pass


if __name__ == "__main__":
    unittest.main()
