# Created by shiyang07ca at 2023/07/31 00:00
# leetgo: dev
# https://leetcode.cn/problems/reorder-list/

from typing import *

from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(head):
            if not head or not head.next:
                return head
            ans = None
            while head:
                cur = head
                head = head.next
                cur.next = ans
                ans = cur
            return ans

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = reverse(slow)
        ans = dummy = ListNode()
        print(serialize(slow), serialize(head), serialize(mid))
        while head is not slow or mid:
            if head is not slow:
                dummy.next = head
                head = head.next
                dummy = dummy.next
            if mid:
                dummy.next = mid
                mid = mid.next
                dummy = dummy.next
        return ans.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    Solution().reorderList(head)
    ans = head

    print("\noutput:", serialize(ans))
