# Created by shiyang07ca at 2024/04/24 00:02
# leetgo: dev
# https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/

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
    # 链接：https://leetcode.cn/problems/amount-of-time-for-binary-tree-to-be-infected/solutions/2753470/cong-liang-ci-bian-li-dao-yi-ci-bian-li-tmt0x/
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        fa = {}
        start_node = None

        def dfs(node: Optional[TreeNode], from_: Optional[TreeNode]) -> None:
            if node is None:
                return
            fa[node] = from_  # 记录每个节点的父节点
            if node.val == start:  # 找到 start
                nonlocal start_node
                start_node = node
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        def maxDepth(node: Optional[TreeNode], from_: TreeNode) -> int:
            if node is None:
                return -1  # 注意这里是 -1，因为 start 的深度为 0
            return (
                max(
                    maxDepth(x, node)
                    for x in (node.left, node.right, fa[node])
                    if x != from_
                )
                + 1
            )

        return maxDepth(start_node, start_node)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().amountOfTime(root, start)
    print("\noutput:", serialize(ans, "integer"))
