# Created by shiyang07ca at 2023/08/13 10:32
# leetgo: dev
# https://leetcode.cn/problems/double-a-number-represented-as-a-linked-list/
# https://leetcode.cn/contest/weekly-contest-358/problems/double-a-number-represented-as-a-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_iter(head):
            if not head or not head.next:
                return head

            pre = None
            while head:
                cur = head
                head = head.next
                cur.next = pre
                pre = cur
            return pre

        # 链接：https://leetcode.cn/circle/discuss/9wQ08W/view/4drty4/
        head = reverse_iter(head)
        carry = 0
        tmp = head
        while tmp:
            v = tmp.val * 2 + carry
            carry, tmp.val = divmod(v, 10)
            tmp = tmp.next
        head = reverse_iter(head)
        return ListNode(carry, head) if carry else head


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().doubleIt(head)

    print("\noutput:", serialize(ans))
