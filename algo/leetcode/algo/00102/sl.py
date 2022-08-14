"""

[102] Binary Tree Level Order Traversal


Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).


--------------------------------------------------

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]


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
	-1000 <= Node.val <= 1000


################################################################


102. 二叉树的层序遍历
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。



示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]


示例 3：
输入：root = []
输出：[]


提示：

* 树中节点数目在范围 [0, 2000] 内
* -1000 <= Node.val <= 1000



"""

import queue
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.val}>"


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return []

        queue = [(root, 0)]
        while queue:
            cur, level = queue.pop(0)
            if level == len(ans):
                ans.append([cur.val])
            else:
                ans[level].append(cur.val)

            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))

        return ans


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        #      1
        #   2    3
        #       7  8

        n1 = TreeNode(1)
        n2 = TreeNode(3)
        n2.left = TreeNode(7)
        n2.right = TreeNode(8)

        n1.left = TreeNode(2)
        n1.right = n2

        root = n1

        self.assertEqual(self.sl.levelOrder(root), [[1], [2, 3], [7, 8]])


if __name__ == "__main__":
    unittest.main()
