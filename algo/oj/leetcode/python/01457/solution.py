# Created by shiyang07ca at 2023/11/25 22:43
# leetgo: dev
# https://leetcode.cn/problems/pseudo-palindromic-paths-in-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, pre):
            if not node.left and not node.right:
                nonlocal ans
                ans += 1 if pre.bit_count() <= 1 else 0
                return

            if node.left:
                dfs(node.left, pre ^ (1 << (node.left.val - 1)))
            if node.right:
                dfs(node.right, pre ^ (1 << (node.right.val - 1)))

        dfs(root, (1 << (root.val - 1)))
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().pseudoPalindromicPaths(root)

    print("\noutput:", serialize(ans))
