"""

6247. Remove Nodes From Linked List

You are given the head of a linked list.

Remove every node which has a node with a strictly greater value anywhere to the right side of it.

Return the head of the modified linked list.



Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.


Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.


Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105


################################################################


6247. 从链表中移除节点

给你一个链表的头节点 head 。

对于列表中的每个节点 node ，如果其右侧存在一个具有 严格更大 值的节点，则移除 node 。

返回修改后链表的头节点 head 。


示例 1：

 5 2 13 3 8    =>    13 8

输入：head = [5,2,13,3,8]
输出：[13,8]
解释：需要移除的节点是 5 ，2 和 3 。
- 节点 13 在节点 5 右侧。
- 节点 13 在节点 2 右侧。
- 节点 8 在节点 3 右侧。


示例 2：

输入：head = [1,1,1,1]
输出：[1,1,1,1]
解释：每个节点的值都是 1 ，所以没有需要移除的节点。


提示：

给定列表中的节点数目在范围 [1, 10^5] 内
1 <= Node.val <= 105

"""

"""
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_gt(nums):
            N = len(nums)
            right = [-1] * N
            st = []
            for i, n in enumerate(nums):
                while st and nums[st[-1]] < n:
                    popi = st.pop()
                    right[popi] = i
                st.append(i)
            return right

        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        head = tmp = ListNode()
        p = get_gt(nums)
        for i, n in enumerate(nums):
            if p[i] == -1:
                tmp.next = ListNode(n)
                tmp = tmp.next
        return head.next


"""

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/D1fgh9/view/LGcCHr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

由于一个节点的取舍取决于后面有无大于它的数，这在链表中相对难以处理，于是我们将链
表转为数组查看。而我们从后往前遍历数组，遇到不小于当前最大值的加入最终链表元素中，
最终生成链表。

"""


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        res = []
        while nums:
            val = nums.pop()
            if len(res) == 0 or res[-1] <= val:
                res.append(val)
        ans = ListNode()
        tmp = ans
        while res:
            tmp.next = ListNode(res.pop())
            tmp = tmp.next
        return ans.next


"""
作者：endlesscheng
链接：https://leetcode.cn/problems/remove-nodes-from-linked-list/solution/di-gui-jian-ji-xie-fa-by-endlesscheng-jfwi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

递归，返回链表头和链表的最大值。
"""


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def f(node):
            if node is None:
                return None, 0
            res, max = f(node.next)
            if max > node.val:
                return res, max  # 删除 node
            node.next = res  # 不删除 node
            return node, node.val  # 返回最大值

        return f(head)[0]


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        head.next = self.removeNodes(head.next)
        if head.next:
            if head.val < head.next.val:
                return head.next

        return head
