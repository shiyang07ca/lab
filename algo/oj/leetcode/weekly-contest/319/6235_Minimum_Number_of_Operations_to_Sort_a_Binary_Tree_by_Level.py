"""

6235. Minimum Number of Operations to Sort a Binary Tree by Level

You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.


Example 1:


Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 2:


Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 3:


Input: root = [1,2,3,4,5,6]
Output: 0
Explanation: Each level is already sorted in increasing order so return 0.


Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
All the values of the tree are unique.

################################################################

# TODO

6235. 逐层排序二叉树所需的最少操作数目

给你一个 值互不相同 的二叉树的根节点 root 。

在一步操作中，你可以选择 同一层 上任意两个节点，交换这两个节点的值。

返回每一层按 严格递增顺序 排序所需的最少操作数目。

节点的 层数 是该节点和根节点之间的路径的边数。


示例 1 ：


输入：root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
输出：3
解释：
- 交换 4 和 3 。第 2 层变为 [3,4] 。
- 交换 7 和 5 。第 3 层变为 [5,6,8,7] 。
- 交换 8 和 7 。第 3 层变为 [5,6,7,8] 。
共计用了 3 步操作，所以返回 3 。
可以证明 3 是需要的最少操作数目。


示例 2 ：


输入：root = [1,3,2,7,6,5,4]
输出：3
解释：
- 交换 3 和 2 。第 2 层变为 [2,3] 。
- 交换 7 和 4 。第 3 层变为 [4,6,5,7] 。
- 交换 6 和 5 。第 3 层变为 [4,5,6,7] 。
共计用了 3 步操作，所以返回 3 。
可以证明 3 是需要的最少操作数目。


示例 3 ：


输入：root = [1,2,3,4,5,6]
输出：0
解释：每一层已经按递增顺序排序，所以返回 0 。


提示：

树中节点的数目在范围 [1, 105] 。
1 <= Node.val <= 105
树中的所有值 互不相同 。


"""


from typing import *
import sys
import inspect
import os
from os.path import abspath, join, dirname


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import TreeNode

# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0

        def count(arr):
            c = 0
            mp = {}
            sarr = sorted(arr)
            for i, n in enumerate(sarr):
                mp[n] = i

            for i in range(len(arr)):
                while arr[i] != sarr[i]:
                    j = mp[arr[i]]
                    arr[j], arr[i] = arr[i], arr[j]
                    c += 1
            return c

        ans = 0
        q = [root]
        while q:
            l = []
            for _ in range(len(q)):
                root = q.pop(0)
                l.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            ans += count(l)

        return ans


"""

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/solution/by-endlesscheng-97i9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


求整个序列中置换环的数量，答案就是序列长度减去置换环的数量。

"""


class Solution1:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans, q = 0, [root]
        while q:
            a = []
            tmp = q
            q = []
            for node in tmp:
                a.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            b = sorted(a)
            a = [bisect_left(b, v) for v in a]  # 离散化

            vis = [False] * len(a)
            t = 0
            for v in a:
                if vis[v]:
                    continue
                while not vis[v]:
                    vis[v] = True
                    v = a[v]
                t += 1
            ans += len(a) - t
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        root = [1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]
        self.assertEqual(
            self.sl.minimumOperations(root),
            3,
        )


if __name__ == "__main__":
    unittest.main()
