"""

[297] Serialize and Deserialize Binary Tree


Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.


--------------------------------------------------

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]


--------------------------------------------------

Example 2:


Input: root = []
Output: []



Constraints:


	The number of nodes in the tree is in the range [0, 10⁴].
	-1000 <= Node.val <= 1000

################################################################


297. 二叉树的序列化与反序列化
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。



示例 1：

          1
     2         3
            4     5


输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]


示例 2：

输入：root = []
输出：[]


示例 3：

输入：root = [1]
输出：[1]


示例 4：

输入：root = [1,2]
输出：[1,2]


提示：

树中结点数在范围 [0, 104] 内
-1000 <= Node.val <= 1000


"""


# from algo.tree.builder import TreeNode




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


class Codec:
    SEP = ','
    NONE = '#'

    def format(self, root):
        if root is None:
            self.s += f"{self.NONE}{self.SEP}"
            return

        # 前序
        self.s += f"{root.val}{self.SEP}"
        # print(f"s: {self.s}")

        self.format(root.left)
        self.format(root.right)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        self.s = ''
        self.format(root)
        return self.s

    def build(self, nodes):
        if not nodes:
            return None

        # 前序遍历，第一个元素就是根节点
        first = nodes.pop(0)
        if first == self.NONE:
            return None
        root = TreeNode(first)
        root.left = self.build(nodes)
        root.right = self.build(nodes)

        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(self.SEP)
        return self.build(nodes)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Codec()

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

        # self.assertEqual(
        #     self.sl,
        #     None,
        # )
        root.log()
        ss = self.sl.serialize(root)
        print(ss)
        self.sl.deserialize(ss).log()


if __name__ == "__main__":
    unittest.main()
