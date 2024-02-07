# Created by shiyang07ca at 2024/02/08 00:37
# leetgo: dev
# https://leetcode.cn/problems/cousins-in-binary-tree/

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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if (
                    cur.left
                    and cur.right
                    and cur.left.val in (x, y)
                    and cur.right.val in (x, y)
                ):
                    return False

                if cur.left:
                    queue.append(cur.left)
                    level.append(cur.left.val)
                if cur.right:
                    queue.append(cur.right)
                    level.append(cur.right.val)

                if x in level and y in level:
                    return True

        return False


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().isCousins(root, x, y)

    print("\noutput:", serialize(ans))
