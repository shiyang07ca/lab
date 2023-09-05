# Created by shiyang07ca at 2023/09/06 00:19
# leetgo: dev
# https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/

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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None

            dep_l, node_l = dfs(node.left)
            dep_r, node_r = dfs(node.right)
            if dep_l == dep_r:
                return dep_l + 1, node
            elif dep_l < dep_r:
                return dep_r + 1, node_r
            else:
                return dep_l + 1, node_l

        return dfs(root)[1]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().lcaDeepestLeaves(root)

    print("\noutput:", serialize(ans))
