"""

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

6223. Height of Binary Tree After Subtree Removal Queries

You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.


Example 1:


Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).
Example 2:


Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).


Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
m == queries.length
1 <= m <= min(n, 104)
1 <= queries[i] <= n
queries[i] != root.val

################################################################

# TODO
# tag: DFS, dp

6223. 移除子树后的二叉树高度
给你一棵 二叉树 的根节点 root ，树中有 n 个节点。每个节点都可以被分配一个从 1 到 n 且互不相同的值。另给你一个长度为 m 的数组 queries 。

你必须在树上执行 m 个 独立 的查询，其中第 i 个查询你需要执行以下操作：

从树中 移除 以 queries[i] 的值作为根节点的子树。题目所用测试用例保证 queries[i] 不 等于根节点的值。
返回一个长度为 m 的数组 answer ，其中 answer[i] 是执行第 i 个查询后树的高度。

注意：

查询之间是独立的，所以在每个查询执行后，树会回到其 初始 状态。
树的高度是从根到树中某个节点的 最长简单路径中的边数 。


示例 1：

       1                          1

    3    4       =>            3

  2    6   5                 2
            7


输入：root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
输出：[2]
解释：上图展示了从树中移除以 4 为根节点的子树。
树的高度是 2（路径为 1 -> 3 -> 2）。


示例 2：

              5
       8              9
    2    1         3     7
   4  6


输入：root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
输出：[3,2,3,2]
解释：执行下述查询：
- 移除以 3 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 4）。
- 移除以 2 为根节点的子树。树的高度变为 2（路径为 5 -> 8 -> 1）。
- 移除以 4 为根节点的子树。树的高度变为 3（路径为 5 -> 8 -> 2 -> 6）。
- 移除以 8 为根节点的子树。树的高度变为 2（路径为 5 -> 9 -> 3）。


提示：

树中节点的数目是 n
2 <= n <= 10^5
1 <= Node.val <= n
树中的所有值 互不相同
m == queries.length
1 <= m <= min(n, 10^4)
1 <= queries[i] <= n
queries[i] != root.val

"""

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/height-of-binary-tree-after-subtree-removal-queries/solution/liang-bian-dfspythonjavacgo-by-endlessch-vvs4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

既然是求树的高度，我们可以先跑一遍 DFS，求出每棵子树的高度 height（这里定义成最
长路径的节点数）。

然后再 DFS 一遍这棵树，同时维护当前节点深度 depth（从 0 开始），
以及删除当前子树后剩余部分的树的高度 restH（这里定义成最长路径的边数）。


具体做法如下：

- 往左走，递归前算一下从根节点到当前节点右子树最深节点的长度，即 depth +
height[node.right]，与 restH 取最大值，然后往下递归；
- 往右走，递归前算一下从根节点到当前节点左子树最深节点的长度，即 depth +
height[node.left]，与 restH 取最大值，然后往下递归。

每个节点的答案即为递归到该节点时的 restH 值。
代码实现时可以直接把答案覆盖到 queries 数组中。

"""


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = defaultdict(int)  # 每棵子树的高度

        def get_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            height[node] = 1 + max(get_height(node.left), get_height(node.right))
            return height[node]

        get_height(root)

        res = [0] * (len(height) + 1)  # 每个节点删除后，其余部分的最大高度

        def dfs(node: Optional[TreeNode], depth: int, rest_h: int) -> None:
            if node is None:
                return
            depth += 1
            res[node.val] = rest_h
            dfs(node.left, depth, max(rest_h, depth + height[node.right]))
            dfs(node.right, depth, max(rest_h, depth + height[node.left]))

        dfs(root, -1, 0)

        for i, q in enumerate(queries):
            queries[i] = res[q]
        return queries
