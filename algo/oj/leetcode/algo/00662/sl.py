"""

[662] Maximum Width of Binary Tree


Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.


--------------------------------------------------

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).


--------------------------------------------------

Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).


--------------------------------------------------

Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).



Constraints:


	The number of nodes in the tree is in the range [1, 3000].
	-100 <= Node.val <= 100


################################################################


662. 二叉树最大宽度
给你一棵二叉树的根节点 root ，返回树的 最大宽度 。

树的 最大宽度 是所有层中最大的 宽度 。

每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。

题目数据保证答案将会在  32 位 带符号整数范围内。



示例 1：


输入：root = [1,3,2,5,3,null,9]
输出：4
解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。

           1
        3     2
      5  3      9


示例 2：

           1
         3   2
       5       9
     6        7


输入：root = [1,3,2,5,null,null,9,6,null,7]
输出：7
解释：最大宽度出现在树的第 4 层，宽度为 7 (6,null,null,null,null,null,7) 。


示例 3：

         1
       3   2
     5


输入：root = [1,3,2,5]
输出：2
解释：最大宽度出现在树的第 2 层，宽度为 2 (3,2) 。


提示：

树中节点的数目范围是 [1, 3000]
-100 <= Node.val <= 100

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
    def getTreeDepth(self, root):
        if root is None:
            return 0

        ans = 0
        queue = [(root, 0)]
        while queue:
            cur, level = queue.pop()
            ans = max(ans, level)

            if cur.left:
                queue.append((cur.left, level + 1))
            if cur.right:
                queue.append((cur.right, level + 1))

        return ans

    # 超时
    def bfs(self, root: Optional[TreeNode]) -> int:
        # 层序遍历，补全非叶子节点，得到每一层元素，包括空值

        queue = [(root, 0)]
        nodes = []
        nodes_size = []
        depth = self.getTreeDepth(root)
        while queue:
            cur, level = queue.pop(0)
            if level == len(nodes):
                if cur.val != "NULL":
                    nodes.append([cur.val])
                    nodes_size.append(1)
                    # nodes.append(1)
            else:
                nodes[level].append(cur.val)
                if cur.val != "NULL":
                    nodes_size[level] = len(nodes[level])

            # 如果当前节点来到最后一层
            # 就是是叶子节点，什么也不做
            # print(cur, level, depth)
            if level == depth:
                continue

            if cur.left is None:
                cur.left = TreeNode("NULL")
            queue.append((cur.left, level + 1))
            if cur.right is None:
                cur.right = TreeNode("NULL")
            queue.append((cur.right, level + 1))

        # print(f"nodes: {nodes}, {nodes_size}")

        return max(nodes_size)

    # Time comlexity: O(n)
    # Space complexity: O(h)
    def dfs(self, root, depth, id_):
        if root is None:
            return 0
        # id_ 是当前节点的偏移量，包括为空值的节点编号

        # 来到了新的一层，最左边节点编号作为当前层的最小值
        if len(self.ids) == depth:
            self.ids.append(id_)

        # 这个二叉树相当于一个完全二叉树(complete),
        # 左右子树节点编号相当于堆的计算方式
        # 最大宽度就是当前节点的偏移量（宽度）和左右子树最大宽度中的最大值
        rootid = id_ - self.ids[depth]
        return max(
            rootid + 1,
            max(
                self.dfs(root.left, depth + 1, rootid * 2),
                self.dfs(root.right, depth + 1, rootid * 2 + 1),
            ),
        )

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # return self.bfs(root)

        # ids 表示每一层节点编号的最小值
        self.ids = []
        return self.dfs(root, 0, 0)


import unittest


def build(data):
    if len(data) == 0:
        return TreeNode(0)
    nodeQueue = []
    # 创建一根节点，并将根节点进栈
    root = TreeNode(data[0])
    nodeQueue.append(root)
    # 记录当前行节点的数量
    lineNum = 2
    # 记录当前行中数字在数组中的位置
    startIndex = 1
    # 记录数组中剩余元素的数量
    restLength = len(data) - 1
    while restLength > 0:
        for index in range(startIndex, startIndex + lineNum, 2):
            if index == len(data):
                return root
            cur_node = nodeQueue.pop()
            if data[index] is not None:
                cur_node.left = TreeNode(data[index])
                nodeQueue.append(cur_node.left)
            if index + 1 == len(data):
                return root
            if data[index + 1] is not None:
                cur_node.right = TreeNode(data[index + 1])
                nodeQueue.append(cur_node.right)
        startIndex += lineNum
        restLength -= lineNum
        # 此处用来更新下一层树对应节点的最大值
        lineNum = len(nodeQueue) * 2
    return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
             1
          3     2
        5  3      9

        """
        n1 = TreeNode(1)
        n2 = TreeNode(3)
        n2.left = TreeNode(5)
        n2.right = TreeNode(3)
        n3 = TreeNode(2)
        n3.right = TreeNode(9)
        n1.left = n2
        n1.right = n3
        n1.log()
        self.assertEqual(
            self.sl.widthOfBinaryTree(n1),
            4,
        )
        """

           1
         3   2
       5       9
     6        7

        """
        n1 = TreeNode(1)
        n2 = TreeNode(3)
        n2.left = TreeNode(5)
        n2.left.left = TreeNode(6)
        n3 = TreeNode(2)
        n3.right = TreeNode(9)
        n3.right.left = TreeNode(7)
        n1.left = n2
        n1.right = n3
        n1.log()
        self.assertEqual(
            self.sl.widthOfBinaryTree(n1),
            7,
        )

        # self.sl.widthOfBinaryTree(n1)
        # n1.log()

        data = [
            0,
            0,
            0,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
            None,
            0,
            0,
            None,
        ]

        # root = build(data)
        # root.log()


if __name__ == "__main__":
    unittest.main()
