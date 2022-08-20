"""

[652] Find Duplicate Subtrees


Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.


--------------------------------------------------

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]


--------------------------------------------------

Example 2:


Input: root = [2,1,1]
Output: [[1]]


--------------------------------------------------

Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]



Constraints:


	The number of the nodes in the tree will be in the range [1, 10^4]
	-200 <= Node.val <= 200

################################################################

652. 寻找重复的子树
给定一棵二叉树 root，返回所有重复的子树。

对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

如果两棵树具有相同的结构和相同的结点值，则它们是重复的。



示例 1：

             1
         2        3
      4        2     4
             4


输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]


示例 2：

          2
       1    1

输入：root = [2,1,1]
输出：[[1]]


示例 3：

         2
      2     2
    3     3

输入：root = [2,2,2,3,null,3,null]
输出：[[2,3],[3]]


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.val}>"

    def __eq__(self, other):
        return self.val == other.val


from typing import *


class Solution:
    def isSameTree(self, n1, n2):
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None:
            return False

        if n1.val != n2.val:
            return False
        return self.isSameTree(n1.left, n2.left) and self.isSameTree(n1.right, n2.right)

    # 暴力解法，超时
    def bf(self, root):
        stack1, stack2 = [root], []
        while stack1:
            cur = stack1.pop()
            stack2.append(cur)
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)

        all_nodes = []
        while stack2:
            all_nodes.append(stack2.pop())

        visit = [False] * len(all_nodes)
        ans = []
        for i in range(0, len(all_nodes) - 1):
            for j in range(i + 1, len(all_nodes) - 1):
                if self.isSameTree(all_nodes[i], all_nodes[j]):
                    if not visit[i]:
                        ans.append(all_nodes[i])
                        visit[i] = visit[j] = True
                    else:
                        visit[j] = True

        return ans

    def traverse(self, root):
        if root is None:
            return "#"

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        sub_tree = f"{left},{right},{root.val}"
        # print(f"sub: {sub_tree}")
        # 要求 sub_tree 只出现过一次
        # 只有当 freq 等于 1 时，才将其加入到结果中
        freq = self.memo.get(sub_tree, 0)
        if freq == 1:
            self.ans.append(root)

        self.memo[sub_tree] = freq + 1
        return sub_tree

    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        # return self.bf(root)
        self.ans = []
        self.memo = {}
        self.traverse(root)
        return self.ans


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """

               1
           2        3
        4        2     4
               4

        """

        n1 = TreeNode(1)
        n2 = TreeNode(2)
        n2.left = TreeNode(4)

        n3 = TreeNode(3)
        n4 = TreeNode(2)
        n4.left = TreeNode(4)
        n3.left = n4
        n3.right = TreeNode(4)

        n1.left = n2
        n1.right = n3

        root = n1

        print(self.sl.findDuplicateSubtrees(root))

        """

               0
           0        0
        0             0
       0 0           0  0

        """
        n1 = TreeNode(0)
        n1.left = TreeNode(0)
        n1.right = TreeNode(0)
        n2 = TreeNode(0)
        n2.left = n1

        n3 = TreeNode(0)
        n3.left = TreeNode(0)
        n3.right = TreeNode(0)
        n4 = TreeNode(0)
        n4.right = n3

        n5 = TreeNode(0)
        n5.left = n2
        n5.right = n4

        root = n5

        print(self.sl.findDuplicateSubtrees(root))


if __name__ == "__main__":
    unittest.main()
