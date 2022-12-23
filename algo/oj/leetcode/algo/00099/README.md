## 题目

[99. 恢复二叉搜索树](https://leetcode.cn/problems/recover-binary-search-tree/)

---

给你二叉搜索树的根节点 `root` ，该树中的 **恰好** 两个节点的值被错误地交换。*请在不改变其结构的情况下，恢复这棵树* 。



**示例 1：**

![](https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg)
```txt
输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
```

**示例 2：**

![](https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg)
```txt
输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
```


**提示：**

-   树上节点的数目在范围 `[2, 1000]` 内
-   `-2^31 <= Node.val <= 2^31 - 1`



**进阶：**使用 `O(n)` 空间复杂度的解法很容易实现。你能想出一个只使用 `O(1)` 空间的解决方案吗？



## 解题

### 方法一：

#### 思路



#### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            arr.append(node)
            dfs(node.right)

        arr = []
        dfs(root)
        # print(arr)
        x = y = None
        for a, b in pairwise(arr):
            if not x and a.val >= b.val:
                x = a
            if x and a.val >= b.val:
                y = b

            # print(a.val, b.val)
        # print(x, y)
        x.val, y.val = y.val, x.val


```
