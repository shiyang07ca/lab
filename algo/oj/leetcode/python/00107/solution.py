# Created by shiyang07ca at 2024/02/15 13:54
# leetgo: dev
# https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/

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
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = [root]
        ans = []
        while q:
            t = []
            for _ in range(len(q)):
                cur = q.pop(0)
                t.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.insert(0, t)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrderBottom(root)

    print("\noutput:", serialize(ans))
