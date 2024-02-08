# Created by shiyang07ca at 2024/02/09 00:30
# leetgo: dev
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # 链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solutions/240096/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return  # 1.
        if not left:
            return right  # 3.
        if not right:
            return left  # 4.
        return root  # 2. if left and right:


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)

    print("\noutput:", serialize(ans))
