# Created by shiyang07ca at 2023/07/14 10:15
# leetgo: dev
# https://leetcode.cn/problems/distribute-coins-in-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        pass


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().distributeCoins(root)

    print("\noutput:", serialize(ans))
