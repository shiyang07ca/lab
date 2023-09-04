# Created by shiyang07ca at 2023/09/04 08:20
# leetgo: dev
# https://leetcode.cn/problems/serialize-and-deserialize-bst/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TODO:


# https://leetcode.cn/problems/serialize-and-deserialize-bst/solutions/1485442/by-ac_oier-ncwn/?envType=daily-question&envId=2023-09-04
class Codec1:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""

        def dfs(root):
            if root is None:
                return ""
            nums.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        nums = []
        dfs(root)
        return "#".join(nums)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""

        def dfs(l, r):
            if l > r:
                return None

            j = bisect_right(vs, vs[l], lo=l + 1, hi=r + 1)
            root = TreeNode(vs[l])
            root.left = dfs(l + 1, j - 1)
            root.right = dfs(j, r)
            return root

        if not data:
            return None

        vs = list(map(int, data.split("#")))
        return dfs(0, len(vs) - 1)


# 链接：https://leetcode.cn/problems/serialize-and-deserialize-bst/solutions/1479903/xu-lie-hua-he-fan-xu-lie-hua-er-cha-sou-5m9r4/
class Codec:
    def serialize(self, root: TreeNode) -> str:
        arr = []

        def postOrder(root: TreeNode) -> None:
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            arr.append(root.val)

        postOrder(root)
        return " ".join(map(str, arr))

    def deserialize(self, data: str) -> TreeNode:
        arr = list(map(int, data.split()))

        def construct(lower: int, upper: int) -> TreeNode:
            if arr == [] or arr[-1] < lower or arr[-1] > upper:
                return None
            val = arr.pop()
            root = TreeNode(val)
            root.right = construct(val, upper)
            root.left = construct(lower, val)
            return root

        return construct(-inf, inf)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().CodecDriver(root)

    print("\noutput:", serialize(ans))
