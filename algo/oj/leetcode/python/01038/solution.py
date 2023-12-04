# Created by shiyang07ca at 2023/12/04 22:34
# leetgo: dev
# https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 链接：https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            nonlocal s
            if root is None:
                return
            dfs(root.right)
            s += root.val
            root.val = s
            dfs(root.left)

        s = 0
        dfs(root)
        return root


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().bstToGst(root)

    print("\noutput:", serialize(ans))
