"""

6242. Closest Nodes Queries in a Binary Search Tree

You are given the root of a binary search tree and an array queries of size n consisting of positive integers.

Find a 2D array answer of size n where answer[i] = [mini, maxi]:

mini is the largest value in the tree that is smaller than or equal to queries[i]. If a such value does not exist, add -1 instead.
maxi is the smallest value in the tree that is greater than or equal to queries[i]. If a such value does not exist, add -1 instead.
Return the array answer.



Example 1:


Input: root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
Output: [[2,2],[4,6],[15,-1]]
Explanation: We answer the queries in the following way:
- The largest number that is smaller or equal than 2 in the tree is 2, and the smallest number that is greater or equal than 2 is still 2. So the answer for the first query is [2,2].
- The largest number that is smaller or equal than 5 in the tree is 4, and the smallest number that is greater or equal than 5 is 6. So the answer for the second query is [4,6].
- The largest number that is smaller or equal than 16 in the tree is 15, and the smallest number that is greater or equal than 16 does not exist. So the answer for the third query is [15,-1].
Example 2:


Input: root = [4,null,9], queries = [3]
Output: [[-1,4]]
Explanation: The largest number that is smaller or equal to 3 in the tree does not exist, and the smallest number that is greater or equal to 3 is 4. So the answer for the query is [-1,4].


Constraints:

The number of nodes in the tree is in the range [2, 105].
1 <= Node.val <= 106
n == queries.length
1 <= n <= 105
1 <= queries[i] <= 106

################################################################

# TODO
# tag: DFS, BST, binary search


6242. 二叉搜索树最近节点查询 显示英文描述

给你一个 二叉搜索树 的根节点 root ，和一个由正整数组成、长度为 n 的数组 queries 。

请你找出一个长度为 n 的 二维 答案数组 answer ，其中 answer[i] = [mini, maxi] ：

mini 是树中小于等于 queries[i] 的 最大值 。如果不存在这样的值，则使用 -1 代替。
maxi 是树中大于等于 queries[i] 的 最小值 。如果不存在这样的值，则使用 -1 代替。
返回数组 answer 。



示例 1 ：

输入：root = [6,2,13,1,4,9,15,null,null,null,null,null,null,14], queries = [2,5,16]
输出：[[2,2],[4,6],[15,-1]]
解释：按下面的描述找出并返回查询的答案：
- 树中小于等于 2 的最大值是 2 ，且大于等于 2 的最小值也是 2 。所以第一个查询的答案是 [2,2] 。
- 树中小于等于 5 的最大值是 4 ，且大于等于 5 的最小值是 6 。所以第二个查询的答案是 [4,6] 。
- 树中小于等于 16 的最大值是 15 ，且大于等于 16 的最小值不存在。所以第三个查询的答案是 [15,-1] 。


示例 2 ：

输入：root = [4,null,9], queries = [3]
输出：[[-1,4]]
解释：树中不存在小于等于 3 的最大值，且大于等于 3 的最小值是 4 。所以查询的答案是 [-1,4] 。

提示：

树中节点的数目在范围 [2, 105] 内
1 <= Node.val <= 106
n == queries.length
1 <= n <= 105
1 <= queries[i] <= 106

"""

from typing import *
from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TLE
class Solution:
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        @cache
        def find1(root, v):
            if root is None:
                return -1

            if root.val == v:
                return v
            elif root.val > v:
                return find1(root.left, v)
            elif root.val < v:
                if root.right is None:
                    return root.val
                else:
                    if root.right.val > v:
                        r = find1(root.right.left, v)
                        if r == -1:
                            return root.val
                        else:
                            return max(root.val, r)
                    else:
                        return find1(root.right, v)

        @cache
        def find2(root, v):
            if root is None:
                return -1

            if root.val == v:
                return v
            elif root.val < v:
                return find2(root.right, v)
            elif root.val > v:
                if root.left is None:
                    return root.val
                else:
                    if root.left.val < v:
                        r = find2(root.left.right, v)
                        if r == -1:
                            return root.val
                        else:
                            return min(root.val, r)
                    else:
                        return find2(root.left, v)

        ans = []
        for n in queries:
            a = find1(root, n)
            b = find2(root, n)
            ans.append([a, b])
        #             print(n, a)

        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/solution/zhong-xu-bian-li-er-fen-cha-zhao-by-endl-m8ez/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from bisect import *


class Solution1:
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        a = []

        def dfs(o: Optional[TreeNode]) -> None:
            if o is None:
                return
            dfs(o.left)
            a.append(o.val)
            dfs(o.right)

        dfs(root)

        ans = []
        for q in queries:
            j = bisect_right(a, q)
            min = a[j - 1] if j else -1
            j = bisect_left(a, q)
            max = a[j] if j < len(a) else -1
            ans.append([min, max])
        return ans


if __name__ == "__main__":
    n1 = TreeNode(6)
    n2 = TreeNode(2)
    n3 = TreeNode(13)
    n1.left = n2
    n1.right = n3
    n2.left = TreeNode(1)
    n2.right = TreeNode(4)
    n3.left = TreeNode(9)
    n3.right = TreeNode(15)
    n3.right.left = TreeNode(14)

    queries = [2, 5, 16]
    sl = Solution1()
    print(sl.closestNodes(n1, queries))
    assert sl.closestNodes(n1, queries) == [[2, 2], [4, 6], [15, -1]]
