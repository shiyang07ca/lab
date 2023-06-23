# Created by shiyang07ca at 2023/05/22 08:40
# https://leetcode.cn/problems/insufficient-nodes-in-root-to-leaf-paths/

"""
1080. 根到叶路径上的不足节点 (Medium)
给你二叉树的根节点 `root` 和一个整数 `limit` ，请你同时删除树中所有 **不足节点**，并返回最终二叉树的
根节点。

假如通过节点 `node` 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 `limit`，则该节点被称之为 **不
足节点**，需要被删除。

**叶子节点**，就是没有子节点的节点。

**示例 1：**

![](https://assets.leetcode.com/uploads/2019/06/05/insufficient-11.png)

```
输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
输出：[1,2,3,4,null,null,7,8,9,null,14]

```

**示例 2：**

![](https://assets.leetcode.com/uploads/2019/06/05/insufficient-3.png)

```
输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
输出：[5,4,8,11,null,17,4,7,null,null,null,5]

```

**示例 3：**

![](https://assets.leetcode.com/uploads/2019/06/11/screen-shot-2019-06-11-at-83301-pm.png)

```
输入：root = [1,2,-3,-5,null,4,null], limit = -1
输出：[1,null,-3,4]

```

**提示：**

- 树中节点数目在范围 `[1, 5000]` 内
- `-10⁵ <= Node.val <= 10⁵`
- `-10⁹ <= limit <= 10⁹`

"""

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
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        def dfs(node, limit):
            if not node.left and not node.right:
                if node.val < limit:
                    return None
                else:
                    return node

            left = right = None
            if node.left:
                left = dfs(node.left, limit - node.val)
            if node.right:
                right = dfs(node.right, limit - node.val)
            if not left and not right:
                return None
            else:
                node.left = left
                node.right = right
                return node

        return dfs(root, limit)


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().sufficientSubset(root, limit)

    print("\noutput:", serialize(ans))
