"""

[654] Maximum Binary Tree


You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:


	Create a root node whose value is the maximum value in nums.
	Recursively build the left subtree on the subarray prefix to the left of the maximum value.
	Recursively build the right subtree on the subarray suffix to the right of the maximum value.


Return the maximum binary tree built from nums.


--------------------------------------------------

Example 1:


Input: nums = [3,2,1,6,0,5]
Output: [6,3,5,null,2,0,null,null,1]
Explanation: The recursive calls are as follow:
- The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
    - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
        - Empty array, so no child.
        - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
            - Empty array, so no child.
            - Only one element, so child is a node with value 1.
    - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
        - Only one element, so child is a node with value 0.
        - Empty array, so no child.


--------------------------------------------------

Example 2:


Input: nums = [3,2,1]
Output: [3,null,2,null,1]



Constraints:


	1 <= nums.length <= 1000
	0 <= nums[i] <= 1000
	All integers in nums are unique.


################################################################



654. 最大二叉树
给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

- 创建一个根节点，其值为 nums 中的最大值。
- 递归地在最大值 左边 的 子数组前缀上 构建左子树。
- 递归地在最大值 右边 的 子数组后缀上 构建右子树。
- 返回 nums 构建的 最大二叉树 。


示例 1：

              6
          3       5
           2     0
            1

输入：nums = [3,2,1,6,0,5]
输出：[6,3,5,null,2,0,null,null,1]
解释：递归调用如下所示：
- [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
        - 空数组，无子节点。
        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
            - 空数组，无子节点。
            - 只有一个元素，所以子节点是一个值为 1 的节点。
    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
        - 只有一个元素，所以子节点是一个值为 0 的节点。
        - 空数组，无子节点。

示例 2：
           3
             2
               1

输入：nums = [3,2,1]
输出：[3,null,2,null,1]


提示：

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
nums 中的所有整数 互不相同


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
    def getMaxIndex(self, nums, l, r):
        index = -1
        max_ = -1
        for i, n in enumerate(nums[l : r + 1]):
            if n > max_:
                max_ = n
                index = i
        return l + index

    def build(self, nums, l, r):
        if l > r:
            return None

        i = self.getMaxIndex(nums, l, r)
        node = TreeNode(nums[i])
        node.left = self.build(nums, l, i - 1)
        node.right = self.build(nums, i + 1, r)

        return node

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums, 0, len(nums) - 1)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        """
            6
        3       5
         2     0
          1

        """
        n1 = TreeNode(6)
        n1.left = TreeNode(3)
        n1.left.right = TreeNode(2)
        n1.left.right.right = TreeNode(1)
        n1.right = TreeNode(5)
        n1.right.left = TreeNode(0)
        n1.log()

        nums = [3, 2, 1, 6, 0, 5]
        self.sl.constructMaximumBinaryTree(nums).log()
        # self.assertEqual(
        #     self.sl,
        #     None,
        # )

    def test_sl2(self):
        """
        3
          2
            1
        """
        n1 = TreeNode(3)
        n1.right = TreeNode(2)
        n1.right.right = TreeNode(1)
        n1.log()

        nums = [3, 2, 1]
        self.sl.constructMaximumBinaryTree(nums).log()


if __name__ == "__main__":
    unittest.main()
