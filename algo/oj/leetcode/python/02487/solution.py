# Created by shiyang07ca at 2024/01/03 00:01
# leetgo: dev
# https://leetcode.cn/problems/remove-nodes-from-linked-list/

from bisect import *
from typing import *

from leetgo_py import *

# @lc code=begin

from sortedcontainers import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ns = []
        cur = head
        while cur:
            ns.append(cur.val)
            cur = cur.next

        pre = ListNode(ns[-1])
        sl = SortedList([ns[-1]])
        for n in ns[-2::-1]:
            if sl.bisect_right(n) == len(sl):
                t = ListNode(n)
                t.next = pre
                pre = t
            sl.add(n)

        return pre


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().removeNodes(head)

    print("\noutput:", serialize(ans))
